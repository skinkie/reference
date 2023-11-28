from dataclasses import dataclass, field
from netex.complaints_service_version_structure import ComplaintsServiceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ComplaintsService(ComplaintsServiceVersionStructure):
    """
    Specialisation of CUSTOMER SERVICE for COMPLAINTs.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
