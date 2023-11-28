from dataclasses import dataclass
from netex.reference_type import ReferenceType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass(unsafe_hash=True, kw_only=True)
class DescriptionReference(ReferenceType):
    """The value of this property is a remote text description of the object.

    The xlink:href attribute of the gml:descriptionReference property
    references the external description.
    """
    class Meta:
        name = "descriptionReference"
        namespace = "http://www.opengis.net/gml/3.2"
