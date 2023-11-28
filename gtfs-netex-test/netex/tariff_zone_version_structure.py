from dataclasses import dataclass, field
from typing import Optional
from netex.presentation_structure import PresentationStructure
from netex.print_presentation_structure import PrintPresentationStructure
from netex.zone_version_structure import ZoneVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TariffZoneVersionStructure(ZoneVersionStructure):
    """
    Type for a TARIFF ZONE.

    :ivar presentation: Presentation values to use when rendering ZONE
        such as a colour.
    :ivar printed_presentation: Presentation values to use in printed
        material for ZONE such as a colour. +v1.1
    """
    class Meta:
        name = "TariffZone_VersionStructure"

    presentation: Optional[PresentationStructure] = field(
        default=None,
        metadata={
            "name": "Presentation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    printed_presentation: Optional[PrintPresentationStructure] = field(
        default=None,
        metadata={
            "name": "PrintedPresentation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
