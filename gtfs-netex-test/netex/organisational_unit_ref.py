from dataclasses import dataclass
from netex.organisational_unit_ref_structure import OrganisationalUnitRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class OrganisationalUnitRef(OrganisationalUnitRefStructure):
    """
    Reference to a ORGANISATIONAL UNIT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
