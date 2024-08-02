from dataclasses import dataclass

from .annotated_stop_point_structure import AnnotatedStopPointStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class AnnotatedStopPointRef(AnnotatedStopPointStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
