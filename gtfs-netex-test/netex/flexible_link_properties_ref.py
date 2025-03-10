from dataclasses import dataclass

from .flexible_link_properties_ref_structure import FlexibleLinkPropertiesRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class FlexibleLinkPropertiesRef(FlexibleLinkPropertiesRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
