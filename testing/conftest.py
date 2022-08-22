import pytest_ordering
import pytest

def pytest_collection_modifyitems(session,config,items):
    # items.reverse()
    for item in items:
        if "add" in item.nodeid:
            item.add_marker(pytest.mark.add)
        elif "div" in item.nodeid:
            item.add_marker(pytest.mark.div)


