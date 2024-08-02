from dataclasses import dataclass

from .flexible_area_structure import FlexibleAreaStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class AimedFlexibleArea(FlexibleAreaStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
