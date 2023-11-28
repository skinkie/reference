from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class OnBecomingEnumeration(Enum):
    """
    Allowed values for Becoming Eiiigble + v1.1.

    :cvar AUTOMATIC: If user becomes eligible, automatically apply
        additional user profile benefits to user, e.g. apply student or
        senior discounts.
    :cvar INVITE: If user becomes eligible, invite user to take up
        eligible products. e.g. Invite to buy Senior railcard.
    :cvar NO_ACTION: If user becomes eligible,, no automatic measures
        are taken.
    :cvar OTHER:
    """
    AUTOMATIC = "automatic"
    INVITE = "invite"
    NO_ACTION = "noAction"
    OTHER = "other"
