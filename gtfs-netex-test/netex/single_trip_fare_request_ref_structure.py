from dataclasses import dataclass

from .fare_request_ref_structure import FareRequestRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class SingleTripFareRequestRefStructure(FareRequestRefStructure):
    pass
