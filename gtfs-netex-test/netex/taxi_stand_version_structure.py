from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDuration
from netex.quay_version_structure import QuayVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TaxiStandVersionStructure(QuayVersionStructure):
    """
    Type for TAXI STAND.

    :ivar maximum_standing_duration: Maximum time for a vehicle standing
        in the spot
    """
    class Meta:
        name = "TaxiStand_VersionStructure"

    maximum_standing_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MaximumStandingDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
