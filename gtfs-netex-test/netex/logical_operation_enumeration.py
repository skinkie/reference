from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class LogicalOperationEnumeration(Enum):
    """Allowed values for logical operations.

    See https://en.wikipedia.org/wiki/Logic_gate

    :cvar AND: Successive elements are logically ANDed together;
        comparison must satisfy all specified values.
    :cvar OR: Successive elements are logically ORed together;
        comparison must satisfy at least one specified value.
    :cvar NOT: Specified elements must be different from the given
        value. If the number of specified elements is equal to 1, the
        function negates it. If the number of specified elements &gt; 1,
        this operator is equal to the NOR operator
    :cvar XOR: Successive elements are logically ORed together;
        comparison must satisfy only one specified value.
    :cvar NAND: Successive elements are logically ANDed together;
        comparison must satisfy all specified values. The result is then
        negated.
    :cvar NOR: Successive elements are logically ORed together;
        comparison must satisfy at least one specified value. The result
        is then negated.
    :cvar XNOR: Successive elements are logically ORed together;
        comparison must satisfy only one specified value. The result is
        then negated.
    """
    AND = "AND"
    OR = "OR"
    NOT = "NOT"
    XOR = "XOR"
    NAND = "NAND"
    NOR = "NOR"
    XNOR = "XNOR"
