from dataclasses import dataclass
from .alternative_name_ref_structure import AlternativeNameRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AlternativeNameRef(AlternativeNameRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
