from dataclasses import dataclass
from .modal_link_ref_by_value_structure import ModalLinkRefByValueStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ModalLinkRefByValue(ModalLinkRefByValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
