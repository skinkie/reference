from dataclasses import dataclass

from .flexible_point_properties_versioned_child_structure import FlexiblePointPropertiesVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class FlexiblePointProperties(FlexiblePointPropertiesVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
