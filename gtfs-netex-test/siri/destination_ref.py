from dataclasses import dataclass

from .destination_ref_structure import DestinationRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class DestinationRef(DestinationRefStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
