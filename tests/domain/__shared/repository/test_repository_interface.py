from typing import Any, Dict, Iterable, Optional

import pytest

from src.domain.__shared.repository import IRepository


class StubRepository(IRepository[Dict[str, Any]]):
    def __init__(self) -> None:
        self._data = []

    def add(self, entity: Dict[str, Any]) -> Dict[str, Any]:  # noqa: D102
        self._data.append(entity)
        return entity

    def find(self, filters: Dict[str, Any]) -> Iterable[Dict[str, Any]]:  # noqa: D102
        return [item for item in self._data if all(item.get(k) == v for k, v in filters.items())]

    def find_one(self, filters: Dict[str, Any]) -> Optional[Dict[str, Any]]:  # noqa: D102
        return next(
            (
                item
                for item in self._data
                if all(item.get(k) == v for k, v in filters.items())
            ),
            None,
        )


@pytest.fixture
def repository_fx() -> StubRepository:
    return StubRepository()


def test_add(repository_fx: StubRepository) -> None:
    entity = {"id": "1", "name": "Test Entity"}
    added_entity = repository_fx.add(entity)
    assert added_entity == entity
    assert repository_fx.find_by_id("1") == entity


def test_find(repository_fx: StubRepository) -> None:
    repository_fx.add({"id": "1", "name": "Entity 1", "category": "A"})
    repository_fx.add({"id": "2", "name": "Entity 2", "category": "B"})

    found_entities = repository_fx.find({"category": "A"})
    assert len(list(found_entities)) == 1
    assert next(iter(found_entities))["id"] == "1"


def test_find_one(repository_fx: StubRepository) -> None:
    repository_fx.add({"id": "1", "name": "Entity 1"})

    found_entity = repository_fx.find_one({"id": "1"})
    assert found_entity["name"] == "Entity 1"

    not_found_entity = repository_fx.find_one({"id": "2"})
    assert not_found_entity is None


def test_find_by_id(repository_fx: StubRepository) -> None:
    repository_fx.add({"id": "1", "name": "Entity 1"})

    found_entity = repository_fx.find_by_id("1")
    assert found_entity["name"] == "Entity 1"


def test_find_by_external_id(repository_fx: StubRepository) -> None:
    repository_fx.add({"id": "1", "external_id": "ext1", "name": "Entity 1"})

    found_entity = repository_fx.find_by_external_id("ext1")
    assert found_entity["name"] == "Entity 1"
