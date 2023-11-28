from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class TravelCreditPolicyEnumeration(Enum):
    """
    Allowed values for  Credit Policy.

    :cvar ALLOW_TRAVEL: Policy if credit threhsold is exceeded is still
        to allow further travel.
    :cvar BLOCK_ALL_TRAVEL: Policy if credit threhsold is exceeded is to
        block all travel bu yuser.
    :cvar BLOCK_PAY_AS_YOU_GO_TRAVEL: Policy if credit threhsold is
        exceeded is to block on demand travel, but still permit period
        pass travel.
    :cvar OTHER:
    """
    ALLOW_TRAVEL = "allowTravel"
    BLOCK_ALL_TRAVEL = "blockAllTravel"
    BLOCK_PAY_AS_YOU_GO_TRAVEL = "blockPayAsYouGoTravel"
    OTHER = "other"
