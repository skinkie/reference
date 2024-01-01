from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SameUserEnumeration(Enum):
    SAME_PERSON = "samePerson"
    DIFFERENT_PERSON = "differentPerson"
    ANY_ONE = "anyOne"
    SPECIFIC = "specific"
