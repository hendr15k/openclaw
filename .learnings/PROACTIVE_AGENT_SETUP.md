# Proactive Agent 🦞

**Installiert:** 2026-03-14
**Autor:** halthelobster (Hal Labs)
**Version:** 3.0.0
**Status:** Aktiv

---

## Was dieser Skill macht

Transformiert KI-Agenten von Task-Followern in proaktive Partner:

**Proaktiv** — Schafft Wert ohne gefragt zu werden
- Antizipiert Bedürfnisse
- Surface-Ideen, die du nicht wusstest zu fragen
- Proaktive Check-ins bei wichtigen Dingen

**Persistent** — Überlebt Context-Loss
- WAL Protocol — Schreibt kritische Details VOR Antworten
- Working Buffer — Capturt jede Exchange
- Compaction Recovery — Recovery nach Context-Loss

**Self-improving** — Wird besser
- Self-healing
- Relentless resourcefulness (10 Ansätze bevor aufgeben)
- Safe evolution mit Guardrails

## Dateien im Workspace

Folgende Dateien werden vom Skill erwartet:
- ONBOARDING.md — First-run Setup
- SESSION-STATE.md — Aktives Working Memory (WAL Target)
- HEARTBEAT.md — Periodische Self-Improvement Checklist
- memory/working-buffer.md — Danger Zone Log

## Schlüssel-Protokolle

**WAL Protocol:** Schreib kritische Details (Korrekturen, Namen, Entscheidungen) nach SESSION-STATE.md VOR Antworten.

**Working Buffer:** Capturt jede Exchange nach 60% Context-Zuweisung für Recovery nach Compaction.

**Compaction Recovery:** Review buffer nach Compaction, extrahiere wichtigsten Context.

---

**Installation:**
```bash
git clone https://github.com/halthelobster/proactive-agent.git ~/.openclaw/workspace/skills/proactive-agent
```
