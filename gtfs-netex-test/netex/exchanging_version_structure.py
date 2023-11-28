from dataclasses import dataclass, field
from typing import Optional
from netex.class_of_use_ref_structure import ClassOfUseRefStructure
from netex.exchangable_to_enumeration import ExchangableToEnumeration
from netex.fare_class_enumeration import FareClassEnumeration
from netex.reselling_version_structure import ResellingVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ExchangingVersionStructure(ResellingVersionStructure):
    """
    Type for EXCHANGING.

    :ivar number_of_exchanges_allowed: Maximum number of exchanges
        allowed.
    :ivar to_fare_class: Fare class to which can exchange, if
        specifically limited.
    :ivar to_class_of_use_ref: Fare class to which can exchange, if
        specifically limited.
    :ivar exchangable_to: Type of fare for which product can be
        exchanged.
    """
    class Meta:
        name = "Exchanging_VersionStructure"

    number_of_exchanges_allowed: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfExchangesAllowed",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    to_fare_class: Optional[FareClassEnumeration] = field(
        default=None,
        metadata={
            "name": "ToFareClass",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    to_class_of_use_ref: Optional[ClassOfUseRefStructure] = field(
        default=None,
        metadata={
            "name": "ToClassOfUseRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    exchangable_to: Optional[ExchangableToEnumeration] = field(
        default=None,
        metadata={
            "name": "ExchangableTo",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
