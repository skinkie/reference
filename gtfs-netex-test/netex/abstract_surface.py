from dataclasses import dataclass

from .abstract_surface_type import AbstractSurfaceType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass(slots=True, kw_only=True)
class AbstractSurface(AbstractSurfaceType):
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
