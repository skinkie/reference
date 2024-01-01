from dataclasses import dataclass
from .version_of_object_ref_structure import VersionOfObjectRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class NoticeRefStructure(VersionOfObjectRefStructure):
    value: RestrictedVar
