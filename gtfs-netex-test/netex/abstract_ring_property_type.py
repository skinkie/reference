from dataclasses import dataclass, field
from typing import Optional
from netex.linear_ring import LinearRing

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass(unsafe_hash=True, kw_only=True)
class AbstractRingPropertyType:
    """
    A property with the content model of gml:AbstractRingPropertyType encapsulates
    a ring to represent the surface boundary property of a surface.
    """
    linear_ring: Optional[LinearRing] = field(
        default=None,
        metadata={
            "name": "LinearRing",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
