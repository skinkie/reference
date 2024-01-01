from dataclasses import dataclass
from .stop_assignment_ref_structure import StopAssignmentRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PassengerStopAssignmentRefStructure(StopAssignmentRefStructure):
    value: RestrictedVar
