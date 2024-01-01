from dataclasses import dataclass
from .reference_type import ReferenceType


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass(kw_only=True)
class DescriptionReference(ReferenceType):
    class Meta:
        name = "descriptionReference"
        namespace = "http://www.opengis.net/gml/3.2"
