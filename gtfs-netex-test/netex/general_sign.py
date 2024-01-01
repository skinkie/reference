from dataclasses import dataclass
from .general_sign_structure import GeneralSignStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GeneralSign(GeneralSignStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
