from dataclasses import dataclass, field
from netex.control_centre_version_structure import ControlCentreVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ControlCentre(ControlCentreVersionStructure):
    """
    An ORGANISATION PART for an operational team who are responsible for issuing
    commands to control the services.

    :ivar id: Identifier of CONTROL CENTRE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
