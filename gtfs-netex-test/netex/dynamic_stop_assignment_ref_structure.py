from dataclasses import dataclass

from .passenger_stop_assignment_ref_structure import (
    PassengerStopAssignmentRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DynamicStopAssignmentRefStructure(PassengerStopAssignmentRefStructure):
    pass
