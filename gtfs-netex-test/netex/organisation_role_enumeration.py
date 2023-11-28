from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class OrganisationRoleEnumeration(Enum):
    """Allowed values for RELATED ORGANISATION role.

    +v1.2.2

    :cvar SUBSIDIARY: Related ORGANISATION is a subsidiary of this
        organisation.
    :cvar OWNER: Related ORGANISATION owns this organisation.
    :cvar COLLABORATOR: Related ORGANISATION collaborates with this
        organisation.
    :cvar CONTRACT_ISSUER: Related ORGANISATION contracts to  this
        organisation to supply it.
    :cvar SUBCONTRACTOR: Related ORGANISATION services contracts for
        this organisation..
    :cvar REGULATOR: Related ORGANISATION regulates this organisation.
    :cvar STATUTORY_RESPONSIBILITY: Related ORGANISATION is subject to
        regulation by this organisation.
    :cvar DISTRIBUTOR: Related ORGANISATION distributes products for
        this organisation.
    :cvar SUPPLIER: Related ORGANISATION supplies products or services
        to this organisation.
    :cvar OTHER: Other role type ORGANISATION.
    """
    SUBSIDIARY = "subsidiary"
    OWNER = "owner"
    COLLABORATOR = "collaborator"
    CONTRACT_ISSUER = "contractIssuer"
    SUBCONTRACTOR = "subcontractor"
    REGULATOR = "regulator"
    STATUTORY_RESPONSIBILITY = "statutoryResponsibility"
    DISTRIBUTOR = "distributor"
    SUPPLIER = "supplier"
    OTHER = "other"
