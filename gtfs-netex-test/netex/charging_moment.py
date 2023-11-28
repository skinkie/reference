from dataclasses import dataclass, field
from netex.charging_moment_value_structure import ChargingMomentValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ChargingMoment(ChargingMomentValueStructure):
    """A classification of FARE PRODUCTs according to the payment method and the account location: pre-payment with cancellation (throw-away), pre-payment with debit on a value card, pre-payment without consumption registration (pass), post-payment etc.

    :ivar id: Identifier of CHARGING MOMENT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
