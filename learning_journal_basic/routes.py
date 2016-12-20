def includeme(config):
    """Pyramid route configuration."""
    config.add_static_view('static', 'static', cache_max_age=10)
    config.add_route('home', '/')
    config.add_route('detail', '/journal/{id:\d+}')
    config.add_route('create', '/journal/new-entry')
    config.add_route('update', '/journal/{id:\d+}/edit-entry')
