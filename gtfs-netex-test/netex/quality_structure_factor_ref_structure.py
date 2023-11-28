from dataclasses import dataclass
from netex.fare_structure_factor_ref_structure import FareStructureFactorRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class QualityStructureFactorRefStructure(FareStructureFactorRefStructure):
    """
    Type for Reference to a QUALITY STRUCTURE FACTOR.
    """
