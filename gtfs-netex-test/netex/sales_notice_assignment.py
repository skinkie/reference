from dataclasses import dataclass, field
from netex.sales_notice_assignment_version_structure import SalesNoticeAssignmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SalesNoticeAssignment(SalesNoticeAssignmentVersionStructure):
    """
    The assignment of a NOTICE to a SALES OFFER PACKAGE or a GROUP OF SALES OFFER
    PACKAGEs.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
