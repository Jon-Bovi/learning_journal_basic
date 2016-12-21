"""Testing module."""
import pytest
from pyramid import testing


@pytest.fixture
def req():
    reque = testing.DummyRequest()
    return reque


def test_home_view_renders_home_data(req):
    """My home page view returns dictionary."""
    from .views import home
    response = home(req).replace(' ', '')
    assert 'bag' in response


def test_home_has_iterable(req):
    from .views import home
    response = home(req)
    assert hasattr(response['bag'], '__iter__')


@pytest.fixture
def testapp():
    from webtest import TestApp
    from learning_journal_basic import main
    app = main({})
    return TestApp(app)


def test_home_has_list(testapp):
    response = testapp.get('/', status=200)
    inner_html = response.html
    import pdb;r
    assert len(inner_html.find_all('li')) == 3
