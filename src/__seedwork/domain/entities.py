from abc import ABC
from dataclasses import dataclass, field, asdict
from typing import Any

from __seedwork.domain.value_objects import UniqueEntityID


@dataclass(frozen=True, slots=True)
class Entity(ABC):

    unique_entity_id: UniqueEntityID = field(
        default_factory=lambda: UniqueEntityID())

    @property
    def id(self):
        return str(self.unique_entity_id)

    def _set(self, name: str, value: Any):
        object.__setattr__(self, name, value)
        return self

    def to_dict(self):
        entity_dict = asdict(self)
        entity_dict.pop("unique_entity_id")
        entity_dict["id"] = self.id
        return entity_dict
