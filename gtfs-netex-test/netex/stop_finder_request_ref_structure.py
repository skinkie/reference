from dataclasses import dataclass
from .passenger_information_request_ref_structure import (
    PassengerInformationRequestRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class StopFinderRequestRefStructure(PassengerInformationRequestRefStructure):
    value: RestrictedVar
