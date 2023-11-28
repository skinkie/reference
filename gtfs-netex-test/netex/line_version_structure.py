from dataclasses import dataclass, field
from typing import List, Optional
from netex.accessibility_assessment import AccessibilityAssessment
from netex.all_vehicle_modes_of_transport_enumeration import AllVehicleModesOfTransportEnumeration
from netex.allowed_line_directions_rel_structure import AllowedLineDirectionsRelStructure
from netex.alternative_texts_rel_structure import DataManagedObjectStructure
from netex.authority_ref import AuthorityRef
from netex.contact_structure import ContactStructure
from netex.external_object_ref_structure import ExternalObjectRefStructure
from netex.group_of_lines_ref_structure import GroupOfLinesRefStructure
from netex.info_links_rel_structure import InfoLinksRelStructure
from netex.line_type_enumeration import LineTypeEnumeration
from netex.mode_refs_rel_structure import ModeRefsRelStructure
from netex.multilingual_string import MultilingualString
from netex.notice_assignments_rel_structure import NoticeAssignmentsRelStructure
from netex.operational_context_ref import OperationalContextRef
from netex.operator_ref import OperatorRef
from netex.payment_method_enumeration import PaymentMethodEnumeration
from netex.presentation_structure import PresentationStructure
from netex.print_presentation_structure import PrintPresentationStructure
from netex.private_code import PrivateCode
from netex.purchase_moment_enumeration import PurchaseMomentEnumeration
from netex.route_refs_rel_structure import RouteRefsRelStructure
from netex.transport_organisation_refs_rel_structure import TransportOrganisationRefsRelStructure
from netex.transport_submode import TransportSubmode
from netex.type_of_line_ref import TypeOfLineRef
from netex.type_of_payment_method_value_structure import TypeOfPaymentMethodValueStructure
from netex.type_of_product_category_ref import TypeOfProductCategoryRef
from netex.type_of_service_ref import TypeOfServiceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class LineVersionStructure(DataManagedObjectStructure):
    """
    Type for a LINE.

    :ivar name: Name of LINE.
    :ivar short_name: Short name of LINE.
    :ivar description: Description of LINE.
    :ivar transport_mode: Transport MODE of LINE.
    :ivar transport_submode:
    :ivar url: Web link for LINE.
    :ivar public_code: Public identifier of a LINe.
    :ivar private_code:
    :ivar external_line_ref: An alternative  code that uniquely
        identifies the LINE specifically for use in AVMS systems. For
        VDV compatibility.
    :ivar authority_ref_or_operator_ref:
    :ivar additional_operators: Additional OPERATORs for LINE.
    :ivar other_modes: Additional transport MODEs for LINE.
    :ivar operational_context_ref:
    :ivar line_type: Classification of LINE. +v1.1.
    :ivar type_of_line_ref:
    :ivar external_product_category_ref: An default product
        classification for all journeys of the lin e for use in AVMS
        systems. For VDV compatibility. +v1.1
    :ivar type_of_product_category_ref:
    :ivar type_of_service_ref:
    :ivar monitored: Whether real-time data is normally available for
        LINE.
    :ivar routes: Routes that follow the LINE.
    :ivar represented_by_group_ref: GROUPS OF LINEs that can be used to
        represent LINE.
    :ivar presentation: Presentation values to use when rendering LINE,
        such as a colour.
    :ivar alternative_presentation: Alternative Presentation values to
        use when rendering LINE, such as a colour.
    :ivar printed_presentation: Presentation values to use in printed
        material for LINE, such as a colour. +v1.1
    :ivar payment_methods: Payment Methods allowed on LINE. +v1.1
    :ivar types_of_payment_method: TYPES OF PAYMENT yment Methods
        allowed on LINE. +v1.1
    :ivar purchase_moment: PURCHASE MOMENT types allowed on LINE. +v1.1
    :ivar contact_details: CantactDetails for Line +V1.1
    :ivar accessibility_assessment:
    :ivar allowed_directions: Allowed directions for routes of LINE.
    :ivar notice_assignments: NOTICES assigned to LINE.
    :ivar document_links: Timetable documents associated with the LINE,
        e.g pdf files
    """
    class Meta:
        name = "Line_VersionStructure"

    name: MultilingualString = field(
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
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
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    transport_mode: Optional[AllVehicleModesOfTransportEnumeration] = field(
        default=None,
        metadata={
            "name": "TransportMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    transport_submode: Optional[TransportSubmode] = field(
        default=None,
        metadata={
            "name": "TransportSubmode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    url: Optional[str] = field(
        default=None,
        metadata={
            "name": "Url",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    public_code: Optional[str] = field(
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
    external_line_ref: Optional[ExternalObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "ExternalLineRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    authority_ref_or_operator_ref: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AuthorityRef",
                    "type": AuthorityRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OperatorRef",
                    "type": OperatorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    additional_operators: Optional[TransportOrganisationRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "additionalOperators",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    other_modes: Optional[ModeRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "otherModes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    operational_context_ref: Optional[OperationalContextRef] = field(
        default=None,
        metadata={
            "name": "OperationalContextRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    line_type: Optional[LineTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "LineType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_line_ref: Optional[TypeOfLineRef] = field(
        default=None,
        metadata={
            "name": "TypeOfLineRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    external_product_category_ref: Optional[ExternalObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "ExternalProductCategoryRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_product_category_ref: Optional[TypeOfProductCategoryRef] = field(
        default=None,
        metadata={
            "name": "TypeOfProductCategoryRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_service_ref: Optional[TypeOfServiceRef] = field(
        default=None,
        metadata={
            "name": "TypeOfServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    monitored: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Monitored",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    routes: Optional[RouteRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    represented_by_group_ref: Optional[GroupOfLinesRefStructure] = field(
        default=None,
        metadata={
            "name": "RepresentedByGroupRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    presentation: Optional[PresentationStructure] = field(
        default=None,
        metadata={
            "name": "Presentation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    alternative_presentation: Optional[PresentationStructure] = field(
        default=None,
        metadata={
            "name": "AlternativePresentation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    printed_presentation: Optional[PrintPresentationStructure] = field(
        default=None,
        metadata={
            "name": "PrintedPresentation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    payment_methods: List[PaymentMethodEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "PaymentMethods",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    types_of_payment_method: Optional[TypeOfPaymentMethodValueStructure] = field(
        default=None,
        metadata={
            "name": "typesOfPaymentMethod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    purchase_moment: List[PurchaseMomentEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "PurchaseMoment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
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
    accessibility_assessment: Optional[AccessibilityAssessment] = field(
        default=None,
        metadata={
            "name": "AccessibilityAssessment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    allowed_directions: Optional[AllowedLineDirectionsRelStructure] = field(
        default=None,
        metadata={
            "name": "allowedDirections",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    notice_assignments: Optional[NoticeAssignmentsRelStructure] = field(
        default=None,
        metadata={
            "name": "noticeAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    document_links: Optional[InfoLinksRelStructure] = field(
        default=None,
        metadata={
            "name": "documentLinks",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
