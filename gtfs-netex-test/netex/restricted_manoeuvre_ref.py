from dataclasses import dataclass
from netex.restricted_manoeuvre_ref_structure import RestrictedManoeuvreRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RestrictedManoeuvreRef(RestrictedManoeuvreRefStructure):
    """
    Reference to a MEETING RESTRICTION.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
