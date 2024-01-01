from dataclasses import dataclass
from .subscribing_version_structure import SubscribingVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Subscribing(SubscribingVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
