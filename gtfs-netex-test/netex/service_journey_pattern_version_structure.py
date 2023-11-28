from dataclasses import dataclass, field
from typing import Optional
from netex.section_in_sequence_versioned_child_structure import JourneyPatternVersionStructure
from netex.service_journey_pattern_type_enumeration import ServiceJourneyPatternTypeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ServiceJourneyPatternVersionStructure(JourneyPatternVersionStructure):
    """
    Type for SERVICE JOURNEY PATTERN.

    :ivar service_journey_pattern_type: Type of SERVICE JOURNEY PATTERN.
    """
    class Meta:
        name = "ServiceJourneyPattern_VersionStructure"

    service_journey_pattern_type: Optional[ServiceJourneyPatternTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "ServiceJourneyPatternType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
