from dataclasses import dataclass, field
from typing import List, Optional

from .abstract_service_delivery_structure import AbstractServiceDeliveryStructure
from .context_structure import ContextStructure
from .extensions_1 import Extensions1
from .pt_situation_element_structure import PtSituationElementStructure
from .road_situation_element import RoadSituationElement

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class SituationExchangeDeliveryStructure(AbstractServiceDeliveryStructure):
    pt_situation_context: Optional[ContextStructure] = field(
        default=None,
        metadata={
            "name": "PtSituationContext",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    situations: Optional["SituationExchangeDeliveryStructure.Situations"] = field(
        default=None,
        metadata={
            "name": "Situations",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    extensions: Optional[Extensions1] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    version: str = field(
        default="2.1",
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass(kw_only=True)
    class Situations:
        pt_situation_element: List[PtSituationElementStructure] = field(
            default_factory=list,
            metadata={
                "name": "PtSituationElement",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        road_situation_element: List[RoadSituationElement] = field(
            default_factory=list,
            metadata={
                "name": "RoadSituationElement",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
