from dataclasses import dataclass
from netex.control_centre_ref_structure import ControlCentreRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ControlCentreRef(ControlCentreRefStructure):
    """
    Reference to a CONTROL CENTRE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
