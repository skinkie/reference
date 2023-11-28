from dataclasses import dataclass
from netex.residential_qualification_ref_structure import ResidentialQualificationRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ResidentialQualificationRef(ResidentialQualificationRefStructure):
    """
    Reference to a RESIDENTIAL QUALIFICATION usage parameter.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
