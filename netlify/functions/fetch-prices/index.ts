import type { Handler } from "@netlify/functions";
import { createClient } from "@netlify/functions";

const client = createClient({
  allowedOrigins: ["https://hendrik-spritpreise.netlify.app"]
});

const TANKERKOENIG_API_KEY = process.env.TANKERKOENIG_API_KEY;

interface Station {
  id: string;
  name: string;
  brand: string;
  price: number;
  diesel?: number;
  e5?: number;
  e10?: number;
  lat: number;
  lng: number;
}

export const handler: Handler = async (event, context) => {
  if (event.httpMethod !== "POST") {
    return client.res(405, { error: "Method not allowed" });
  }

  try {
    const body = JSON.parse(event.body || "{}");
    const { lat, lng, radius = 5 } = body;

    if (!lat || !lng) {
      return client.res(400, { error: "Missing lat or lng" });
    }

    // Find nearby stations
    const stationsUrl = `https://creativecommons.tankerkoenig.de/json/list.php?lat=${lat}&lng=${lng}&rad=${radius}&type=all&apikey=${TANKERKOENIG_API_KEY}`;
    const resp = await fetch(stationsUrl);
    const data = await resp.json();

    if (!data.ok) {
      return client.res(500, { error: data.message || "Tankerkoenig API error" });
    }

    const stations = (data.stations || []).filter((s: any) => s.isOpen).map((s: any): Station => ({
      id: s.id,
      name: s.name,
      brand: s.brand,
      price: s.diesel || s.e5 || s.e10 || 0,
      diesel: s.diesel,
      e5: s.e5,
      e10: s.e10,
      lat: s.lat,
      lng: s.lng
    })).slice(0, 20);

    const prices = stations.map(s => s.price);
    const minPrice = Math.min(...prices);
    const maxPrice = Math.max(...prices);
    const avgPrice = prices.reduce((a, b) => a + b, 0) / prices.length;

    return client.res(200, {
      stations,
      stats: { minPrice, maxPrice, avgPrice, count: stations.length }
    });
  } catch (err) {
    console.error(err);
    return client.res(500, { error: (err as Error).message });
  }
};