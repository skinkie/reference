from dataclasses import dataclass, field
from netex.restricted_manoeuvre_version_structure import RestrictedManoeuvreVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RestrictedManoeuvre(RestrictedManoeuvreVersionStructure):
    """A specification of a move for a certain type of vehicle.

    It specifies from which INFRASTRUCTURE LINK to which other
    (adjacent) INFRASTRUCTURE LINK a certain can or cannot VEHICLE TYPE
    cannot proceed, due to physical restrictions.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
