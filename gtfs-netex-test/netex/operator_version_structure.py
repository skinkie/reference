from dataclasses import dataclass
from netex.transport_organisation_version_structure import TransportOrganisationVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class OperatorVersionStructure(TransportOrganisationVersionStructure):
    """
    Type for an OPERATOR.
    """
    class Meta:
        name = "Operator_VersionStructure"
