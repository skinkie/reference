from dataclasses import dataclass
from netex.flexible_link_properties_ref_structure import FlexibleLinkPropertiesRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FlexibleLinkPropertiesRef(FlexibleLinkPropertiesRefStructure):
    """
    Reference to a FLEXIBLE LINK PROPERTies.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
