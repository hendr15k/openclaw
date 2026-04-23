# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## OpenClaw Gateway

The openclaw gateway runs as a systemd service on this machine. Do NOT use `openclaw gateway restart`.

To restart the gateway:

```bash
sudo systemctl restart openclaw-gateway
```

To check gateway status:

```bash
sudo systemctl status openclaw-gateway
```

## ClawHub

**Account:** @hendr15k (eingeloggt)

**Rate Limits:** Anonyme Requests werden stark gedrosselt. IMMER prüfen ob eingeloggt:
```bash
clawhub whoami  # Sollte @hendr15k zeigen
```

**Slug-Format:** Nur Skill-Name, NICHT owner/repo:
```
clawhub.ai/JimLiuxinghai/find-skills → clawhub install find-skills
```

Falls Rate Limit trotz Login: **60s warten** (nicht 30s), dann retry. Git Clone als letzter Fallback:
```bash
git clone https://github.com/username/skill-repo.git ~/.openclaw/workspace/skills/skill-name
```

## Maton API Gateway

**Status:** Active (key in ~/.bashrc as MATON_API_KEY)
**Gateway URL:** `https://gateway.maton.ai/{app}/{endpoint}`
**Control URL:** `https://ctrl.maton.ai/connections`
**Installed:** 2026-03-15

**Aktive Verbindungen (Live-Check 2026-03-16):**
- google-sheets (hendrik.schmitz03.sh@gmail.com) — CREATE/READ/WRITE
- google-mail (hendrik.schmitz03.sh@gmail.com)
- google-drive (hendrik.schmitz03.sh@gmail.com)
- google-docs (hendrik.schmitz03.sh@gmail.com)
- google-calendar (hendrik.schmitz03.sh@gmail.com)
- google-slides (hendrik.schmitz03.sh@gmail.com)
- google-tasks (hendrik.schmitz03.sh@gmail.com)
- google-forms
- github
- notion
- youtube
- brave-search

**Erstellte Sheets:**
- Sci-Fi Bibliothek: `1jb6MYwQ4urDWEVF5rbHvbwHC9rXgiRV0vlxTZrd-tIY`
- Sci-Fi Buchempfehlungen: `1beec_lWXD6kqMURED4V1OuSVfE3lgh1uPcXB7GgLbSo`
- US-Iran Konflikt Analyse: `1LE6T8wv57IlJ1tM4eYxcAVNj3RdELWvUvbeigemF8b0`
- Pharmakologie: `1IVWuTs9uR7JOVfFHkRomrLx4FPzUm5B6qwF-jB-t5nE`

**Erstellte Docs:**
- Promethazin Rezeptorprofil: `1eMfRruupzevBJd8J76oF4sHAA1PeFCPGzACO44de1kA`

**Auth-Pattern:**
```python
import urllib.request, os, json
req = urllib.request.Request('https://gateway.maton.ai/google-sheets/v4/...')
req.add_header('Authorization', f'Bearer {os.environ["MATON_API_KEY"]}')
req.add_header('Content-Type', 'application/json')
```

## Netlify Deployments (via Maton)

**Base URL:** `https://gateway.maton.ai/netlify/api/v1`
**Auth-Pattern:**
```python
req = urllib.request.Request('https://gateway.maton.ai/netlify/api/v1/sites/{site_id}/deploys', data=zip_bytes, method='POST')
req.add_header('Authorization', f'Bearer {os.environ["MATON_API_KEY"]}')
req.add_header('Content-Type', 'application/zip')
```

**Sites:**
- **hendrik-sci-fi-books** — Sci-Fi-Bibliothek mit Leseplan, Filter, Export
  - Site ID: `fa810fd6-ae1b-4c86-ab9a-30a5dae87df1`
  - URL: `https://hendrik-sci-fi-books.netlify.app`
  - Deploy-Pattern: ZIP mit `index.html` + `_headers`
  - Functions: `netlify/functions/sync-todoist/` (TypeScript, Todoist-Sync)
- **hendrik-spritpreise** — Spritpreisprognose Deutschland
  - Site ID: `a904ef00-c75d-4dbe-8c5b-8aaa9632e349`
  - URL: `https://hendrik-spritpreise.netlify.app`
  - Deploy-Pattern: ZIP mit `index.html` + `_headers`

## Web Scraping: JavaScript-Rendered Pages

Standard `curl` often fetches only skeleton HTML from JS-heavy sites (e.g., Shopify). Use Jina AI Reader API for reliable text extraction:

```bash
# General pattern
curl -s "https://r.jina.ai/http://example.com/page" > output.txt

# Example: happy-420.de product
curl -s "https://r.jina.ai/http://happy-420.de/products/super-pollen-thcp" | grep -i "cannabinoide"
```

This returns clean markdown with all rendered content. Alternative: use `web_fetch` tool if available. Reserve `browser` tool for cases requiring actual JS execution or interaction.

## Brave Search (web_search tool)

**Status:** ❌ Missing BRAVE_API_KEY
**Error:** `web_search failed: missing_brave_api_key`
**Setup:** `openclaw configure --section web` oder `BRAVE_API_KEY` in Gateway Environment

**Workaround:** Startpage via Jina AI Reader für Web-Suche nutzen:
```bash
curl -s "https://r.jina.ai/https://www.startpage.com/do/dsearch?query=SEARCH+TERMS"
```
Oder `web_fetch` tool mit DuckDuckGo HTML (erste Suche vor CAPTCHA).

## QMD Memory Backend

**Status:** Enabled (`memory.backend: "qmd"`)
**Installed:** 2026-03-15

**Binary:** `/usr/local/bin/qmd` (symlink → wrapper → bun run TypeScript)
**Bun:** `/usr/local/bin/bun` (symlink → `~/.bun/bin/bun`)
**Models:** Auto-downloaded on first `memory_search` (~1-2 GB, CPU-only)

**Quick checks:**
```bash
qmd status          # index health
qmd status --json   # machine-readable
```

**Notes:**
- Falls back to builtin SQLite if QMD fails
- First search may be slow (model download)
- CPU-only by default (1 core, no GPU)
- Models: embeddinggemma-300M + Qwen3-Reranker-0.6B + query-expansion-1.7B

## GitHub CLI (gh)

**Installed:** `/home/linuxbrew/.linuxbrew/bin/gh`
**Account:** hendr15k (Hendrik Schmitz)
**Auth:** `echo TOKEN | gh auth login --with-token` (silent = success)
**Verify:** `gh api user --jq .login` → hendr15k
**Scopes:** Full (repo, user, workflow, admin:*, etc.)

**⚠️ Maton GitHub API does NOT work** — all `/github/v3/` endpoints return 404. Use `gh` CLI directly.

**GitHub Pages API — JSON Format (NOT string):**
```bash
# ❌ WRONG: -f source=main → 422 error
# ✅ RIGHT:
gh api -X POST repos/OWNER/REPO/pages --input - <<'EOF'
{"source":{"branch":"main","path":"/"}}
EOF
```

**Pages URL Pattern:** `https://USERNAME.github.io/REPO_NAME/`

## Netlify Deploy via API (No zip command!)

`zip` is NOT installed. Use Python:
```python
import zipfile
with zipfile.ZipFile('deploy.zip', 'w', zipfile.ZIP_DEFLATED) as z:
    z.write('index.html', 'index.html')
    z.write('_headers', '_headers')
```

**Always include `_headers`** with `Content-Type: text/html; charset=UTF-8` to prevent raw source display.

## agent-browser (Headless Browser Automation)

**Version:** 0.20.10
**Binary:** `/opt/openclaw/npm-global/bin/agent-browser`
**Chrome:** `/home/openclaw/.agent-browser/browsers/chrome-146.0.7680.80`
**Add to PATH:** `export PATH="/opt/openclaw/npm-global/bin:$PATH"` (already in ~/.bashrc)

**Quick test:**
```bash
/opt/openclaw/npm-global/bin/agent-browser --version
/opt/openclaw/npm-global/bin/agent-browser open https://example.com
/opt/openclaw/npm-global/bin/agent-browser snapshot -i --json
```

**Notes:**
- Skill: `agent-browser-clawdbot` für Kommando-Referenz
- Immer `-i --json` für Snapshots nutzen
- Sessions für isolierte Browser-Kontexte
- State save/load für Auth-Persistenz

---

Add whatever helps you do your job. This is your cheat sheet.

## Google Drive (via Maton)

**Wichtig:** Benannte Root-Ordner nicht ungefragt verschieben. Speziell `FH AACHEN` im Drive-Root in Ruhe lassen, außer Hendrik sagt explizit, dass er umsortiert werden soll.

**Endpoint Pattern:** `https://gateway.maton.ai/google-drive/drive/v3/{rest-of-path}`
**Note:** Requires `drive/v3/` prefix after app name (native Google Drive API path)

**List files in folder:**
```bash
curl -s -H "Authorization: Bearer $MATON_API_KEY" \
  "https://gateway.maton.ai/google-drive/drive/v3/files?q='FOLDER_ID'+in+parents&fields=files(id,name,mimeType,size)"
```

**Download file:**
```bash
curl -s -H "Authorization: Bearer $MATON_API_KEY" \
  "https://gateway.maton.ai/google-drive/drive/v3/files/{FILE_ID}?alt=media" -o output.pdf
```

**Known folders:**
- Export (Eventuell unvollständig): `1sVCjmblECiVxWgo9VjjJFqAEpj_obuxR`

## Dekompilierte Android-APKs

**Hardcoded Resource-IDs sind nach Rebuild instabil.**
JADX belässt originale Resource-IDs als Literalzahlen (z.B. `2130837661`). Nach Gradle-Rebuild mappen diese auf andere Resources → `Resources$NotFoundException`.
**Fix:** IMMER nach `2130xxxxxx` / `0x7f0x...` suchen und durch `R.xxx.yyy` Referenzen ersetzen. Scanner: `tools/hardcoded-id-scanner.sh`

**`<include android:id=...>` überschreibt die Root-ID des included Layouts.**
`findViewById(R.id.toolbar)` returned null wenn das `<include>`-Tag eine eigene `android:id` hat (z.B. `@id/include`).
**Fix:** Fallback auf Include-ID: `findViewById(R.id.include) != null ? findViewById(R.id.include) : findViewById(R.id.toolbar)`

## Nebo — PDF vs. Backup

**PDF-Export (bevorzugen):** Enthält erkannten Text via `page.get_text()` (PyMuPDF). Quelle: Google Drive Export-Ordner oder manueller Export.

**Backup (.nebobackup):** Enthält nur PNG-Rasterbilder der Notizen (keine Textschicht). Gut für Struktur (Ordner, Titel, Datum), schlecht für Inhalt.

**Workflow für Notizen-Analyse:**
1. Backup analysieren → Struktur (Ordner, Dokumente, Datum)
2. PDF-Exporte lesen → Inhalte (erkannte Handschrift)
3. Kombinieren → Vollständige Übersicht


## Todoist (via Maton)

**Endpoint:** `https://gateway.maton.ai/todoist/api/v1/...`
**Note:** Todoist API v1 (not v2!) via Maton

**List tasks:**
```bash
curl -s -H "Authorization: Bearer $MATON_API_KEY" \
  "https://gateway.maton.ai/todoist/api/v1/tasks" | jq '.results[] | {content, due: .due.date, id}'
```

**Create task:**
```bash
curl -s -X POST -H "Authorization: Bearer $MATON_API_KEY" \
  -H "Content-Type: application/json" \
  "https://gateway.maton.ai/todoist/api/v1/tasks" \
  -d '{"content":"Task name","due_string":"tomorrow 10am"}'
```

**Complete task:**
```bash
curl -s -X POST -H "Authorization: Bearer $MATON_API_KEY" \
  "https://gateway.maton.ai/todoist/api/v1/tasks/{TASK_ID}/close"
```

## Tado Thermostat

**OAuth Token Refresh Required:** Access-Token läuft nach 10 Minuten ab. Vor API-Call Refresh-Token verwenden:
```bash
curl -s -X POST "https://login.tado.com/oauth2/token" \
  -d "client_id=1bb50063-6b0c-4d11-bd99-387f4a91cc46" \
  -d "grant_type=refresh_token" \
  -d "refresh_token=$TADO_REFRESH_TOKEN"
```
Tokens in ~/.bashrc gespeichert.

---

## Google Calendar (via Maton)

**Endpoint:** `https://gateway.maton.ai/google-calendar/calendar/v3/...`

**Create event:**
```bash
curl -s -H "Authorization: Bearer $MATON_API_KEY" \
  "https://gateway.maton.ai/google-calendar/calendar/v3/calendars/primary/events" -X POST \
  -H "Content-Type: application/json" \
  -d '{"summary":"...","start":{"dateTime":"2026-06-30T15:45:00+02:00","timeZone":"Europe/Berlin"},"end":{"dateTime":"2026-06-30T16:45:00+02:00","timeZone":"Europe/Berlin"}}'
```

**Note:** Date format: `YYYY-MM-DDTHH:MM:SS+02:00` (summer) or `+01:00` (winter), timezone `Europe/Berlin`

## OpenClaw Android Pairing (Bug #47887 Workaround)

**GitHub Issue:** [#47887](https://github.com/openclaw/openclaw/issues/47887) (OPEN)

**Problem:** Bootstrap tokens are single-use, but Android app opens 2 sockets (node + operator) simultaneously → second gets `bootstrap_token_invalid`.

**Workaround:** Use shared gateway token instead of bootstrap token.

**Generate setup code:**
```bash
# Get shared token from config
SHARED_TOKEN=$(cat ~/.openclaw/openclaw.json | jq -r '.gateway.auth.token')

# Create setup code with shared token
echo -n "{\"url\":\"ws://8.209.235.235:18789\",\"token\":\"$SHARED_TOKEN\"}" | base64 -w0
```

**Manual entry in app:**
- Host: `8.209.235.235`
- Port: `18789`
- Token: (from `~/.openclaw/openclaw.json` → `gateway.auth.token`)

---

## sessions_spawn (Subagent Tool)

**⚠️ streamTo Parameter Restriction:**
- `streamTo: "parent"` is ONLY valid for `runtime: "acp"`
- For `runtime: "subagent"` → do NOT use `streamTo` at all
- Tool schema shows `streamTo` as optional, but validation enforces this rule

**Example (correct):**
```json
// subagent runtime — NO streamTo
{"runtime": "subagent", "task": "...", "mode": "run"}

// acp runtime — streamTo allowed
{"runtime": "acp", "agentId": "...", "task": "...", "streamTo": "parent"}
```

## Skill-Script-Pfade

Skill-Scripts liegen IMMER in `skills/NAME/scripts/`, **nicht** in `workspace/scripts/`.
Beispiel: `~/.openclaw/workspace/skills/humidity-hysteresis-control/scripts/humidity_hysteresis_control.py`

Immer vollen Pfad vom Skill-Verzeichnis nutzen.

## Google Home Control

**Script:** `~/.openclaw/workspace/skills/google-home-control/scripts/control.py`
**WICHTIG:** MUSS mit der venv-Python gestartet werden — System-Python fehlen die Dependencies!

```bash
~/.openclaw/workspace/skills/google-home-control/google_home_env/bin/python \
  ~/.openclaw/workspace/skills/google-home-control/scripts/control.py "Turn off the lights"
```

Antwort kommt als Text in stdout. Keine Ausgabe = Befehl ausgeführt (stiller Erfolg).
