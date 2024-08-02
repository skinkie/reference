from dataclasses import dataclass

from .stop_place_ref_structure import StopPlaceRefStructure

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass(kw_only=True)
class StopPlaceRef(StopPlaceRefStructure):
    class Meta:
        namespace = "http://www.ifopt.org.uk/ifopt"
