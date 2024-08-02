from dataclasses import dataclass, field
from typing import List

from .affects_scope_structure import AffectsScopeStructure
from .passenger_information_action import PassengerInformationAction
from .scope_type_enumeration import ScopeTypeEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class PublishingActionStructure:
    publish_at_scope: "PublishingActionStructure.PublishAtScope" = field(
        metadata={
            "name": "PublishAtScope",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    passenger_information_action: List[PassengerInformationAction] = field(
        default_factory=list,
        metadata={
            "name": "PassengerInformationAction",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        },
    )

    @dataclass(kw_only=True)
    class PublishAtScope:
        scope_type: ScopeTypeEnumeration = field(
            metadata={
                "name": "ScopeType",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "required": True,
            }
        )
        affects: AffectsScopeStructure = field(
            metadata={
                "name": "Affects",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "required": True,
            }
        )
