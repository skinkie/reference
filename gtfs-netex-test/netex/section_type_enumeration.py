from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SectionTypeEnumeration(Enum):
    TRUNK = "trunk"
    BRANCH = "branch"
    EYEL_BRANCH = "eyelBranch"
    END_LOOP = "endLoop"
    OTHER = "other"
