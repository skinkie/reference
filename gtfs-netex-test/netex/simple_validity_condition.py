from dataclasses import dataclass
from netex.alternative_texts_rel_structure import ValidBetweenVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SimpleValidityCondition(ValidBetweenVersionStructure):
    """OPTIMISATION Simple version of a VALIDITY CONDITION used in order to
    characterise a given VERSION of a VERSION FRAME.

    Comprises a simple period.Deprecated.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
