---
name: ki-connect
description: Configure and manage ki-connect NRW model provider for OpenClaw. Use when setting up ki-connect API access, adding FH Aachen models (gpt-5.2, gpt-5-nano), or troubleshooting ki-connect integration. Triggers: "ki-connect setup", "add ki-connect models", "FH Aachen AI", "kiconnect nrw".
---

# ki-connect NRW Model Provider

ki-connect is an OpenAI-compatible API provided by FH Aachen/NRW with access to GPT-5 models.

## Available Models

- `gpt-5.2` — Full GPT-5.2 model
- `gpt-5-nano` — Lightweight GPT-5 nano model

## API Details

- **Base URL:** `https://chat.kiconnect.nrw/api/v1`
- **Auth:** Bearer token (API key format: `userid:apikey`)
- **Compatibility:** OpenAI API (chat/completions endpoint)

## Configuration

### Step 1: Add API Key to Environment

Add the ki-connect API key to `~/.bashrc`:

```bash
export KICONNECT_API_KEY="your-api-key-here"
```

Then reload: `source ~/.bashrc`

### Step 2: Add Provider to openclaw.json

Add the ki-connect provider to `~/.openclaw/openclaw.json` under `models.providers`:

```json
"kiconnect": {
  "api": "openai-completions",
  "apiKey": "${KICONNECT_API_KEY}",
  "baseUrl": "https://chat.kiconnect.nrw/api/v1",
  "models": [
    {
      "id": "gpt-5.2",
      "name": "GPT-5.2 (ki-connect)",
      "contextWindow": 128000,
      "maxTokens": 4096,
      "input": ["text"],
      "reasoning": false,
      "cost": {
        "input": 0,
        "output": 0,
        "cacheRead": 0,
        "cacheWrite": 0
      }
    },
    {
      "id": "gpt-5-nano",
      "name": "GPT-5 Nano (ki-connect)",
      "contextWindow": 128000,
      "maxTokens": 4096,
      "input": ["text"],
      "reasoning": false,
      "cost": {
        "input": 0,
        "output": 0,
        "cacheRead": 0,
        "cacheWrite": 0
      }
    }
  ]
}
```

### Step 3: Use the Models

Once configured, reference the models as `kiconnect/gpt-5.2` or `kiconnect/gpt-5-nano` in your OpenClaw configuration (primary, fallbacks, or per-session).

## Verify Integration

Test API connectivity (after setting KICONNECT_API_KEY):

```bash
curl -s -H "Authorization: Bearer $KICONNECT_API_KEY" \
  "https://chat.kiconnect.nrw/api/v1/models"
```

## Notes

- API key format: `userid:apikey` (single string with colon separator)
- FH Aachen students/staff can get access via chat.kiconnect.nrw
- OpenAI-compatible, works with existing OpenClaw OpenAI client