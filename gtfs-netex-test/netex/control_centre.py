from dataclasses import dataclass

from .control_centre_version_structure import ControlCentreVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ControlCentre(ControlCentreVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
