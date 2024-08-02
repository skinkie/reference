from dataclasses import dataclass, field
from typing import List, Optional

from .natural_language_string_structure import NaturalLanguageStringStructure
from .ticket_restriction_enumeration import TicketRestrictionEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class EasementsStructure:
    ticket_restrictions: Optional[TicketRestrictionEnumeration] = field(
        default=None,
        metadata={
            "name": "TicketRestrictions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    easement: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "Easement",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    easement_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "EasementRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
