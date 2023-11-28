from dataclasses import dataclass
from netex.geographical_structure_factor_ref_structure import GeographicalStructureFactorRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GeographicalStructureFactorRef(GeographicalStructureFactorRefStructure):
    """
    Reference to a GEOGRAPHICAL STRUCTURE FACTOR.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
