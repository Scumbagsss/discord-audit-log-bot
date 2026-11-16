# Discord Audit Log Pipeline — architecture notes

> This is a **suggested technical boundary for a private-source module**, not a claim that all components are implemented or active in a particular deployment.

## Objective

Discord can emit overlapping events for message changes, voice transitions, member changes and moderation actions. A useful audit pipeline must normalize different event shapes, attribute an actor only when supported and avoid flooding staff with misleading records.

## Conceptual responsibilities

**1. Discord event.** Receive a Discord event from a configured listener.

**2. Exclusion filter.** Apply channel, category and role exclusions.

**3. Normalize record.** Attach event time, subject and the best available attribution context.

**4. Resolve attribution.** Format a concise staff record without inventing an actor.

**5. Staff audit sink.** Deliver to an authorized destination and record delivery failures.

## Review risks and recommended tests

| Concern | Failure mode | Verification to add |
|---|---|---|
| Actor attribution | Audit events may not provide a reliable responsible user | Test missing, delayed and ambiguous actor resolution |
| Privacy and scope | Edited messages and member activity can contain personal data | Enforce channel exclusions and retention policy |
| Delivery failure | Target log channel may be removed or lack permissions | Define failure reporting and retry limits |
| Event volume | Bursts can trigger API rate limits and noisy alerts | Batch or rate-limit safely without losing ordering |

## Integration and permissions

The Discord interaction layer should treat its inputs as untrusted. A server-side handler must establish the principal, check authorization for the concrete operation and return user-safe errors. The persistence or external API adapter is separately responsible for safe updates, retries and recovery. The public `src/public_interface.py` is only a surface sketch; **none of these safeguards can be confirmed by running it**.

## Production/public boundary

No real member IDs, credentials, channel IDs, private schemas, moderation rules or live logs should appear in this repository. The architectural context belongs to the wider [DeadCity platform case study](https://github.com/Scumbagsss/BOT). For a separately developed runnable example, see the [ticket workflow backend](https://github.com/Scumbagsss/advanced-discord-ticket-bot).
