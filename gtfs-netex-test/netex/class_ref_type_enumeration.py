from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ClassRefTypeEnumeration(Enum):
    MEMBERS = "members"
    MEMBER_REFERENCES = "memberReferences"
    ALL = "all"
