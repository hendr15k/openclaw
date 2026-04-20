# Learnings Log

**Priority Levels**: low | medium | high | critical
**Areas**: frontend | backend | infra | tests | docs | config
**Status**: pending | in_progress | resolved | promoted | wont_fix

---

## [LRN-20260326-001] best_practice

**Logged**: 2026-03-26T06:19:00+08:00
**Priority**: medium
**Status**: resolved
**Area**: config

### Summary
Jules API sources endpoint defaults to pageSize=30 — use larger pageSize to find repos in paginated results.

### Details
When checking if `hendr15k/openclaw` was registered with Jules, the first API call with default pagination only returned 30 repos. The target repo appeared to be missing.

Fix: Use `pageSize=100` to get more results in a single call:
```bash
curl -s -H "x-goog-api-key: $JULES_API_KEY" \
  "https://jules.googleapis.com/v1alpha/sources?pageSize=100"
```

The repo was actually registered all along — just not visible in the first page.

### Suggested_action
When searching Jules sources, always use `pageSize=100` or filter directly with the `filter` parameter.

### Metadata
- Source: error
- Related Files: ~/.openclaw/workspace/skills/jules-api/SKILL.md
- Tags: jules, pagination, api, sources

---

## [LRN-20260320-001] config

**Logged**: 2026-03-20T01:22:00+08:00
**Priority**: high
**Status**: resolved
**Area**: config

### Summary
Gateway (systemd service) cannot access environment variables from ~/.bashrc — embed API keys directly in openclaw.json.

### Details
Added `KICONNECT_API_KEY` to ~/.bashrc but gateway restart failed with:
`SecretRefResolutionError: Environment variable "KICONNECT_API_KEY" is missing or empty.`

The OpenClaw gateway runs as a systemd service with its own environment. Variables in ~/.bashrc are NOT available.

Fix: Embed API key directly in openclaw.json instead of using `${KICONNECT_API_KEY}` reference.

### Suggested_action
For provider API keys, prefer embedding directly in openclaw.json. Only use environment variable references for keys that are set system-wide (e.g., in /etc/environment or systemd service override).

### Metadata
- Source: error
- Related Files: ~/.openclaw/openclaw.json
- Tags: gateway, environment, api-keys, systemd

---

## [LRN-20260320-002] best_practice

**Logged**: 2026-03-20T01:17:00+08:00
**Priority**: medium
**Status**: resolved
**Area**: config

### Summary
New OpenRouter models must be added to provider's models array before they can be used as fallbacks.

### Details
User wanted `openrouter/gpt-5.4-nano` as fallback but got:
`Model "openrouter/gpt-5.4-nano" is not allowed.`

The model ID must exist in `models.providers.openrouter.models[]` array for OpenClaw to recognize it.

Fix: Add model definition to provider's models list:
```json
{
  "id": "gpt-5.4-nano",
  "name": "GPT-5.4 Nano",
  "contextWindow": 128000,
  "maxTokens": 4096,
  ...
}
```

### Suggested_action
When adding new model references to fallbacks, first verify the model ID exists in the provider's models array. Use `/models openrouter` to list available models.

### Metadata
- Source: error
- Related Files: ~/.openclaw/openclaw.json
- Tags: model-config, openrouter, fallbacks
- See Also: LRN-20260319-010

---

## [LRN-20260320-003] skill_creation

**Logged**: 2026-03-20T01:25:00+08:00
**Priority**: low
**Status**: resolved
**Area**: docs

### Summary
Created ki-connect skill for FH Aachen NRW AI models.

### Details
- Base URL: `https://chat.kiconnect.nrw/api/v1`
- Available models: `gpt-5.2`, `gpt-5-nano`
- Auth: Bearer token (format: `userid:apikey`)
- OpenAI-compatible API

Skill location: `~/.openclaw/workspace/skills/ki-connect/SKILL.md`

### Suggested_action
Use `kiconnect/gpt-5-nano` or `kiconnect/gpt-5.2` as model references.

### Metadata
- Source: conversation
- Related Files: ~/.openclaw/workspace/skills/ki-connect/SKILL.md
- Tags: skill, ki-connect, fh-aachen, models

---

## [LRN-20260322-001] best_practice

**Logged**: 2026-03-22T10:32:00+08:00
**Priority**: medium
**Status**: promoted
**Area**: config
**Promoted**: MEMORY.md, TOOLS.md

### Summary
Tado OAuth Access-Token läuft nach 10 Minuten ab — Refresh-Token vor API-Call verwenden.

### Details
Tado Access-Token hat `expires_in: 600` (10 Minuten). Der Refresh-Token bleibt gültig und kann verwendet werden, um einen neuen Access-Token zu holen:

```bash
curl -s -X POST "https://login.tado.com/oauth2/token" \
  -d "client_id=1bb50063-6b0c-4d11-bd99-387f4a91cc46" \
  -d "grant_type=refresh_token" \
  -d "refresh_token=$TADO_REFRESH_TOKEN"
```

Die Tokens sind in ~/.bashrc gespeichert, aber da der Gateway nicht auf ~/.bashrc zugreifen kann (siehe LRN-20260320-001), müssen sie bei Bedarf manuell geladen werden.

### Suggested_action
Bei Tado-Abfragen zuerst Token refreshen, dann API-Call durchführen. Für Gateway-Integration sollten Tokens direkt in openclaw.json oder in einer secrets-Datei gespeichert werden.

### Metadata
- Source: conversation
- Related Files: ~/.bashrc, skills/tado-thermostat/SKILL.md
- Tags: tado, oauth, token-refresh, smart-home
- See Also: LRN-20260320-001

---

## [LRN-20260319-001] correction

**Logged**: 2026-03-19T16:20:00+08:00
**Priority**: medium
**Status**: resolved
**Area**: config

### Summary
Model primary/fallback must match exact format: `provider/model-id` not `provider/provider/model-id`.

### Details
User wanted "5.4 nano" via OpenRouter. The correct reference is:
- ✅ `openrouter/gpt-5.4-nano`
- ❌ `openrouter/openrouter/gpt-5.4-nano` (double provider prefix)

### Suggested_action
Always use single provider prefix: `provider/model-id`.

### Metadata
- Source: user_feedback
- Related Files: ~/.openclaw/openclaw.json
- Tags: model-config, naming

---
## [LRN-20260324-001] best_practice

**Logged**: 2026-03-24T00:27:00+08:00
**Priority**: high
**Status**: pending
**Area**: infra

### Summary
Before updating OpenClaw, determine the real install method first; for global npm installs, direct npm update is more reliable than the wrapper when the wrapper stalls.

### Details
This machine uses a global npm install at `/opt/openclaw/npm-global`. The wrapper command `openclaw update` stalled in doctor/package-manager handling, while `npm update -g openclaw` successfully updated the package from `2026.3.13` to `2026.3.22`.

### Suggested Action
For future OpenClaw update incidents:
1. Check install method (`npm list -g --depth=0 | grep openclaw`)
2. If installed globally via npm, use `npm update -g openclaw`
3. Then verify CLI version and restart the gateway service if the running process still reports the old version

### Metadata
- Source: error
- Related Files: /opt/openclaw/npm-global/lib/node_modules/openclaw, TOOLS.md
- Tags: openclaw, update, npm, gateway

---

## [LRN-20260324-002] best_practice

**Logged**: 2026-03-24T00:50:00+08:00
**Priority**: high
**Status**: pending
**Area**: frontend

### Summary
If OpenClaw Web Control fails with `Control UI assets not found`, verify whether `dist/control-ui/index.html` exists inside the installed package before attempting a full rebuild.

### Details
The installed package at `/opt/openclaw/npm-global/lib/node_modules/openclaw` contained control-ui helper JS files but lacked the static bundle directory `dist/control-ui/`. A full `ui:build` from source attempted to pull large workspace dependencies and then failed on a git-hosted dependency, so the fastest successful recovery was: locate an existing prebuilt `dist/control-ui/`, copy it into the installed package, then restart `openclaw-gateway`.

### Suggested Action
Debug order for future incidents:
1. Check `/opt/openclaw/npm-global/lib/node_modules/openclaw/dist/control-ui/index.html`
2. If missing, search local caches/source trees for a prebuilt `dist/control-ui/`
3. Copy assets into the installed package as a recovery workaround
4. Restart `openclaw-gateway`
5. Then verify `/chat` or `open.claw.cloud/setting`

### Metadata
- Source: error
- Related Files: /opt/openclaw/npm-global/lib/node_modules/openclaw/dist/control-ui, /home/openclaw/tmp/openclaw-src/scripts/ui.js
- Tags: openclaw, control-ui, assets, recovery, gateway

---
## [LRN-20260325-001] correction

**Logged**: 2026-03-24T17:33:00Z
**Priority**: high
**Status**: pending
**Area**: docs

### Summary
When hunting FH Aachen Math 1 exams, do not count files from the wrong Fachbereich/professor as valid matches.

### Details
During a Drive-vs-web comparison, I included Uniturm files from FH Aachen Mathe pages that belonged to a different Fachbereich/professor than the target course collection. Hendrik corrected that these are not valid for this task. Future comparisons must verify course ownership/professor context, not just institution name + "Mathe".

### Suggested Action
For FH Aachen exam hunts, require at least one of: matching professor/course page lineage, official host continuity, or explicit evidence that the file belongs to the same target exam series before treating it as a missing item.

### Metadata
- Source: user_feedback
- Tags: correction, fh-aachen, professor-match, source-validation

---
## [LRN-20260325-002] best_practice

**Logged**: 2026-03-24T18:47:00Z
**Priority**: high
**Status**: pending
**Area**: docs

### Summary
When importing archived FH Aachen exam PDFs into Drive, verify byte-identity against existing files before upload and use the exam date read from the PDF itself instead of trusting filenames.

### Details
During a Wayback-based recovery of FH Aachen Math 1 exams, some archived files turned out to be byte-identical to files already present in Drive under different names (`klausur15-1` = `klausur_WS1415`, `klausur16-1` = `klausur_WS1516`, etc.). Uploading first and cleaning up later created avoidable duplicate noise. Also, Hendrik explicitly wanted the real exam date read from the PDF because filenames can be misleading.

### Suggested Action
Before uploading recovered exam files:
1. Download candidate PDF
2. Extract date from PDF text/content when possible
3. Compare hash against existing Drive files in likely matching folders
4. Upload only if not byte-identical to an existing file
5. If provenance matters, store source info separately instead of duplicating the PDF

### Metadata
- Source: conversation
- Tags: best-practice, fh-aachen, drive, deduplication, pdf-date, wayback
- See Also: LRN-20260325-001

---

## [LRN-20260326-001] correction

**Logged**: 2026-03-26T05:38:00+08:00
**Priority**: medium
**Status**: promoted
**Area**: tool_usage
**Promoted**: TOOLS.md

### Summary
Parameter `streamTo: "parent"` in `sessions_spawn` is only supported for `runtime: "acp"`, not for `runtime: "subagent"`.

### Details
Der User wollte einen Subagent für die Android APK-Kompilierung spawnen. Ich habe wiederholt `sessions_spawn` mit `streamTo: "parent"` aufgerufen, aber jeder Versuch schlug fehl mit:

```
error: streamTo is only supported for runtime=acp; got runtime=subagent
```

Ich habe den Fehler nicht sofort erkannt und weiter versucht, streamTo zu verwenden, bis der User mich mehrfach korrigiert hat ("Fixe es", "Ein subagent soll es machen!!!").

Die Lösung war einfach: `streamTo: "parent"` aus dem Tool-Call entfernen. Dann hat `sessions_spawn` mit `runtime: "subagent"` funktioniert.

### Suggested_action
Beim Aufruf von `sessions_spawn`:
- Wenn `runtime: "subagent"`: **niemals** `streamTo` verwenden
- Wenn `runtime: "acp"`: dann `streamTo: "parent"` verwenden
- Das Tool-Schema zeigt `streamTo` als optional, aber die Validierung erzwingt diese Regel

### Metadata
- Source: user_feedback
- Related Files: ~/.openclaw/openclaw.json, sessions_spawn tool definition
- Tags: sessions_spawn, streamTo, subagent, acp, tool-error

---

## [LRN-20260326-002] best_practice

**Logged**: 2026-03-26T06:05:00+08:00
**Priority**: high
**Status**: pending
**Area**: tool_usage

### Summary
Jules CLI requires repos to be registered as Sources in the Jules web UI before use. REST API needs OAuth, not just API key. Sources cannot be added via CLI/API.

### Details
Der User wollte Jules für die APK-Kompilierung nutzen. Versuche schlugen fehl:

1. **REST API**: `curl` mit `x-goog-api-key` Header gab 401 UNAUTHENTICATED
   - "Expected OAuth 2 access token" — API Key allein reicht nicht
   
2. **Jules CLI**: `jules task "..."` gab RuntimeError
   - "No source matched repo 'hendr15k/spritpreise'"
   - Config hat `default_repo = "hendr15k/spritpreise"`, aber das Repo ist nicht als Source registriert
   - Available sources zeigt 30+ Repos, aber openclaw/openclaw nicht dabei

3. **Sources hinzufügen**: Geht NUR über jules.google.com Web-UI
   - CLI command `jules workspace add-source` existiert nicht
   - REST API ist read-only für Sources

**Lösung**: Repos müssen vorher auf jules.google.com verbunden werden.

### Suggested_action
Bevor Jules genutzt werden kann:
1. Geh zu https://jules.google.com
2. Verbinde das gewünschte GitHub Repo als "Source"
3. Dann funktioniert `jules task` und REST API mit OAuth

### Metadata
- Source: error
- Related Files: ~/.config/jules/config.toml, skills/jules-api/SKILL.md
- Tags: jules, api, oauth, sources, cli-limitation
- See Also: LRN-20260326-001

---
## [LRN-20260326-003] correction

**Logged**: 2026-03-26T07:50:00+08:00
**Priority**: high
**Status**: promoted
**Area**: config
**Promoted**: MEMORY.md

### Summary
Android App Cache löschen reicht NICHT um alte Bootstrap Token zu entfernen — App muss komplett deinstalliert werden.

### Details
User hatte `bootstrap_token_invalid` Fehler auf Android (Xiaomi 13T Pro). Diagnose:
1. Gateway restart leert `bootstrap.json` (Token verloren)
2. Neuer QR generiert mit `openclaw qr --json`
3. App gescannt → **aber App nutzte immer noch alten ge-cacheten Token!**
4. App-Cache löschen brachte nichts
5. App-Komplett-Deinstallation nötig um alten Token zu entfernen

Dies ist ein wiederkehrendes Problem. MEMORY.md (2026-03-18/19) dokumentiert bereits dass Gateway restart `bootstrap.json` leert, aber nicht dass App Cache-Löschen unzureichend ist.

### Suggested_action
Bei `bootstrap_token_invalid` auf Android:
1. App KOMPLETT deinstallieren (nicht nur Cache!)
2. APK neu installieren
3. Frischen QR scannen (`openclaw qr --json`)
4. Gateway NICHT neu starten währenddessen

### Metadata
- Source: error
- Related Files: ~/.openclaw/devices/bootstrap.json, MEMORY.md
- Tags: android, bootstrap-token, device-pair, pairing, app-cache
- See Also: LRN-20260319-007 (Gateway restart clears bootstrap.json)
- Pattern-Key: harden.bootstrap_token_reset
- Recurrence-Count: 2
- First-Seen: 2026-03-18
- Last-Seen: 2026-03-26

---
## [LRN-20260326-004] correction

**Logged**: 2026-03-26T08:05:00+08:00
**Priority**: medium
**Status**: promoted
**Area**: communication
**Promoted**: MEMORY.md

### Summary
Bei Terminplanung mit relativen Zeitangaben ("morgen", "heute") IMMER den aktuellen Zeitstempel explizit mit dem User abgleichen.

### Details
User schrieb "Will morgen um 8 in der FH sein muss aber später noch zum Zahnarzt". Ich interpretierte "morgen" als Freitag 27.03. und "später" als zweiten Zahnarzttermin.

Korrektur durch User: "Mit morgen meinte ich heute" — er meinte HEUTE (26.03.) und der Zahnarzttermin war bereits 16:00 HEUTE im Kalender.

**Root Cause:** Relative Zeitangaben ohne explizites Datum sind mehrdeutig. Ich hätte direkt fragen sollen: "Meinst du morgen (Freitag 27.03.) oder heute (Donnerstag 26.03.)?"

### Suggested_action
Bei relativen Zeitangaben:
1. Immer aktuelles Datum/Tag explizit nennen
2. Bei Unsicherheit direkt nachfragen mit konkretem Datum
3. Kalender zuerst prüfen bevor Annahmen treffen

### Metadata
- Source: user_feedback
- Tags: communication, terminology, date-ambiguity, planning
- See Also: LRN-20260326-001 (correction pattern)

---
## [LRN-20260326-005] best_practice

**Logged**: 2026-03-26T08:27:00+08:00
**Priority**: high
**Status**: promoted
**Area**: config
**Promoted**: MEMORY.md

### Summary
Ontology als zusätzlichen Speicher für ALLE Erinnerungen nutzen — nicht nur memory/YYYY-MM-DD.md.

### Details
User forderte explizit: "Nutze auch absolut immer ontology als zusätzlichen Speicher wo alle Erinnerungen gelesen werden und geschrieben werden (alle)"

**Workflow:**
1. **Schreiben:** Jede neue Erinnerung → memory/YYYY-MM-DD.md + ontology Entity
2. **Lesen:** Bei Erinnerungs-Abfragen → memory_search + ontology query
3. **Verknüpfungen:** Relations zwischen Entities (Event → Task, Task → Person)

**Ontology Entity Types für Erinnerungen:**
- Event (Termine, Zeitplan)
- Task (Todoist Tasks)
- Note (Präferenzen, Beobachtungen)
- Person (Kontakte)
- Document (Referenzen)

**Storage:** `memory/ontology/graph.jsonl`
**CLI:** `python3 skills/ontology/scripts/ontology.py`

### Suggested_action
Bei allen Erinnerungs-Operationen:
1. memory/YYYY-MM-DD.md aktualisieren
2. Ontology Entity erstellen
3. Relations zwischen verwandten Entities setzen
4. Bei Abfragen: beide Quellen konsultieren

### Metadata
- Source: user_feedback
- Related Files: memory/ontology/graph.jsonl, skills/ontology/SKILL.md
- Tags: ontology, memory, storage, workflow
- See Also: LRN-20260326-004 (proactive planning)

---

---

## [LRN-20260327-001] bug_workaround

**Logged**: 2026-03-27T00:43:00+08:00
**Priority**: high
**Status**: promoted
**Area**: infra

### Summary
OpenClaw Android pairing fails with `bootstrap_token_invalid` because bootstrap tokens are single-use but apps open 2 sockets simultaneously — use shared token instead.

### Details
**GitHub Issue:** [#47887](https://github.com/openclaw/openclaw/issues/47887) (OPEN)

The Android app opens TWO WebSocket connections simultaneously:
1. Node role (device capabilities)
2. Operator role (chat/messaging)

Bootstrap tokens are SINGLE-USE — first socket consumes it, second gets rejected.

**Symptoms:**
- `bootstrap_token_invalid` error despite fresh QR scan
- No pending device in `openclaw devices list`
- Multiple pairing attempts all fail

**Workaround:**
Use the shared gateway token instead of bootstrap token:

```json
{
  "url": "ws://8.209.235.235:18789",
  "token": "<shared-gateway-token>"
}
```

Setup code (base64):
```bash
echo -n '{"url":"ws://8.209.235.235:18789","token":"<token>"}' | base64 -w0
```

### Suggested Action
When pairing Android devices:
1. Check if `gateway.auth.token` is set in openclaw.json
2. Generate setup code with shared token, not bootstrap token
3. Use manual entry in app: host, port, shared token

### Metadata
- Source: error
- Related Files: ~/.openclaw/openclaw.json, src/infra/device-bootstrap.ts
- Tags: openclaw, android, pairing, bootstrap, gateway, bug_workaround
- Pattern-Key: harden.bootstrap_token_single_use
- GitHub Issue: openclaw/openclaw#47887

---

### Resolution
- **Resolved**: 2026-03-27T00:45:00+08:00
- **Promoted**: TOOLS.md
- **Notes**: Added "OpenClaw Android Pairing (Bug #47887 Workaround)" section with setup code generation instructions.

## [LRN-20260420-001] Google Drive File Move API

**Logged**: 2026-04-20T21:30:00+02:00
**Priority**: medium
**Status**: resolved
**Area**: infra

### Summary
Google Drive API `PATCH /files/{id}?addParents=FOLDER_ID` für Datei-Verschieben ohne removeParents funktioniert (Dateien behalten alte Parent-Verzeichnisse). Für echtes Verschieben: `removeParents=oldParent` zusätzlich angeben.

### Details
Beim Verschieben von 11 lose liegenden Dateien im Drive-Root in Zielordner: PATCH ohne removeParents führt dazu dass Dateien in NEUEM Ordner landen ABER noch im Root erscheinen (doppelte Sichtbarkeit). Lösung: `addParents=NEU` + `removeParents=root` oder erst alle root-parent-Einträge entfernen.

### Suggested Action
Bei Drive-Verschieben IMMER beide Parameter nutzen: `addParents=NEU&removeParents=OLD` — oder Dateien haben danach mehrfache Parent-Referenzen.

### Metadata
- Source: own experimentation
- Related Files: TOOLS.md (Google Drive section)
- Tags: google-drive, api, maton

---
