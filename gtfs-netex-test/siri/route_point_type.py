from dataclasses import dataclass, field

from .route_point_type_enumeration import RoutePointTypeEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class RoutePointType:
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: RoutePointTypeEnumeration = field(
        default=RoutePointTypeEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
