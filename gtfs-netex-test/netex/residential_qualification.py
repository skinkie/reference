from dataclasses import dataclass

from .residential_qualification_version_structure import ResidentialQualificationVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ResidentialQualification(ResidentialQualificationVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
