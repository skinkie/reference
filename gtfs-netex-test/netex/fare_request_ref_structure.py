from dataclasses import dataclass

from .passenger_information_request_ref_structure import PassengerInformationRequestRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareRequestRefStructure(PassengerInformationRequestRefStructure):
    pass
