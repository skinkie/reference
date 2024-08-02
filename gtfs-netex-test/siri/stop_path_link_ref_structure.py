from dataclasses import dataclass

from .stop_place_component_ref_structure import StopPlaceComponentRefStructure

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass(kw_only=True)
class StopPathLinkRefStructure(StopPlaceComponentRefStructure):
    pass
