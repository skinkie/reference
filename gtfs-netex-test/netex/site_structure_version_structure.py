from dataclasses import dataclass, field
from typing import Optional, Union

from .entity_in_version_structure import DataManagedObjectStructure
from .levels_in_structure_rel_structure import LevelsInStructureRelStructure
from .multilingual_string import MultilingualString
from .parking_ref import ParkingRef
from .point_of_interest_ref import PointOfInterestRef
from .service_site_ref import ServiceSiteRef
from .site_ref import SiteRef
from .stop_place_ref import StopPlaceRef
from .taxi_rank_ref import TaxiRankRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SiteStructureVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "SiteStructure_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    site_ref_or_stop_place_ref: Optional[Union[ParkingRef, PointOfInterestRef, TaxiRankRef, StopPlaceRef, ServiceSiteRef, SiteRef]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ParkingRef",
                    "type": ParkingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointOfInterestRef",
                    "type": PointOfInterestRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TaxiRankRef",
                    "type": TaxiRankRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StopPlaceRef",
                    "type": StopPlaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceSiteRef",
                    "type": ServiceSiteRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SiteRef",
                    "type": SiteRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    levels_in_structure: Optional[LevelsInStructureRelStructure] = field(
        default=None,
        metadata={
            "name": "levelsInStructure",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
