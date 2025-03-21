from dataclasses import dataclass, field
from typing import Any, Optional

from .alternative_names_rel_structure import AlternativeNamesRelStructure
from .contact_structure import ContactStructure
from .entity_in_version_structure import (
    DataManagedObjectStructure,
    ValidBetweenVersionStructure,
)
from .external_object_ref_structure import ExternalObjectRefStructure
from .locale import Locale
from .multilingual_string import MultilingualString
from .organisation_parts_rel_structure import OrganisationPartsRelStructure
from .organisation_refs_rel_structure import OrganisationRefsRelStructure
from .organisation_type_enumeration import OrganisationTypeEnumeration
from .private_code import PrivateCode
from .public_code_structure import PublicCodeStructure
from .related_organisations_rel_structure import RelatedOrganisationsRelStructure
from .responsibility_sets_rel_structure import ResponsibilitySetsRelStructure
from .type_of_organisation_refs_rel_structure import TypeOfOrganisationRefsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class OrganisationVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "Organisation_VersionStructure"

    public_code: Optional[PublicCodeStructure] = field(
        default=None,
        metadata={
            "name": "PublicCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    private_code: Optional[PrivateCode] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    company_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "CompanyNumber",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    vatnumber: Optional[str] = field(
        default=None,
        metadata={
            "name": "VATNumber",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    external_operator_ref: Optional[ExternalObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "ExternalOperatorRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    short_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    legal_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "LegalName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    trading_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "TradingName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    alternative_names: Optional[AlternativeNamesRelStructure] = field(
        default=None,
        metadata={
            "name": "alternativeNames",
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
    remarks: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    locale: Optional[Locale] = field(
        default=None,
        metadata={
            "name": "Locale",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    contact_details: Optional[ContactStructure] = field(
        default=None,
        metadata={
            "name": "ContactDetails",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    private_contact_details: Optional[ContactStructure] = field(
        default=None,
        metadata={
            "name": "PrivateContactDetails",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    organisation_type: list[OrganisationTypeEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "OrganisationType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    types_of_organisation: Optional[TypeOfOrganisationRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "typesOfOrganisation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    status: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    validity_period: Optional["OrganisationVersionStructure.ValidityPeriod"] = field(
        default=None,
        metadata={
            "name": "ValidityPeriod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    parts: Optional[OrganisationPartsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    own_responsibility_sets: Optional[ResponsibilitySetsRelStructure] = field(
        default=None,
        metadata={
            "name": "ownResponsibilitySets",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    delegated_responsibility_sets: Optional[ResponsibilitySetsRelStructure] = field(
        default=None,
        metadata={
            "name": "delegatedResponsibilitySets",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    delegated_from: Optional[OrganisationRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "delegatedFrom",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    related_organisations: Optional[RelatedOrganisationsRelStructure] = field(
        default=None,
        metadata={
            "name": "relatedOrganisations",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )

    @dataclass(slots=True, kw_only=True)
    class ValidityPeriod(ValidBetweenVersionStructure):
        name: Any = field(
            init=False,
            default=None,
            metadata={
                "type": "Ignore",
            },
        )
        description: Any = field(
            init=False,
            default=None,
            metadata={
                "type": "Ignore",
            },
        )
        conditioned_object_ref: Any = field(
            init=False,
            default=None,
            metadata={
                "type": "Ignore",
            },
        )
        with_condition_ref: Any = field(
            init=False,
            default=None,
            metadata={
                "type": "Ignore",
            },
        )
        key_list: Any = field(
            init=False,
            default=None,
            metadata={
                "type": "Ignore",
            },
        )
        private_codes: Any = field(
            init=False,
            default=None,
            metadata={
                "type": "Ignore",
            },
        )
        extensions: Any = field(
            init=False,
            default=None,
            metadata={
                "type": "Ignore",
            },
        )
        branding_ref: Any = field(
            init=False,
            default=None,
            metadata={
                "type": "Ignore",
            },
        )
        validity_conditions_or_valid_between: Any = field(
            init=False,
            default=None,
            metadata={
                "type": "Ignore",
            },
        )
        alternative_texts: Any = field(
            init=False,
            default=None,
            metadata={
                "type": "Ignore",
            },
        )
