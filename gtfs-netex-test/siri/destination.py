from dataclasses import dataclass

from .annotated_destination_structure import AnnotatedDestinationStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class Destination(AnnotatedDestinationStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
