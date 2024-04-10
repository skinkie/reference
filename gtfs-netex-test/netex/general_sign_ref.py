from dataclasses import dataclass

from .general_sign_ref_structure import GeneralSignRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GeneralSignRef(GeneralSignRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
