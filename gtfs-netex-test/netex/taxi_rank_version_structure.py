from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDuration
from netex.stop_place_version_structure import StopPlaceVersionStructure
from netex.taxi_stands_rel_structure import TaxiStandsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TaxiRankVersionStructure(StopPlaceVersionStructure):
    """
    Type for TAXI RANK.

    :ivar maximum_standing_duration: Maximum time for a vehicle standing
        in the spot
    :ivar taxi_stands: Taxis stands in RANK&gt; NB This is a work around
        as cannout get TAXI STAND to be a Substitution Group for  a
        QUAY. +v1.2.2
    """
    class Meta:
        name = "TaxiRank_VersionStructure"

    maximum_standing_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MaximumStandingDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    taxi_stands: Optional[TaxiStandsRelStructure] = field(
        default=None,
        metadata={
            "name": "taxiStands",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
