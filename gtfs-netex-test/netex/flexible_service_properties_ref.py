from dataclasses import dataclass
from netex.flexible_service_properties_ref_structure import FlexibleServicePropertiesRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FlexibleServicePropertiesRef(FlexibleServicePropertiesRefStructure):
    """
    Reference to a FLEXIBLE SERVICE PROPERTIES.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
