from dataclasses import dataclass, field
from typing import List, Optional
from netex.suitability import Suitability
from netex.user_need import UserNeed

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PassengerAccessibilityNeedsStructure:
    """Type for accessibility needs.

    Records the requirements of a passenger that may affect choice of
    facilities.

    :ivar accompanied_by_carer: Whether the passenger is accompanied by
        a carer or assistant.
    :ivar user_needs: Mobility needs of a user.
    :ivar suitabilities: Suitability needs of a user.
    """
    accompanied_by_carer: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AccompaniedByCarer",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    user_needs: Optional["PassengerAccessibilityNeedsStructure.UserNeeds"] = field(
        default=None,
        metadata={
            "name": "userNeeds",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    suitabilities: Optional["PassengerAccessibilityNeedsStructure.Suitabilities"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )

    @dataclass(unsafe_hash=True, kw_only=True)
    class UserNeeds:
        user_need: List[UserNeed] = field(
            default_factory=list,
            metadata={
                "name": "UserNeed",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            }
        )

    @dataclass(unsafe_hash=True, kw_only=True)
    class Suitabilities:
        suitability: List[Suitability] = field(
            default_factory=list,
            metadata={
                "name": "Suitability",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            }
        )
