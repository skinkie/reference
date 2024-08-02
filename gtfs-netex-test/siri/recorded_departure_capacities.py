from dataclasses import dataclass

from .passenger_capacity_structure import PassengerCapacityStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class RecordedDepartureCapacities(PassengerCapacityStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
