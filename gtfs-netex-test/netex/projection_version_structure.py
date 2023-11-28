from dataclasses import dataclass, field
from typing import Optional
from netex.alternative_texts_rel_structure import DataManagedObjectStructure
from netex.complex_feature_ref import ComplexFeatureRef
from netex.multilingual_string import MultilingualString
from netex.simple_feature_ref import SimpleFeatureRef
from netex.spatial_feature_ref import SpatialFeatureRef
from netex.type_of_projection_ref_structure import TypeOfProjectionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ProjectionVersionStructure(DataManagedObjectStructure):
    """
    Type for a PROJECTION.

    :ivar type_of_projection_ref: Type of PROJECTION.
    :ivar name: Description of PROJECTION.
    :ivar
        complex_feature_ref_or_simple_feature_ref_or_spatial_feature_ref:
    :ivar order: Order of Order in which to process PROJECTION.
    """
    class Meta:
        name = "Projection_VersionStructure"

    type_of_projection_ref: Optional[TypeOfProjectionRefStructure] = field(
        default=None,
        metadata={
            "name": "TypeOfProjectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    complex_feature_ref_or_simple_feature_ref_or_spatial_feature_ref: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ComplexFeatureRef",
                    "type": ComplexFeatureRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SimpleFeatureRef",
                    "type": SimpleFeatureRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SpatialFeatureRef",
                    "type": SpatialFeatureRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    order: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
