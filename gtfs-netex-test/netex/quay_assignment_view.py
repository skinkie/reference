from dataclasses import dataclass
from netex.passenger_stop_assignment_derived_view_structure import PassengerStopAssignmentDerivedViewStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class QuayAssignmentView(PassengerStopAssignmentDerivedViewStructure):
    """
    Assignment to a specific QUAY within the STOP PLACE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
