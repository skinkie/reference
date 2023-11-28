from dataclasses import dataclass, field
from netex.open_transport_mode_value_structure import OpenTransportModeValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class OpenTransportMode(OpenTransportModeValueStructure):
    """Open values TRANSPORT MODE.

    Allows additional named modes to be created. A mode is a
    characterisation of the operation according to the means of
    transport (bus, tram, metro, train, ferry, ship). NOTE : To enforce
    standardisation, enumerated values are generally used in references.
    In The schema.

    :ivar id: Identifier of ENTITY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
