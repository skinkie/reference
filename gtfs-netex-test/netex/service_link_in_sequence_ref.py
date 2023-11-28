from dataclasses import dataclass
from netex.service_link_in_sequence_ref_structure import ServiceLinkInSequenceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ServiceLinkInSequenceRef(ServiceLinkInSequenceRefStructure):
    """Reference to a SERVICE LINK IN SEQUENCE.

    If given by context does not need to be stated.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
