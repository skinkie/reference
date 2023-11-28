from dataclasses import dataclass, field
from typing import Optional
from netex.derived_view_structure import DerivedViewStructure
from netex.external_object_ref_structure import ExternalObjectRefStructure
from netex.fare_scheduled_stop_point_ref import FareScheduledStopPointRef
from netex.multilingual_string import MultilingualString
from netex.presentation_structure import PresentationStructure
from netex.private_code import PrivateCode
from netex.private_code_structure import PrivateCodeStructure
from netex.scheduled_stop_point_ref import ScheduledStopPointRef
from netex.stop_type_enumeration import StopTypeEnumeration
from netex.type_of_point_ref import TypeOfPointRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ScheduledStopPointDerivedViewStructure(DerivedViewStructure):
    """
    Type for SCHEDULED STOP POINT VIEW.

    :ivar fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref:
    :ivar name: Name of Stop Point.
    :ivar type_of_point_ref:
    :ivar short_name: Short Name of SCHEDULED STOP POINT.
    :ivar name_suffix: Optiona l Suffix for Name of SCHEDULED STOP
        POINT.
    :ivar description: Further description of SCHEDULED STOP POINT.
    :ivar label: Label of SCHEDULED STOP POINT.
    :ivar short_stop_code: An alternative short code that t identifies
        the STOP POINT.
    :ivar public_code: A PUBLIC code that uniquely identifies the STOP
        POINT.
    :ivar private_code:
    :ivar external_stop_point_ref: An alternative  code that uniquely
        identifies the STOP POINT. pecifically for use in AVMS systems
        that require an alias, if. For VDV compatibility.
    :ivar url: URL for SCHEDULED STOP POINT.
    :ivar stop_type: Categorisation of SCHEDULED STOP POINT.
    :ivar compass_bearing: Heading of STOP relative to street. Degrees
        from North. This should be considered as a derived value that
        can be used for presentation purposes when information about the
        physical stop is not available. . The definitive value is the
        compass bearing found on the QUAY (i.e. physical stop) to which
        a SCHEDULED STOP POINT is assigned.
    :ivar presentation: Presentation values to use when rendering STOP
        POINT such as a colour. and font.
    """
    class Meta:
        name = "ScheduledStopPoint_DerivedViewStructure"

    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FareScheduledStopPointRef",
                    "type": FareScheduledStopPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ScheduledStopPointRef",
                    "type": ScheduledStopPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_point_ref: Optional[TypeOfPointRef] = field(
        default=None,
        metadata={
            "name": "TypeOfPointRef",
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
    name_suffix: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "NameSuffix",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    label: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Label",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    short_stop_code: Optional[PrivateCodeStructure] = field(
        default=None,
        metadata={
            "name": "ShortStopCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    public_code: Optional[PrivateCodeStructure] = field(
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
    external_stop_point_ref: Optional[ExternalObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "ExternalStopPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    url: Optional[str] = field(
        default=None,
        metadata={
            "name": "Url",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    stop_type: Optional[StopTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "StopType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    compass_bearing: Optional[float] = field(
        default=None,
        metadata={
            "name": "CompassBearing",
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
