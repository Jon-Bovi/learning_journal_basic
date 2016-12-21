def includeme(config):
    """Pyramid route configuration."""
    config.add_static_view(name='static', path='learning_journal_basic:static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('detail', '/journal/{id:\d+}')
    config.add_route('create', '/journal/new-entry')
    config.add_route('update', '/journal/{id:\d+}/edit-entry')
