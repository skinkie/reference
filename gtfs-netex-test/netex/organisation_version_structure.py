from dataclasses import dataclass, field
from typing import List, Optional
from netex.alternative_names_rel_structure import AlternativeNamesRelStructure
from netex.alternative_texts_rel_structure import (
    DataManagedObjectStructure,
    ValidBetweenVersionStructure,
)
from netex.contact_structure import ContactStructure
from netex.external_object_ref_structure import ExternalObjectRefStructure
from netex.locale import Locale
from netex.multilingual_string import MultilingualString
from netex.organisation_parts_rel_structure import OrganisationPartsRelStructure
from netex.organisation_refs_rel_structure import OrganisationRefsRelStructure
from netex.organisation_type_enumeration import OrganisationTypeEnumeration
from netex.private_code import PrivateCode
from netex.private_code_structure import PrivateCodeStructure
from netex.related_organisations_rel_structure import RelatedOrganisationsRelStructure
from netex.responsibility_sets_rel_structure import ResponsibilitySetsRelStructure
from netex.type_of_organisation_refs_rel_structure import TypeOfOrganisationRefsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class OrganisationVersionStructure(DataManagedObjectStructure):
    """
    Type for an ORGANISATION.

    :ivar public_code: Public code to use for ORGANISATION.
    :ivar private_code:
    :ivar company_number: Company registration number including Country
        prefix.
    :ivar external_operator_ref: An alternative  code that uniquely
        identifies the OPERATOR. Specifically for use in AVMS systems.
        For VDV compatibility.
    :ivar name: The name of the ORGANISATION.
    :ivar short_name: A short name of the ORGANISATION.
    :ivar legal_name: The legal name of the ORGANISATION, if different
        from Name.
    :ivar trading_name: The Trading name of the ORGANISATION given to
        the Public - If different from Name or Legal Name.
    :ivar alternative_names: Alternativie names for ORGANISATION.
    :ivar description: Description of ORGANISATION.
    :ivar remarks: Further remarks about ORGANISATION.
    :ivar locale:
    :ivar contact_details: Contact details for ORGANISATION for Public
        use.
    :ivar private_contact_details: Contact details for ORGANISATION
        Private use.
    :ivar organisation_type: Type of ORGANISATION.
    :ivar types_of_organisation: Classification of OPERATOR. Used for
        arbitrary documentation.
    :ivar status: Whether the ORGANISATION is active. Default is true.
    :ivar validity_period: Period when the ORGANISATION is valid.[NOTE
        COULD DROP THis NOW that have VALIDITY PERIOD on base.
    :ivar parts: Parts of the ORGANISATION.
    :ivar own_responsibility_sets: Own RESPONSIBILITY SETs V1.1
    :ivar delegated_responsibility_sets: Delegated responsibility SETS.
    :ivar delegated_from: Other ORGANISATIONs that delegate to this
        ORGANISATION. (TAP TSI B1.)
    :ivar related_organisations: Related ORGABISATIONs +v1.2,2
    """
    class Meta:
        name = "Organisation_VersionStructure"

    public_code: Optional[PrivateCodeStructure] = field(
        default=None,
        metadata={
            "name": "PublicCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    private_code: Optional[PrivateCode] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    company_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "CompanyNumber",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    external_operator_ref: Optional[ExternalObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "ExternalOperatorRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    short_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    legal_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "LegalName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    trading_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "TradingName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    alternative_names: Optional[AlternativeNamesRelStructure] = field(
        default=None,
        metadata={
            "name": "alternativeNames",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    remarks: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    locale: Optional[Locale] = field(
        default=None,
        metadata={
            "name": "Locale",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    contact_details: Optional[ContactStructure] = field(
        default=None,
        metadata={
            "name": "ContactDetails",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    private_contact_details: Optional[ContactStructure] = field(
        default=None,
        metadata={
            "name": "PrivateContactDetails",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    organisation_type: List[OrganisationTypeEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "OrganisationType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    types_of_organisation: Optional[TypeOfOrganisationRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "typesOfOrganisation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    status: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    validity_period: Optional[ValidBetweenVersionStructure] = field(
        default=None,
        metadata={
            "name": "ValidityPeriod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parts: Optional[OrganisationPartsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    own_responsibility_sets: Optional[ResponsibilitySetsRelStructure] = field(
        default=None,
        metadata={
            "name": "ownResponsibilitySets",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    delegated_responsibility_sets: Optional[ResponsibilitySetsRelStructure] = field(
        default=None,
        metadata={
            "name": "delegatedResponsibilitySets",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    delegated_from: Optional[OrganisationRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "delegatedFrom",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    related_organisations: Optional[RelatedOrganisationsRelStructure] = field(
        default=None,
        metadata={
            "name": "relatedOrganisations",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
