from dataclasses import dataclass

from .individual_passenger_info_version_structure import IndividualPassengerInfoVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class IndividualPassengerInfo(IndividualPassengerInfoVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
