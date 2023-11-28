from dataclasses import dataclass, field
from typing import List, Optional
from netex.country_ref import CountryRef
from netex.external_object_ref_structure import ExternalObjectRefStructure
from netex.multilingual_string import MultilingualString
from netex.presentation_structure import PresentationStructure
from netex.private_code import PrivateCode
from netex.private_code_structure import PrivateCodeStructure
from netex.request_method_type_enumeration import RequestMethodTypeEnumeration
from netex.stop_area_refs_rel_structure import StopAreaRefsRelStructure
from netex.stop_type_enumeration import StopTypeEnumeration
from netex.tariff_zone_refs_rel_structure import TariffZoneRefsRelStructure
from netex.timing_point_version_structure import TimingPointVersionStructure
from netex.topographic_place_ref import TopographicPlaceRef
from netex.topographic_place_view import TopographicPlaceView
from netex.vehicle_mode_enumeration import VehicleModeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ScheduledStopPointVersionStructure(TimingPointVersionStructure):
    """
    Type for SCHEDULED STOP POINT restricts id.

    :ivar stop_areas: Whether by default a passenger can alight at
        SCHEDULED STOP POINT.
    :ivar tariff_zones: TARIFF ZONEs for SCHEDULED STOP POINT.
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
    :ivar vehicle_modes: TRANSPORT MODE or MODES of STOP POINT.
    :ivar for_alighting: Default for whether SCHEDULED STOP POINT may be
        used for alighting. May be overridden on specific services.
    :ivar for_boarding: Default for whether SCHEDULED STOP POINT may be
        used for boarding. May be overridden on specific services.
    :ivar request_stop: Whether stop is by default a request stop in the
        timetable. May be overridden in specific SERVICE PATTERNs.
    :ivar request_method_type: Method of request stop. Default is
        noneRequired. + v1.1
    :ivar country_ref:
    :ivar topographic_place_ref_or_topographic_place_view:
    :ivar at_centre: Whether STOP POINT can be considered as being at
        the centre of a TOPOGRAPHIC PLACE.  Default is false.
    """
    class Meta:
        name = "ScheduledStopPoint_VersionStructure"

    stop_areas: Optional[StopAreaRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "stopAreas",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    tariff_zones: Optional[TariffZoneRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "tariffZones",
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
    vehicle_modes: List[VehicleModeEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "VehicleModes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    for_alighting: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ForAlighting",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    for_boarding: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ForBoarding",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    request_stop: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RequestStop",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    request_method_type: Optional[RequestMethodTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "RequestMethodType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    country_ref: Optional[CountryRef] = field(
        default=None,
        metadata={
            "name": "CountryRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    topographic_place_ref_or_topographic_place_view: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TopographicPlaceRef",
                    "type": TopographicPlaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TopographicPlaceView",
                    "type": TopographicPlaceView,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    at_centre: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AtCentre",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
