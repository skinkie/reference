from dataclasses import dataclass
from netex.validity_trigger_ref_structure import ValidityTriggerRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ValidityTriggerRef(ValidityTriggerRefStructure):
    """Reference to a VALIDITY TRIGGER An External event defining a VALIDITY
    CONDITION.

    E.g. exceptional flow of a river, bad weather, Road closure for
    works.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
