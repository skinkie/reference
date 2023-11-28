from dataclasses import dataclass, field
from netex.general_organisation_version_structure import GeneralOrganisationVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GeneralOrganisation(GeneralOrganisationVersionStructure):
    """
    Any type of GENERAL ORGANISATION.

    :ivar id: Identifier of  GENERAL ORGANISATION.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
