from dataclasses import dataclass

from .surface_array_property_type import SurfaceArrayPropertyType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass(slots=True, kw_only=True)
class SurfaceMembers(SurfaceArrayPropertyType):
    class Meta:
        name = "surfaceMembers"
        namespace = "http://www.opengis.net/gml/3.2"
