from dataclasses import dataclass, field
from netex.branding_version_structure import BrandingVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class Branding(BrandingVersionStructure):
    """
    An arbitrary marketing classification.

    :ivar id: Identifier of Branding
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
