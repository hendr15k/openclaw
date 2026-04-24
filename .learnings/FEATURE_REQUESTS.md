# Feature Requests

Capabilities users want that don't exist yet.

**Priority Levels**: low | medium | high | critical
**Areas**: frontend | backend | infra | tests | docs | config
**Complexity**: simple | medium | complex

---


## [FEAT-20260421-001] open-reader-voice-persistence

**Logged**: 2026-04-21T10:45:00+02:00
**Priority**: medium
**Status**: pending
**Area**: frontend

### Requested Capability
open-reader: Selected Voice und Speed auch in localStorage persistieren (wie Dark Mode und Reading Progress).

### User Context
Nach Reload wird immer Default-Voice und Speed=1 verwendet. Nutzer müssen每次 neu einstellen.

### Complexity Estimate
simple

### Suggested Implementation
Key: `open-reader-voice` und `open-reader-speed` in localStorage. Initialisierung in useState-Initializer in App.tsx (beim TTS-Setup).

### Metadata
- Frequency: first_time
- Related Features: open-reader dark mode persistence (LRN-20260421-005)


## [FEAT-20260424-001] swipe_navigation

**Logged**: 2026-04-24T12:55:00+02:00
**Priority**: low
**Status**: pending
**Area**: frontend

### Requested Capability
Swipe left/right to navigate between tools on mobile.

### User Context
Users on mobile expect swipe gestures for navigation. Adding swipe support between tool views would make the app feel more native and reduce the need for the tool navigation bar.

### Complexity Estimate
medium

### Suggested Implementation
Use touchstart/touchmove/touchend events to detect horizontal swipes. When swipe threshold is reached, navigate to next/previous tool. Could use a circular list of tools for infinite swiping.

### Metadata
- Frequency: first_time
- Related Features: mobile-tool-nav, bottom-toolbar

---
