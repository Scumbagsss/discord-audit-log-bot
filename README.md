# Discord Audit Log Bot

> **Portfolio showcase — production source is private and this repository is intentionally non-runnable.**

Advanced Discord moderation logger for messages, voice, members, bans, roles and nickname changes.

## What it demonstrates

- Message delete/edit logs
- Voice-state logs
- Member join/leave logs
- Kick/ban/unban attribution
- Role and nickname change logs
- Channel/category/role exclusions

## Technology

Python • discord.py • Discord Audit Log API • Async listeners

## High-level workflow

1. Receive Discord event
2. Apply exclusions
3. Resolve responsible actor when possible
4. Format audit record
5. Send to configured log channel

## Public interface preview

The public skeleton exposes only the architectural surface:

- `handle_message_event(...)`
- `handle_voice_event(...)`
- `resolve_audit_actor(...)`
- `emit_audit_record(...)`

The production implementations behind these methods are withheld. See [`NOTICE.md`](NOTICE.md).

## Repository contents

- `src/public_interface.py` — non-runnable interface skeleton;
- `docs/ARCHITECTURE.md` — high-level design;
- `examples/config.example.jsonc` — sanitized configuration shape;
- `LICENSE` — explicit all-rights-reserved notice.

## Status

Production-tested private project / portfolio edition.
