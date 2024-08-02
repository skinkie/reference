from dataclasses import dataclass, field
from typing import List, Optional

from .actions_structure import ActionsStructure
from .country_ref_structure import CountryRefStructure
from .extensions_1 import Extensions1
from .natural_language_string_structure import NaturalLanguageStringStructure
from .network_context_structure import NetworkContextStructure
from .participant_ref_structure import ParticipantRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ContextStructure:
    country_ref: Optional[CountryRefStructure] = field(
        default=None,
        metadata={
            "name": "CountryRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    participant_ref: ParticipantRefStructure = field(
        metadata={
            "name": "ParticipantRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    topographic_place_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "TopographicPlaceRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    topographic_place_name: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "TopographicPlaceName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    default_language: Optional[str] = field(
        default=None,
        metadata={
            "name": "DefaultLanguage",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    network_context: Optional[NetworkContextStructure] = field(
        default=None,
        metadata={
            "name": "NetworkContext",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    actions: Optional[ActionsStructure] = field(
        default=None,
        metadata={
            "name": "Actions",
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
