from dataclasses import dataclass, field
from typing import Optional
from netex.alternative_texts_rel_structure import DataManagedObjectStructure
from netex.destination_display_variants_rel_structure import DestinationDisplayVariantsRelStructure
from netex.multilingual_string import MultilingualString
from netex.presentation_structure import PresentationStructure
from netex.private_code import PrivateCode
from netex.vias_rel_structure import ViasRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DestinationDisplayVersionStructure(DataManagedObjectStructure):
    """
    Type for a DESTINATION DISPLAY.

    :ivar name: Name of destination on DESTINATION DISPLAY.
    :ivar short_name: Short Name on DESTINATION DISPLAY.
    :ivar side_text: Name of destination to show on side of VEHICLE.
    :ivar front_text: Name of destination to show on front of VEHICLE.
    :ivar driver_display_text: Text to show to Driver or Staff for the
        DESTINATION DISPLAY.
    :ivar short_code: Short code associated with Destination display
        used vehicle display controller which describes the format of
        the destination text in the front and side display in the
        vehicle. (VDV).
    :ivar public_code: Public code to show for Destination.
    :ivar private_code:
    :ivar presentation: Preferred presentation attributes to use when
        rendering destiation on maps, etc. +v1.1
    :ivar vias: Headings that distinguish the route by which the service
        runs to the Destination  Name .
    :ivar variants: DEITINATION DISPLAY VARIANT for DESTINATION DISPLAY.
        Variants may  be for use in a specifc context or on a specifc
        media, or a combination of both.
    """
    class Meta:
        name = "DestinationDisplay_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    short_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    side_text: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "SideText",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    front_text: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "FrontText",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    driver_display_text: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "DriverDisplayText",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    short_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShortCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    public_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PublicCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    private_code: Optional[PrivateCode] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    presentation: Optional[PresentationStructure] = field(
        default=None,
        metadata={
            "name": "Presentation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vias: Optional[ViasRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    variants: Optional[DestinationDisplayVariantsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
