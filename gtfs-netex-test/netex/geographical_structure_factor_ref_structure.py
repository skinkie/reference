from dataclasses import dataclass

from .fare_structure_factor_ref_structure import FareStructureFactorRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class GeographicalStructureFactorRefStructure(FareStructureFactorRefStructure):
    pass
