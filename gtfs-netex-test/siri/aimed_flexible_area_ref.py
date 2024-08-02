from dataclasses import dataclass

from .flexible_area_ref_structure import FlexibleAreaRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class AimedFlexibleAreaRef(FlexibleAreaRefStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
