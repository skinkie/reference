from dataclasses import dataclass
from netex.accessibility_limitation_versioned_child_structure import AccessibilityLimitationVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AccessibilityLimitation(AccessibilityLimitationVersionedChildStructure):
    """
    A categorisation of the ACCESSIBILITY characteristics of a STOP PLACE COMPONENT
    such as a STOP PATH LINK, STOP PLACE or ACCESS SPACE to indicate its usability
    by passengers with specific needs, for example, those needing wheelchair
    access, step-free access or wanting to avoid confined spaces such as lifts.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
