from dataclasses import dataclass

from .passenger_stop_assignment_derived_view_structure import PassengerStopAssignmentDerivedViewStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class QuayAssignmentView(PassengerStopAssignmentDerivedViewStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
