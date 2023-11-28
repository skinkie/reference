from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SameUserEnumeration(Enum):
    """
    Allowed values for User ENTITLEMENT CONSTRAINT.
    """
    SAME_PERSON = "samePerson"
    DIFFERENT_PERSON = "differentPerson"
    ANY_ONE = "anyOne"
    SPECIFIC = "specific"
