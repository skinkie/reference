from dataclasses import dataclass
from .default_connection_ref_structure import DefaultConnectionRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DefaultConnectionRef(DefaultConnectionRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
