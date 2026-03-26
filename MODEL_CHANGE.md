# Model Configuration Change

**Status:** Pending restart
**Date:** 2026-03-15

---

## Configuration Updated

**New Primary Model:** `openrouter/step-3.5-flash:free`

**Added Provider:**
- **OpenRouter** with API key configured
- **Model:** step-3.5-flash:free

**Available Models:**
- `occ/glm-4.7` (old default)
- `occ/glm-5` (fallback)
- `occ/claude-sonnet-4-6` (reasoning)
- **`openrouter/step-3.5-flash:free`** (new primary)

---

## Action Required

**Gateway needs restart:**

```bash
sudo systemctl restart openclaw-gateway
```

**Or via systemd:**

```bash
sudo systemctl restart openclaw-gateway.service
```

---

## Notes

- Configuration file: `/home/openclaw/.openclaw/openclaw.json`
- Primary model changed from `occ/glm-4.7` to `openrouter/step-3.5-flash:free`
- OpenRouter provider added with API key
- Gateway restart required to apply changes
