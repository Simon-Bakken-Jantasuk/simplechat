CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer', # For simplicity, use in-memory channel layer. For production, use Redis or similar.
    },
}
