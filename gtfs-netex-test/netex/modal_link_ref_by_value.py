from dataclasses import dataclass

from .modal_link_ref_by_value_structure import ModalLinkRefByValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ModalLinkRefByValue(ModalLinkRefByValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
