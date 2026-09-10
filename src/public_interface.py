"""Portfolio-only interface skeleton. This module is intentionally non-runnable."""


class DiscordAuditLogBotInterface:
    """Architectural surface of the private production implementation."""

    async def handle_message_event(self, *args, **kwargs):
        """Public portfolio signature only. Production logic is private."""
        raise NotImplementedError("Production implementation is private")

    async def handle_voice_event(self, *args, **kwargs):
        """Public portfolio signature only. Production logic is private."""
        raise NotImplementedError("Production implementation is private")

    async def resolve_audit_actor(self, *args, **kwargs):
        """Public portfolio signature only. Production logic is private."""
        raise NotImplementedError("Production implementation is private")

    async def emit_audit_record(self, *args, **kwargs):
        """Public portfolio signature only. Production logic is private."""
        raise NotImplementedError("Production implementation is private")

