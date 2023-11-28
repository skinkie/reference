from dataclasses import dataclass, field
from netex.organisational_unit_version_structure import OrganisationalUnitVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class OrganisationalUnit(OrganisationalUnitVersionStructure):
    """
    OrganisationalUnit of an ORGANISATION.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
