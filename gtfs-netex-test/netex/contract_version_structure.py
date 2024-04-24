from dataclasses import dataclass, field
from typing import Optional

from .contract_type_enumeration import ContractTypeEnumeration
from .entity_in_version_structure import DataManagedObjectStructure
from .info_links_rel_structure import InfoLinksRelStructure
from .legal_status_enumeration import LegalStatusEnumeration
from .multilingual_string import MultilingualString
from .organisation_refs_rel_structure import OrganisationRefsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ContractVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "Contract_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    contract_type: Optional[ContractTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "ContractType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    legal_status: Optional[LegalStatusEnumeration] = field(
        default=None,
        metadata={
            "name": "LegalStatus",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    contract_governing_law: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "ContractGoverningLaw",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    contractees: Optional[OrganisationRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    contractors: OrganisationRefsRelStructure = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    contract_documents: Optional[InfoLinksRelStructure] = field(
        default=None,
        metadata={
            "name": "contractDocuments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
