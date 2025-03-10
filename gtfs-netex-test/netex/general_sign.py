from dataclasses import dataclass

from .general_sign_structure import GeneralSignStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class GeneralSign(GeneralSignStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
