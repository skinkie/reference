from dataclasses import dataclass, field
from typing import Optional

from .presentation_structure import PresentationStructure
from .print_presentation_structure import PrintPresentationStructure
from .public_code_structure import PublicCodeStructure
from .zone_version_structure import ZoneVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TariffZoneVersionStructure(ZoneVersionStructure):
    class Meta:
        name = "TariffZone_VersionStructure"

    presentation: Optional[PresentationStructure] = field(
        default=None,
        metadata={
            "name": "Presentation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    printed_presentation: Optional[PrintPresentationStructure] = field(
        default=None,
        metadata={
            "name": "PrintedPresentation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    public_code: Optional[PublicCodeStructure] = field(
        default=None,
        metadata={
            "name": "PublicCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
