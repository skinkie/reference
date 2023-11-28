from dataclasses import dataclass
from netex.passenger_stop_assignment_derived_view_structure import PassengerStopAssignmentDerivedViewStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PassengerStopAssignmentView(PassengerStopAssignmentDerivedViewStructure):
    """View of an assignment of a SCHEDULED STOP POINT to a STOP PLACE and quay.

    etc.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
