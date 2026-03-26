import type { Handler } from "@netlify/functions";
import { createClient } from "@netlify/functions";

const client = createClient({
  allowedOrigins: ["https://hendrik-spritpreise.netlify.app"]
});

interface Snapshot {
  timestamp: string;
  location: { lat: number; lng: number };
  stats: { min: number; avg: number };
  stations: Array<{ name: string; brand: string; price: number; diesel?: number; e5?: number; e10?: number }>;
}

export const handler: Handler = async (event, context) => {
  if (event.httpMethod !== "POST") {
    return client.res(405, { error: "Method not allowed" });
  }

  try {
    const snapshot: Snapshot = JSON.parse(event.body || "{}");
    const apiKey = process.env.MATON_API_KEY;
    if (!apiKey) {
      return client.res(500, { error: "MATON_API_KEY not set" });
    }

    const stamp = snapshot.timestamp.split("T")[0];
    const pageRes = await fetch("https://gateway.maton.ai/notion/v1/pages", {
      method: "POST",
      headers: {
        "Authorization": `Bearer ${apiKey}`,
        "Content-Type": "application/json",
        "Notion-Version": "2025-09-03"
      },
      body: JSON.stringify({
        parent: { workspace: true },
        properties: {
          title: {
            title: [{ type: "text", text: { content: `Spritpreise Live ${stamp}` } }]
          }
        },
        children: [
          {
            object: "block",
            type: "paragraph",
            paragraph: {
              rich_text: [{ type: "text", text: { content: "Automatischer Snapshot der Spritpreise in deiner Nähe." } }]
            }
          }
        ]
      })
    });

    if (!pageRes.ok) {
      const text = await pageRes.text();
      return client.res(500, { error: "Notion page creation failed", details: text });
    }

    const page = await pageRes.json();
    const pageId = page["id"];

    const blocks = [
      {
        object: "block",
        type: "heading_2",
        heading_2: { rich_text: [{ type: "text", text: { content: "Snapshot" } }] }
      },
      {
        object: "block",
        type: "code",
        code: {
          rich_text: [{ type: "text", text: { content: JSON.stringify(snapshot, null, 2) } }],
          language: "json"
        }
      },
      {
        object: "block",
        type: "heading_2",
        heading_2: { rich_text: [{ type: "text", text: { content: "Statistiken" } }] }
      },
      {
        object: "block",
        type: "paragraph",
        paragraph: {
          rich_text: [{ type: "text", text: { content: `Min: ${snapshot.stats.min.toFixed(3)} € | Avg: ${snapshot.stats.avg.toFixed(3)} €` } }]
        }
      },
      {
        object: "block",
        type: "heading_2",
        heading_2: { rich_text: [{ type: "text", text: { content: "Top‑5 Tankstellen" } }] }
      }
    ];

    snapshot.stations.slice(0, 5).forEach((s, i) => {
      const line = `${i + 1}. ${s.name} (${s.brand}) — Preis: ${s.price.toFixed(3)} €`;
      blocks.push({
        object: "block",
        type: "paragraph",
        paragraph: { rich_text: [{ type: "text", text: { content: line } }] }
      });
    });

    const appendRes = await fetch(`https://gateway.maton.ai/notion/v1/blocks/${pageId}/children`, {
      method: "PATCH",
      headers: {
        "Authorization": `Bearer ${apiKey}`,
        "Content-Type": "application/json",
        "Notion-Version": "2025-09-03"
      },
      body: JSON.stringify({ children: blocks })
    });

    if (!appendRes.ok) {
      const text = await appendRes.text();
      return client.res(500, { error: "Notion append failed", details: text });
    }

    return client.res(200, { url: page.url, pageId });
  } catch (err) {
    console.error(err);
    return client.res(500, { error: (err as Error).message });
  }
};