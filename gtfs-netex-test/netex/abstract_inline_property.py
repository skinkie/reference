from dataclasses import dataclass

from .inline_property_type import InlinePropertyType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass(slots=True, kw_only=True)
class AbstractInlineProperty(InlinePropertyType):
    class Meta:
        name = "abstractInlineProperty"
        namespace = "http://www.opengis.net/gml/3.2"
