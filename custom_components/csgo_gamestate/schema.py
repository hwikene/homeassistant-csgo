import voluptuous as vol


WEBHOOK_SCHEMA = vol.Schema(
    {
        vol.Optional("round"): vol.Schema(
            {
                vol.Optional("phase"): vol.Any("live", "freezetime", "over"),
                vol.Optional("bomb"): vol.Any("planted", "defused", "exploded"),
            },
            extra=vol.ALLOW_EXTRA,
        ),
    },
    extra=vol.ALLOW_EXTRA,
)
