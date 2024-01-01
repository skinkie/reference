from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class OrganisationRoleEnumeration(Enum):
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
