from dataclasses import dataclass
from .fare_request_ref_structure import FareRequestRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SingleTripFareRequestRefStructure(FareRequestRefStructure):
    value: RestrictedVar
