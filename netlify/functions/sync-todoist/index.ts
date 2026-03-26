import type { Handler } from "@netlify/functions";
import { createClient } from "@netlify/functions";

const client = createClient({
  allowedOrigins: ["https://hendrik-sci-fi-books.netlify.app", "https://69b8a8f98b88e0fa0a89315d--hendrik-sci-fi-books.netlify.app"]
});

export const handler: Handler = async (event, context) => {
  if (event.httpMethod !== "POST") {
    return client.res(405, { error: "Method not allowed" });
  }

  try {
    const body = JSON.parse(event.body || "{}");
    const items: Array<{date: string; title: string; level: string}> = body.items || [];

    if (!Array.isArray(items) || items.length === 0) {
      return client.res(400, { error: "Missing or empty items" });
    }

    const apiKey = process.env.MATON_API_KEY;
    if (!apiKey) {
      return client.res(500, { error: "MATON_API_KEY not set" });
    }

    const created = [];
    for (const item of items.slice(0, 12)) {
      const {date, title, level} = item;
      if (!date || !title) continue;

      const task = {
        content: `📖 Sci-Fi Leseplan: ${title}`,
        description: `Schwierigkeit: ${level || "?"}`,
        due_string: date
      };

      const resp = await fetch("https://gateway.maton.ai/todoist/api/v1/tasks", {
        method: "POST",
        headers: {
          "Authorization": `Bearer ${apiKey}`,
          "Content-Type": "application/json"
        },
        body: JSON.stringify(task)
      });

      if (resp.ok) {
        created.push({date, title, status: "created"});
      } else {
        created.push({date, title, status: "failed", error: resp.statusText});
      }
    }

    return client.res(200, {created, total: created.length});
  } catch (err) {
    console.error(err);
    return client.res(500, {error: (err as Error).message});
  }
};