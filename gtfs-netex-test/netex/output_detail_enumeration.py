from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class OutputDetailEnumeration(Enum):
    """
    Detail Levels for Network Request.
    """
    ALL = "All"
    BASIC = "Basic"
    NO_GEOMETRY = "NoGeometry"
    XREF = "Xref"
    ALL_WITH_XREF = "AllWithXref"
