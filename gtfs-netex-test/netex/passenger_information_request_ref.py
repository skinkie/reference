from dataclasses import dataclass

from .passenger_information_request_ref_structure import PassengerInformationRequestRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class PassengerInformationRequestRef(PassengerInformationRequestRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
