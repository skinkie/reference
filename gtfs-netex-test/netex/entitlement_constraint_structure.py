from dataclasses import dataclass, field
from typing import Optional
from netex.same_class_of_use_enumeration import SameClassOfUseEnumeration
from netex.same_journey_enumeration import SameJourneyEnumeration
from netex.same_operator_enumeration import SameOperatorEnumeration
from netex.same_period_enumeration import SamePeriodEnumeration
from netex.same_route_enumeration import SameRouteEnumeration
from netex.same_stop_enumeration import SameStopEnumeration
from netex.same_type_of_product_category_enumeration import SameTypeOfProductCategoryEnumeration
from netex.same_type_of_travel_document_enumeration import SameTypeOfTravelDocumentEnumeration
from netex.same_user_enumeration import SameUserEnumeration
from netex.same_zone_enumeration import SameZoneEnumeration
from netex.user_profile_refs_rel_structure import UserProfileRefsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class EntitlementConstraintStructure:
    """Entitlement constraints related product or offe.

    +v1.1.

    :ivar period_constraint: Constraints on  valdity period.
    :ivar origin_constraint: Constraints on origin SCHEDULED STOP POINT
    :ivar destination_constraint: Constraints on  destination SCHEDULED
        STOP POINT
    :ivar tariff_zone_constraint: Constraints on TARIFF ZONE.
    :ivar route_constraint: Constraints on ROUTE
    :ivar direction_constraint: Constraints on DIRECTION.
    :ivar operator_constraint: Constraints on OPERATOR.
    :ivar type_of_product_category_constraint: Constraints on  TYPE OF
        PRODUCT CATEGORY
    :ivar class_of_use_constraint: Constraints on CLASS OF USE.
    :ivar type_of_travel_document_constraint: Constraints on  TYPE OF
        TRAVEL DOCUMENT
    :ivar journey_constraint: Constraints on   SERVICE JOURNEYs  to be
        used.
    :ivar user_constraint: Constraints on  USER. Default is samePerson.
    :ivar specific_to_profiles: USER PROFILEs to which entitlement
        applies
    """
    period_constraint: Optional[SamePeriodEnumeration] = field(
        default=None,
        metadata={
            "name": "PeriodConstraint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    origin_constraint: Optional[SameStopEnumeration] = field(
        default=None,
        metadata={
            "name": "OriginConstraint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    destination_constraint: Optional[SameStopEnumeration] = field(
        default=None,
        metadata={
            "name": "DestinationConstraint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    tariff_zone_constraint: Optional[SameZoneEnumeration] = field(
        default=None,
        metadata={
            "name": "TariffZoneConstraint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    route_constraint: Optional[SameRouteEnumeration] = field(
        default=None,
        metadata={
            "name": "RouteConstraint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    direction_constraint: Optional[SameRouteEnumeration] = field(
        default=None,
        metadata={
            "name": "DirectionConstraint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    operator_constraint: Optional[SameOperatorEnumeration] = field(
        default=None,
        metadata={
            "name": "OperatorConstraint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_product_category_constraint: Optional[SameTypeOfProductCategoryEnumeration] = field(
        default=None,
        metadata={
            "name": "TypeOfProductCategoryConstraint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    class_of_use_constraint: Optional[SameClassOfUseEnumeration] = field(
        default=None,
        metadata={
            "name": "ClassOfUseConstraint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_travel_document_constraint: Optional[SameTypeOfTravelDocumentEnumeration] = field(
        default=None,
        metadata={
            "name": "TypeOfTravelDocumentConstraint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    journey_constraint: Optional[SameJourneyEnumeration] = field(
        default=None,
        metadata={
            "name": "JourneyConstraint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    user_constraint: Optional[SameUserEnumeration] = field(
        default=None,
        metadata={
            "name": "UserConstraint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    specific_to_profiles: Optional[UserProfileRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "specificToProfiles",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
