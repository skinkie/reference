from dataclasses import dataclass
from netex.passenger_accessibility_needs_structure import PassengerAccessibilityNeedsStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PassengerAccessibilityNeeds(PassengerAccessibilityNeedsStructure):
    """A  passenger's requirement for accessibility, comprising one or more USER
    NEEDs.

    For example, that he is unable to navigate stairs, or lifts, or has
    visual or auditory impairments. PASSENGER ACCESSIBILITY NEEDS can be
    used to derive an accessibility constraint for the passenger,
    allowing the computation of paths for passengers with specifically
    constrained mobility. Example: Wheelchair, No Lifts, No Stairs.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
