from dataclasses import dataclass

from .fare_interval_version_structure import FareIntervalVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareInterval(FareIntervalVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
