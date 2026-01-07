import pytest
from pink_morsels.web import create_app


@pytest.fixture
def app():
    return create_app()


def test_header_present(dash_duo, app):
    dash_duo.start_server(app)

    header = dash_duo.find_element("h1")
    assert header.text == "Pink Morsel Sales Visualiser"


def test_visualisation_present(dash_duo, app):
    dash_duo.start_server(app)

    graph = dash_duo.find_element("#sales-line-chart")
    assert graph is not None


def test_region_picker_present(dash_duo, app):
    dash_duo.start_server(app)

    radio_items = dash_duo.find_element("#region-filter")
    assert radio_items is not None
