from dataclasses import dataclass

from .abstract_feeder_item_structure import AbstractFeederItemStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class FeederItem(AbstractFeederItemStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
