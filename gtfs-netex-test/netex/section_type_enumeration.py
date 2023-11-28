from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SectionTypeEnumeration(Enum):
    """
    Allowed values for a type of LONE SECTION.
    """
    TRUNK = "trunk"
    BRANCH = "branch"
    EYEL_BRANCH = "eyelBranch"
    END_LOOP = "endLoop"
    OTHER = "other"
