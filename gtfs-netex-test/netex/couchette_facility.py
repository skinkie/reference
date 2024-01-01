from dataclasses import dataclass, field
from .couchette_facility_enumeration import CouchetteFacilityEnumeration


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CouchetteFacility:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: CouchetteFacilityEnumeration = field(
        default=CouchetteFacilityEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
