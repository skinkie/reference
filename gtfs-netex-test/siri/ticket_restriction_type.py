from dataclasses import dataclass, field

from .ticket_restriction_enumeration import TicketRestrictionEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class TicketRestrictionType:
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: TicketRestrictionEnumeration = field(
        default=TicketRestrictionEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
