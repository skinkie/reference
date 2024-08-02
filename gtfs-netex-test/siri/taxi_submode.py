from dataclasses import dataclass, field

from .taxi_submodes_of_transport_enumeration import TaxiSubmodesOfTransportEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class TaxiSubmode:
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: TaxiSubmodesOfTransportEnumeration = field(
        default=TaxiSubmodesOfTransportEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
