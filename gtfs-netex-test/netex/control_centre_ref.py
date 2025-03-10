from dataclasses import dataclass

from .control_centre_ref_structure import ControlCentreRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ControlCentreRef(ControlCentreRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
