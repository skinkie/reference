from dataclasses import dataclass
from .flexible_link_properties_versioned_child_structure import (
    FlexibleLinkPropertiesVersionedChildStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FlexibleLinkProperties(FlexibleLinkPropertiesVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
