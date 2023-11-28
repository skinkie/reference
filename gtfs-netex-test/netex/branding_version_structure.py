from dataclasses import dataclass, field
from typing import Optional
from netex.presentation_structure import PresentationStructure
from netex.type_of_value_version_structure import TypeOfValueVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class BrandingVersionStructure(TypeOfValueVersionStructure):
    """
    Type for a BRANDING.

    :ivar presentation: Preferred presentation values associated with
        BRANDING. +v1.1
    """
    class Meta:
        name = "Branding_VersionStructure"

    presentation: Optional[PresentationStructure] = field(
        default=None,
        metadata={
            "name": "Presentation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
