from dataclasses import dataclass, field
from typing import Optional
from netex.companion_profiles_rel_structure import CompanionProfilesRelStructure
from netex.group_booking_enumeration import GroupBookingEnumeration
from netex.group_check_in_enumeration import GroupCheckInEnumeration
from netex.group_size_changes_enumeration import GroupSizeChangesEnumeration
from netex.group_ticketing_enumeration import GroupTicketingEnumeration
from netex.per_basis_enumeration import PerBasisEnumeration
from netex.type_of_concession_ref import TypeOfConcessionRef
from netex.usage_parameter_version_structure import UsageParameterVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GroupTicketVersionStructure(UsageParameterVersionStructure):
    """
    Type for GROUP TICKET.

    :ivar type_of_concession_ref:
    :ivar minimum_number_of_persons: Maximum number of persons overall
        allowed on GROUP TICKET.
    :ivar maximum_number_of_persons: Maximum number of persons overall
        allowed on GROUP TICKET.
    :ivar minimum_number_of_card_holders: Minium number of card holders
        needed on GROUP TICKET, if any.
    :ivar companion_profiles: Minimum and maximum numbers of users in
        each category  allowed on GROUP TICKET.
    :ivar pricing_basis: Whether pricing is per person or for whole
        group.
    :ivar maximum_persons_free: Minimum number of free people allowed on
        ticket.
    :ivar maximum_persons_discounted: Minimum number of discounted
        persons allowed on GROUP TICKET.
    :ivar discount_only_for_first_person: Whether there is only a
        discount for the first person in the group.
    :ivar one_for_npersons: Discount is given as one free place for  n
        people. Intermediate numbers are rounded down.
    :ivar group_size_changes: Possibilities for changiing the numbe of
        people in the group.
    :ivar ticketing: Natute of tickets issued for group
    :ivar joint_check_in: Whether the group must check in together.
    :ivar group_booking_facility:
    """
    class Meta:
        name = "GroupTicket_VersionStructure"

    type_of_concession_ref: Optional[TypeOfConcessionRef] = field(
        default=None,
        metadata={
            "name": "TypeOfConcessionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    minimum_number_of_persons: Optional[int] = field(
        default=None,
        metadata={
            "name": "MinimumNumberOfPersons",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    maximum_number_of_persons: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaximumNumberOfPersons",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    minimum_number_of_card_holders: Optional[int] = field(
        default=None,
        metadata={
            "name": "MinimumNumberOfCardHolders",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    companion_profiles: Optional[CompanionProfilesRelStructure] = field(
        default=None,
        metadata={
            "name": "companionProfiles",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    pricing_basis: Optional[PerBasisEnumeration] = field(
        default=None,
        metadata={
            "name": "PricingBasis",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    maximum_persons_free: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaximumPersonsFree",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    maximum_persons_discounted: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaximumPersonsDiscounted",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    discount_only_for_first_person: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DiscountOnlyForFirstPerson",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    one_for_npersons: Optional[int] = field(
        default=None,
        metadata={
            "name": "OneForNPersons",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    group_size_changes: Optional[GroupSizeChangesEnumeration] = field(
        default=None,
        metadata={
            "name": "GroupSizeChanges",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    ticketing: Optional[GroupTicketingEnumeration] = field(
        default=None,
        metadata={
            "name": "Ticketing",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    joint_check_in: Optional[GroupCheckInEnumeration] = field(
        default=None,
        metadata={
            "name": "JointCheckIn",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    group_booking_facility: Optional[GroupBookingEnumeration] = field(
        default=None,
        metadata={
            "name": "GroupBookingFacility",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
