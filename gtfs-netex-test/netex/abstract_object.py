from dataclasses import dataclass

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass(slots=True, kw_only=True)
class AbstractObject:
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
