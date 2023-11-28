from dataclasses import dataclass
from netex.medium_application_instance_ref_structure import MediumApplicationInstanceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class MediumApplicationInstanceRef(MediumApplicationInstanceRefStructure):
    """Reference to a MEDIUM APPLICATION INSTANCE.

    +v1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
