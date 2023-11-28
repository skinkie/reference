from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SetOperatorEnumeration(Enum):
    """Allowed values for set operations.where there are one or more GROUPs OF ENTITTies of a given type - used to distinguish between selection of a whole group or of an item in the group).  Used  in a  product description  to indicate the range from which a choice may be made and in a sales transaction to record the nature of a choice that has been made.
    member                                              Set
    AND         AllMembersAllSets                             AllMembersAllSets
    OR           OneItem 											AllMembers Of OnSet
    XOR         OnlyOneItem from AnyGroup               	AllMembers Of OnlySet      - AllOfOneSet
    NOT			None

    :cvar ONE_OF_ANY_ONE_SET: Only one item from all  referenced GROUPs
        OF ENTITTies of a given type may be selected/has been selected.
    :cvar ONE_OF_EACH_SET: One item from each specified   referenced
        GROUP OF ENTITTies of a given type must be selected/has been
        selected..
    :cvar SOME_OF_ANY_SET: Multiple  items from any referenced GROUP OF
        ENTITTies of a given type  may be selected/have been selected.
    :cvar ALL_OF_ONE_SET: All  items from one specified  referenced
        GROUP OF ENTITTies of a given type  may be selected/have been
        selected.
    :cvar ALL_OF_ALL_SETS: All  items from all  referenced GROUPs OF
        ENTITTies of a given type   may be selected/have been selected.
    """
    ONE_OF_ANY_ONE_SET = "oneOfAnyOneSet"
    ONE_OF_EACH_SET = "oneOfEachSet"
    SOME_OF_ANY_SET = "someOfAnySet"
    ALL_OF_ONE_SET = "allOfOneSet"
    ALL_OF_ALL_SETS = "allOfAllSets"
