from dataclasses import dataclass

from .commercial_profile_ref_structure import CommercialProfileRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CommercialProfileRef(CommercialProfileRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
