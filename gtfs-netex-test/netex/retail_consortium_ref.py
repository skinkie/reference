from dataclasses import dataclass

from .retail_consortium_ref_structure import RetailConsortiumRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RetailConsortiumRef(RetailConsortiumRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
