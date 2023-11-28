from dataclasses import dataclass, field
from typing import Optional
from netex.country_ref import CountryRef
from netex.projection_version_structure import ProjectionVersionStructure
from netex.topographic_place_ref import TopographicPlaceRef
from netex.version_of_object_ref_structure import VersionOfObjectRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TopographicProjectionVersionStructure(ProjectionVersionStructure):
    """Type for a TOPOGRAPHIC  PROJECTION.

    +v1.1

    :ivar projected_object_ref: Object being projected onto TOPOGRAPHIC
        AALCE&gt; May be given by context.
    :ivar country_ref_or_topographic_place_ref:
    """
    class Meta:
        name = "TopographicProjection_VersionStructure"

    projected_object_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "ProjectedObjectRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    country_ref_or_topographic_place_ref: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "CountryRef",
                    "type": CountryRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TopographicPlaceRef",
                    "type": TopographicPlaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
