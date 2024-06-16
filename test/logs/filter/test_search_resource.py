import pytest
from unittest.mock import MagicMock, patch
from logs.filter.search_resource import SearchResource


def test_search_resource_with_empty_resource():

    resource = ""
    assert not SearchResource.filter(resource)


@patch.object(
    ["search?"],
    "src.logs.filter.search_resource.SEARCH_KEYS",
)
@pytest.mark.parametrize(
    "resource",
    [
        "https://fake-domain/sub-domain/search?X?type_c=true"
    ]
)
def test_search_resource_with_search_key(resource: str):

    assert SearchResource.filter(resource)
