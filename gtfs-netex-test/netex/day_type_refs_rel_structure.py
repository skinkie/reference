from dataclasses import dataclass, field
from typing import Union

from .day_type_ref import DayTypeRef
from .fare_day_type_ref import FareDayTypeRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class DayTypeRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "dayTypeRefs_RelStructure"

    day_type_ref: list[Union[FareDayTypeRef, DayTypeRef]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FareDayTypeRef",
                    "type": FareDayTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DayTypeRef",
                    "type": DayTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
