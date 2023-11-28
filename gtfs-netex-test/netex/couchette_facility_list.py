from dataclasses import dataclass, field
from typing import List
from netex.couchette_facility_enumeration import CouchetteFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CouchetteFacilityList:
    """
    List of COUCHETTE FACILITies.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: List[CouchetteFacilityEnumeration] = field(
        default_factory=lambda: [
            CouchetteFacilityEnumeration.UNKNOWN,
        ],
        metadata={
            "tokens": True,
        }
    )
