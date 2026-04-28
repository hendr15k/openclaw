# HEARTBEAT.md — Periodic Self-Improvement Checklist

**Letzter Check:** 2026-04-27T23:15:00+02:00

---

## Status

**Aktuelle Zeit:** Mo 27.04.2026 23:15 Berlin / 21:15 UTC

### ✅ Erledigt (2026-04-27 — Drive Sort Night, Nachtsession)
- ✅ Google Drive komplett aufgeräumt (außer FH AACHEN)
- ✅ Root: 25 lose PDFs/Sheets → Ordner verschoben (Copy+Delete workaround für Maton PATCH-bug)
- ✅ 03_Forschung: 3 Duplicate PDFs gelöscht (je größte Version behalten)
- ✅ 02_Technik: 4 leere OPLMonitor APKs gelöscht, PRISM + agent-browser-screenshots gelöscht
- ✅ 04_Persoenliches: 2 Google Docs "Der moralische Virologe" gelöscht, 1 unbennantes Dok umbenannt, Therapie + Bindung gelöscht
- ✅ 05_Downloads: 4 Backup-Ordner → OS_Images_und_VMs zusammengelegt (82 Files)
  - Alte_Archive (40), Backups_und_Dubletten (14), Images_und_Backups (6), ISO_Downloads (9) → gelöscht
- ✅ 06_Literatur: APK nach Technik/Android_Tools verschoben, "Die Erben" umbenannt, leerer Sci-Fi Ordner gelöscht
- ✅ bookish-waffle: `odestats(sol)` implementiert — `e459cd3` gepusht
- ✅ Humidity daemon re-enabled (PID 42089) — 03:04 active

### ✅ Erledigt (2026-04-26 — Translation Marathon!)
- ✅ "The Inheritors" komplett übersetzt — 19 Kapitel, ~64.469 Wörter
- ✅ Hendrik-Sci-Fi: 9 neue Titel (Hugo/Goodreads/Nebula/Clarke Award) → CSV jetzt 164 Einträge
- ✅ bookish-waffle: Bogacki-Shampine 4(5) Solver (`bs45`) implementiert — `9e7a01c` gepusht

### ⚠️ Hendrik-Sci-Fi: Empfehlungen-Sichtbarkeit unklar
- Site funktioniert technisch: CSV lädt, Recommender läuft
- Wahrscheinlich Browser-Cache — Hendrik soll Ctrl+Shift+R oder Cache leeren

### ⚠️ Beobachtet / Unklar
- ⚠️ Workspace: ~2.8 GB potentiell aufräumbar (decompile/ etc.)
- ⚠️ OPL Monitor — wartet auf Hendrik Feedback
- ⚠️ Spritpreise Demo-Modus aktiv (API-Key noch tot)

### 🔜 Nächste Schritte
1. Hendrik-Sci-Fi: Mehr neue Titel + Empfehlungsfinder testen
2. OPL Monitor Feedback einholen
3. Workspace Cleanup (~2.8 GB) — Hendriks Freigabe benötigt
4. bookish-waffle: weitere Solver oder Features

## Learnings (2026-04-22 bis 2026-04-27)
- LRN-20260422-001: Parallele Subagents auf gleiche Files = nur letzter Commit gewinnt
- LRN-20260422-002: GitHub Pages+Vite: lokaler dist/ ist irrelevant
- LRN-20260422-003: Subagent "completed" ohne Token-Output = File-Dump statt Arbeit
- LRN-20260424-001: Curly-Apostrophe in JS-Strings = SyntaxError
- LRN-20260424-002: Inline-JS mit Nicht-ASCII kann Node.js --check brechen
- LRN-20260424-003: `streamTo: parent` ist INVALID für `runtime=subagent`
- LRN-20260425-001: Subagent-Passwort-Interaktionen können Output unterbrechen
- LRN-20260426-001: Subagent-Parallelspawn für einzelne Kapitel = bessere Übersetzungsqualität
- LRN-20260426-002: Conrad/Ford "The Inheritors" Kapitel 5-7 sehr unterschiedliche Textlängen
- LRN-20260426-003: chapter-14 Subagent bekam falschen Text → IMMER Kapiteltext VOR Spawn lesen
- LRN-20260426-004: "The Inheritors" komplett übersetzt in ~11 Stunden
- LRN-20260426-005: IMMER kurze timeouts. exec: 30s, spawn: 60s. Länger -> background + polling
- LRN-20260427-001: Maton PATCH addParents/removeParents wird ignoriert → Copy+Delete Workaround
- LRN-20260427-002: Nested subfolders in Google Drive: Files einzeln kopieren, nicht Ordner
- LRN-20260427-003: Subagent commit lokal → IMMER danach `git push origin main`

## Security
- [x] Config-File Rechte 600
- [x] Gemini API Keys entfernt
- [x] Sonstiges sauber

## Memory
- [x] memory/2026-04-26.md aktuell
- [x] memory/2026-04-26-drive-sort.md aktuell
- [x] HEARTBEAT.md bereinigt und aktualisiert

---

*HEARTBEAT.md aktualisiert 2026-04-27T00:50*
