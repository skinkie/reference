import datetime
import math
from _decimal import Decimal
from typing import List, Generator
import os

import duckdb
import numpy
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.models.datatype import XmlDateTime, XmlTime, XmlDate

from callsprofile import CallsProfile
from dbaccess import write_objects, write_generator
from netex import Codespace, DataSource, MultilingualString, Version, VersionFrameDefaultsStructure, \
    VersionTypeEnumeration, LocaleStructure, SystemOfUnits, Operator, ContactStructure, Locale, LanguageUsageStructure, \
    LanguageUseEnumeration, Line, PresentationStructure, AllVehicleModesOfTransportEnumeration, PrivateCode, \
    PublicationDelivery, DataObjectsRelStructure, OperationalContext, ResourceFrame, TypeOfFrameRef, \
    DataSourcesInFrameRelStructure, OrganisationsInFrameRelStructure, OperationalContextsInFrameRelStructure, \
    CompositeFrame, VersionsRelStructure, FramesRelStructure, ServiceFrame, LinesInFrameRelStructure, \
    OperatorRef, StopArea, LocationStructure2, SimplePointVersionStructure, PrivateCodeStructure, \
    ScheduledStopPoint, StopAreaRefsRelStructure, StopAreaRefStructure, \
    StopAreasInFrameRelStructure, ScheduledStopPointsInFrameRelStructure, AvailabilityCondition, ServiceJourneyPattern, \
    DestinationDisplayView, ScheduledStopPointRef, Call, ArrivalStructure, \
    DepartureStructure, CallsRelStructure, ValidityConditionsRelStructure, AvailabilityConditionRef, BlockRef, \
    DirectionTypeEnumeration, AccessibilityAssessment, LimitationStatusEnumeration, TimetableFrame, \
    JourneysInFrameRelStructure, LineRef, JourneyPatternView, CodespacesRelStructure, \
    ServiceJourney, \
    OnwardServiceLinkView, Route, \
    RoutePoint, PointsOnRouteRelStructure, RoutePointRef, PointOnRoute, \
    RouteLink, DayTypesRelStructure, DayType, \
    PropertiesOfDayRelStructure, PropertyOfDay, DayOfWeekEnumeration, Block, ServiceFacilitySetsRelStructure, \
    ServiceFacilitySet, LuggageCarriageEnumeration, LinkSequenceProjection, LinkSequenceProjectionRef, LineString, \
    PosList, CodespaceRefStructure, DataSourceRefStructure, ParticipantRef, LuggageCarriageFacilityList, StopPlace, \
    ZoneRefStructure, InfoLinksRelStructure, InfoLink, TypeOfInfoLinkEnumeration, QuaysRelStructure, \
    SiteEntrancesRelStructure, Quay, StopPlaceEntrance, LevelRef, AccessSpacesRelStructure, AccessSpace, \
    PassengerStopAssignment, ZonesInFrameRelStructure

from refs import getRef, getIndex, getBitString2, getFakeRef, getOptionalString, getId


def get_or_none(l: list, i: int, cast_clazz=None):
    if l is None:
        return l

    if cast_clazz is not None:
        return cast_clazz(l[i])

    return l[i]

def gtfs_date(d: str):
    return datetime.datetime(year=int(str(d)[0:4]), month=int(str(d)[4:6]), day=int(str(d)[6:8]))

def date_to_xmldatetime(d: datetime.date):
    x = datetime.datetime.combine(d, datetime.datetime.min.time())
    return XmlDateTime.from_datetime(x)

class GtfsNeTexProfile(CallsProfile):
    @staticmethod
    def getShortName(name: str):
        if len(name) > 8:
            return ''.join([x[0].upper() for x in name.split(' ')])
        return name

    def getCodespaceAndDataSource(self) -> (Codespace, DataSource, Version, VersionFrameDefaultsStructure):
        feed_info_sql = """select * from feed_info limit 1;"""

        with self.conn.cursor() as cur:
            cur.execute(feed_info_sql)
            df = cur.df()

            short_name = self.getShortName(df['feed_publisher_name'][0])
            codespace_name = short_name.replace(' ', '')

            codespace = Codespace(id="{}:Codespace:{}".format(codespace_name, codespace_name), xmlns=codespace_name,
                                  xmlns_url=df['feed_publisher_url'][0], description=df['feed_publisher_name'][0])

            start_date = datetime.datetime.combine(gtfs_date(df['feed_start_date'][0]), datetime.datetime.min.time())
            end_date = datetime.datetime.combine(gtfs_date(df['feed_end_date'][0]), datetime.datetime.min.time())

            version = Version(id="{}:Version:{}".format(codespace_name, df['feed_version'][0]),
                              version=df['feed_version'][0] if df['feed_version'][0] not in ('', None) else str(datetime.date.today()).replace('-', ''),
                              start_date=XmlDateTime.from_datetime(start_date),
                              end_date=XmlDateTime.from_datetime(end_date),
                              version_type=VersionTypeEnumeration.BASELINE)

            data_source = DataSource(id="{}:DataSource:{}".format(codespace_name, codespace_name),
                                     version=version.version,
                                     name=MultilingualString(value=df['feed_publisher_name'][0]),
                                     short_name=MultilingualString(value=short_name),
                                     description=MultilingualString(value=df['feed_publisher_name'][0]))

            frame_defaults = VersionFrameDefaultsStructure(default_codespace_ref=getRef(codespace, CodespaceRefStructure),
                                                           default_data_source_ref=getRef(data_source, DataSourceRefStructure),
                                                           default_locale=LocaleStructure(default_language=df['feed_lang'][0]),
                                                           default_location_system="EPSG:4326",
                                                           default_system_of_units=SystemOfUnits.SI_METRES
                                                           )

            return (codespace, data_source, version, frame_defaults)

    def getResourceFrame(self, operators, id="ResourceFrame") -> ResourceFrame:
        resource_frame = ResourceFrame(id=getId(ResourceFrame, self.codespace, id), version=self.version.version)
        resource_frame.data_sources = DataSourcesInFrameRelStructure(data_source=[self.data_source])
        # resource_frame.zones = ZonesInFrameRelStructure(transport_administrative_zone=[transport_administrative_zone])
        resource_frame.organisations = OrganisationsInFrameRelStructure(organisation_or_transport_organisation=operators)
        resource_frame.operational_contexts = OperationalContextsInFrameRelStructure(
            operational_context=self.getOperationalContexts())
        # resource_frame.vehicle_types = VehicleTypesInFrameRelStructure(compound_train_or_train_or_vehicle_type=getVehicleTypes(codespace))
        # resource_frame.vehicles = VehiclesInFrameRelStructure(train_element_or_vehicle=getVehicles(codespace))
        return resource_frame

    def getOperators(self, agency_sql = {'query': """select * from agency;"""}) -> list[Operator]:
        results = []

        with self.conn.cursor() as cur:
            cur.execute(**agency_sql)
            df = cur.df()

            agency_ids = df.get('agency_id')
            agency_names = df.get('agency_name')
            agency_timezones = df.get('agency_timezone')
            agency_langs = df.get('agency_lang')
            agency_phones = df.get('agency_phone')
            agency_urls = df.get('agency_url')
            agency_emails = df.get('agency_email')

            for i in range(0, len(agency_ids)):
                operator = Operator(id=getId(Operator, self.codespace, agency_ids[i]),
                                    version=self.version.version,
                                    name=MultilingualString(value=get_or_none(agency_names, i)),
                                    locale=Locale(time_zone=get_or_none(agency_timezones, i),
                                                  languages=LocaleStructure.Languages(language_usage=[LanguageUsageStructure(language=get_or_none(agency_langs, i),
                                                                                                                             language_use=[LanguageUseEnumeration.NORMALLY_USED])]) if get_or_none(agency_langs, i) is not None else None),
                                    customer_service_contact_details=ContactStructure(url=get_or_none(agency_urls, i),
                                                                                      phone=get_or_none(agency_phones, i),
                                                                                      email=get_or_none(agency_emails, i)))
                results.append(operator)

        return results

    @staticmethod
    def gtfsToNeTEx(route_type: int):
        if route_type == 0:
            return AllVehicleModesOfTransportEnumeration.TRAM
        elif route_type == 1:
            return AllVehicleModesOfTransportEnumeration.METRO
        elif route_type == 2:
            return AllVehicleModesOfTransportEnumeration.RAIL
        elif route_type == 3:
            return AllVehicleModesOfTransportEnumeration.BUS
        elif route_type == 4:
            return AllVehicleModesOfTransportEnumeration.WATER
        elif route_type == 5 or route_type == 7:
            return AllVehicleModesOfTransportEnumeration.FUNICULAR
        elif route_type == 6:
            return AllVehicleModesOfTransportEnumeration.CABLEWAY
        elif route_type == 11:
            return AllVehicleModesOfTransportEnumeration.TROLLEY_BUS

        return None

    def getOperationalContexts(self) -> list[OperationalContext]:
        operational_contexts = []

        operational_contexts_sql = """select distinct route_type from routes;"""

        with self.conn.cursor() as cur:
            cur.execute(operational_contexts_sql)
            df = cur.df()

            for i in range(0, len(df['route_type'])):
                operational_context = OperationalContext(
                    id = getId(OperationalContext, self.codespace, df['route_type'][i]),
                    version = self.version.version,
                    vehicle_mode = self.gtfsToNeTEx(df['route_type'][i])
                )
                operational_contexts.append(operational_context)

        return operational_contexts

    def getLines(self) -> list[Line]:
        lines = []

        lines_sql = """select routes.* from routes;"""

        with self.conn.cursor() as cur:
            cur.execute(lines_sql)
            df = cur.df()

            route_ids = df.get('route_id')
            route_text_colors = df.get('route_text_color')
            route_colors = df.get('route_color')
            route_long_names = df.get('route_long_name')
            route_short_names = df.get('route_short_name')
            route_descs = df.get('route_desc')
            route_types = df.get('route_type')
            route_urls = df.get('route_url')
            agency_ids = df.get('agency_id')

            for i in range(0, len(route_ids)):
                presentation = None
                if get_or_none(route_colors, i) is not None or get_or_none(route_text_colors, i) is not None:
                    presentation = PresentationStructure(colour=get_or_none(route_colors, i), text_colour=get_or_none(route_text_colors, i),
                                                         background_colour=get_or_none(route_colors, i))

                agency_id = get_or_none(agency_ids, i)
                operator_ref = None
                if agency_id is not None:
                    operator_ref = getFakeRef(getId(Operator, self.codespace, get_or_none(agency_ids, i)), OperatorRef, self.version.version)

                line = Line(id=getId(Line, self.codespace, get_or_none(route_ids, i)),
                            version=self.version.version,
                            name=MultilingualString(value=get_or_none(route_long_names, i)),
                            short_name=getOptionalString(get_or_none(route_short_names, i)),
                            description=getOptionalString(get_or_none(route_descs, i)),
                            transport_mode=self.gtfsToNeTEx(get_or_none(route_types, i)),
                            presentation=presentation,
                            url=get_or_none(route_urls, i),
                            operator_ref=operator_ref,
                            public_code=get_or_none(route_short_names, i),
                            private_code=PrivateCode(value=get_or_none(route_ids, i), type_value="route_id")
                            )
                lines.append(line)

        return lines

    def getStopAreas(self, stop_area_sql={'query': """select * from stops where location_type = 1 order by stop_id;"""}) -> list[StopArea]:
        stop_areas = []

        with self.conn.cursor() as cur:
            cur.execute(**stop_area_sql)
            df = cur.df()

            stop_ids = df.get('stop_id')
            stop_names = df.get('stop_name')
            stop_lats = df.get('stop_lat')
            stop_lons = df.get('stop_lon')
            stop_codes = df.get('stop_code')
            stop_descs = df.get('stop_desc')
            zone_ids = df.get('zone_id')
            stop_urls = df.get('stop_url')
            location_types = df.get('location_type')
            parent_stations = df.get('parent_station')
            wheelchair_boardings = df.get('wheelchair_boarding')
            stop_timezones = df.get('stop_timezone')
            platform_codes = df.get('platform_code')


            for i in range(0, len(stop_ids)):
                stop_area = StopArea(id=getId(StopArea, self.codespace, stop_ids[i]),
                                     version=self.version.version,
                                     name=MultilingualString(value=stop_names[i]),
                                     public_code=get_or_none(stop_codes, i),
                                     description=getOptionalString(get_or_none(stop_descs, i)),
                                     private_code=PrivateCode(value=stop_ids[i], type_value="stop_id"),
                                     centroid=SimplePointVersionStructure(location=
                                                                          LocationStructure2(latitude=Decimal(str(stop_lats[i])),
                                                                                             longitude=Decimal(str(stop_lons[i])),
                                                                                             srs_name="EPSG:4326")),
                                     )
                stop_areas.append(stop_area)

        return stop_areas

    def getScheduledStopPoints(self, stop_areas, scheduled_stop_points_sql={'query': """select * from stops where location_type = 0 or location_type is null order by stop_id;"""}) -> list[ScheduledStopPoint]:
        stop_areas = getIndex(stop_areas)

        scheduled_stop_points = []
        passenger_stop_assignments = []

        with self.conn.cursor() as cur:
            cur.execute(**scheduled_stop_points_sql)
            df = cur.df()

            stop_ids = df.get('stop_id')
            stop_names = df.get('stop_name')
            stop_lats = df.get('stop_lat')
            stop_lons = df.get('stop_lon')
            stop_codes = df.get('stop_code')
            stop_descs = df.get('stop_desc')
            zone_ids = df.get('zone_id')
            stop_urls = df.get('stop_url')
            location_types = df.get('location_type')
            parent_stations = df.get('parent_station')
            wheelchair_boardings = df.get('wheelchair_boarding')
            stop_timezones = df.get('stop_timezone')
            platform_codes = df.get('platform_code')


            for i in range(0, len(stop_ids)):
                short_stop_code = None
                platform_code = get_or_none(platform_codes, i)
                if platform_code is not None:
                    short_stop_code = PrivateCodeStructure(value=platform_code, type_value='platform_code')

                location = LocationStructure2(longitude=Decimal(str(stop_lons[i])) if stop_lons[i] is not None else None,
                                              latitude=Decimal(str(stop_lats[i])) if stop_lats[i] is not None else None,
                                              srs_name="EPSG:4326")

                my_stop_areas = None
                parent_station = get_or_none(parent_stations, i)
                if parent_station is not None:
                    stop_area_ref = getId(StopArea, self.codespace, parent_station)
                    my_stop_areas = StopAreaRefsRelStructure(stop_area_ref=[
                        getRef(stop_areas[stop_area_ref], StopAreaRefStructure)])


                scheduled_stop_point = ScheduledStopPoint(id=getId(ScheduledStopPoint, self.codespace, stop_ids[i]),
                                                          version=self.version.version,
                                                          name=MultilingualString(value=stop_names[i]),
                                                          description=getOptionalString(get_or_none(stop_descs, i)),
                                                          private_code=PrivateCode(value=stop_ids[i], type_value="stop_id"),
                                                          short_stop_code=short_stop_code,
                                                          public_code=get_or_none(stop_codes, i),
                                                          url=get_or_none(stop_urls, i),
                                                          location=location,
                                                          stop_areas=my_stop_areas)
                scheduled_stop_points.append(scheduled_stop_point)

                """
                stop_place_ref = None
                if row['stopplacecoderef'] is not None:
                    stop_place_ref = getFakeRef(row['stopplacecoderef'], StopPlaceRef, "any")

                quay_ref = None
                if row['quaycoderef'] is not None:
                    quay_ref = getFakeRef(row['quaycoderef'], QuayRef, "any")

                if stop_place_ref is not None or quay_ref is not None:
                    passenger_stop_assignment = PassengerStopAssignment(
                        scheduled_stop_point_ref=getRef(scheduled_stop_point, ScheduledStopPointRef),
                        stop_place_ref=stop_place_ref,
                        quay_ref=quay_ref, order=1)
                    setIdVersion(passenger_stop_assignment, codespace, row['id'], version)
                    passenger_stop_assignments.append(passenger_stop_assignment)
                """

        return scheduled_stop_points

    # TODO: implement
    def getStopPlaces(self, stop_places_sql={'query': """select * from stops order by parent_station, stop_id;"""}) -> (List[StopPlace], List[PassengerStopAssignment]):
        stop_places = {}
        passenger_stop_assignments = []
        with self.conn.cursor() as cur:
            cur.execute(**stop_places_sql)
            df = cur.df()

            stop_ids = df.get('stop_id')
            stop_names = df.get('stop_name')
            stop_lats = df.get('stop_lat')
            stop_lons = df.get('stop_lon')
            stop_codes = df.get('stop_code')
            stop_descs = df.get('stop_desc')
            zone_ids = df.get('zone_id')
            stop_urls = df.get('stop_url')
            location_types = df.get('location_type')
            parent_stations = df.get('parent_station')
            wheelchair_boardings = df.get('wheelchair_boarding')
            stop_timezones = df.get('stop_timezone')
            platform_codes = df.get('platform_code')
            level_ids = df.get('level_id')

            for i in range(0, len(stop_ids)):
                # Every stop that does not have a parent_station, will become a StopPlace
                if parent_stations[i] is None:
                    stop_place = StopPlace(id=getId(StopPlace, self.codespace, stop_ids[i]),
                                           version=self.version.version,
                                           name=MultilingualString(value=stop_names[i]),
                                           public_code=get_or_none(stop_codes, i),
                                           description=getOptionalString(get_or_none(stop_descs, i)),
                                           private_code=PrivateCode(value=stop_ids[i], type_value="stop_id"),
                                           locale=Locale(time_zone=stop_timezones[i]) if stop_timezones[i] is not None else None,
                                           parent_zone_ref=ZoneRefStructure(ref=zone_ids[i], version_ref="EXTERNAL") if zone_ids[i] is not None else None,
                                           accessibility_assessment=AccessibilityAssessment(id=getId(AccessibilityAssessment, self.codespace, 'StopPlace_' + stop_ids[i]),
                                                                                            version=self.version.version,
                                                                                            mobility_impaired_access=self.wheelchairToNeTEx(wheelchair_boardings[i])) if wheelchair_boardings[i] is not None else None,
                                           info_links=InfoLinksRelStructure(info_link=[InfoLink(type_of_info_link=[TypeOfInfoLinkEnumeration.RESOURCE], value=stop_urls[i])]) if stop_urls[i] is not None else None,
                                           centroid=SimplePointVersionStructure(location=
                                                                              LocationStructure2(latitude=Decimal(str(stop_lats[i])),
                                                                                                 longitude=Decimal(str(stop_lons[i])),
                                                                                                 srs_name="EPSG:4326")),
                                           )
                    stop_places[stop_place.id] = stop_place
                else:
                    stop_place = stop_places[getId(StopPlace, self.codespace, parent_stations[i])]

                if location_types[i] == 1:
                    # Nothing to do, we already created the StopPlace
                    continue

                if location_types[i] != location_types[i] or location_types[i] == 0 or location_types[i] == 4:
                    # Stop or Platform or BoardingArea, to Quay
                    if stop_place.quays is None:
                        stop_place.quays = QuaysRelStructure()

                    quay = Quay(id=getId(Quay, self.codespace, stop_ids[i]),
                                version=self.version.version,
                                name=MultilingualString(value=stop_names[i]),
                                public_code=get_or_none(stop_codes, i),
                                description=getOptionalString(get_or_none(stop_descs, i)),
                                private_code=PrivateCode(value=stop_ids[i], type_value="stop_id"),
                                parent_zone_ref=ZoneRefStructure(ref=zone_ids[i], version_ref="EXTERNAL") if zone_ids[i] is not None else None,
                                accessibility_assessment=AccessibilityAssessment(id=getId(AccessibilityAssessment, self.codespace, stop_ids[i]), version=self.version.version,
                                                                                 mobility_impaired_access=self.wheelchairToNeTEx(wheelchair_boardings[i])) if wheelchair_boardings[i] is not None else None,
                                info_links=InfoLinksRelStructure(info_link=[InfoLink(type_of_info_link=[TypeOfInfoLinkEnumeration.RESOURCE], value=stop_urls[i])]) if stop_urls[i] is not None else None,
                                centroid=SimplePointVersionStructure(location=
                                                                     LocationStructure2(
                                                                         latitude=Decimal(str(stop_lats[i])),
                                                                         longitude=Decimal(str(stop_lons[i])),
                                                                         srs_name="EPSG:4326")),
                                level_ref=LevelRef(ref=level_ids[0], version=self.version.version) if level_ids[i] is not None else None,
                                )

                    stop_place.quays.taxi_stand_ref_or_quay_ref_or_quay.append(quay)

                    passenger_stop_assignment = PassengerStopAssignment(id=getId(PassengerStopAssignment, self.codespace, stop_ids[i]),
                                                                        version=self.version.version,
                                                                        order=1,
                                                                        fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point=getFakeRef(getId(ScheduledStopPoint, self.codespace, stop_ids[i]), ScheduledStopPointRef, self.version.version),
                                                                        taxi_stand_ref_or_quay_ref_or_quay=getRef(quay))
                    passenger_stop_assignments.append(passenger_stop_assignment)

                elif location_types[i] == 2:
                    # Entrance or Exit
                    if stop_place.entrances is None:
                        stop_place.entrances = SiteEntrancesRelStructure()

                    stop_place_entrance = StopPlaceEntrance(id=getId(StopPlaceEntrance, self.codespace, stop_ids[i]),
                                           version=self.version.version,
                                           name=MultilingualString(value=stop_names[i]),
                                           public_code=get_or_none(stop_codes, i),
                                           description=getOptionalString(get_or_none(stop_descs, i)),
                                           private_code=PrivateCode(value=stop_ids[i], type_value="stop_id"),
                                           parent_zone_ref=ZoneRefStructure(ref=zone_ids[i], version_ref="EXTERNAL") if zone_ids[i] is not None else None,
                                           accessibility_assessment=AccessibilityAssessment(id=getId(AccessibilityAssessment, self.codespace, stop_ids[i]),
                                                                                            version=self.version.version,
                                                                                            mobility_impaired_access=self.wheelchairToNeTEx(wheelchair_boardings[i])) if wheelchair_boardings[i] is not None else None,
                                           info_links=InfoLinksRelStructure(info_link=[InfoLink(type_of_info_link=[TypeOfInfoLinkEnumeration.RESOURCE], value=stop_urls[i])]) if stop_urls[i] is not None else None,
                                           centroid=SimplePointVersionStructure(location=
                                                                              LocationStructure2(latitude=Decimal(str(stop_lats[i])),
                                                                                                 longitude=Decimal(str(stop_lons[i])),
                                                                                                 srs_name="EPSG:4326")),
                                           level_ref=LevelRef(ref=level_ids[0], version=self.version.version) if level_ids[i] is not None else None,
                                           )

                    stop_place.entrances.parking_entrance_ref_or_entrance_ref_or_entrance.append(stop_place_entrance)

                elif location_types[i] == 3:
                    # Generic Node
                    if stop_place.access_spaces is None:
                        stop_place.access_spaces = AccessSpacesRelStructure()

                    access_space = AccessSpace(id=getId(AccessSpace, self.codespace, stop_ids[i]),
                                           version=self.version.version,
                                           name=MultilingualString(value=stop_names[i]),
                                           description=getOptionalString(get_or_none(stop_descs, i)),
                                           private_code=PrivateCode(value=stop_ids[i], type_value="stop_id"),
                                           parent_zone_ref=ZoneRefStructure(ref=zone_ids[i], version_ref="EXTERNAL") if zone_ids[i] is not None else None,
                                           accessibility_assessment=AccessibilityAssessment(id=getId(AccessibilityAssessment, self.codespace, stop_ids[i]),
                                                                                            version=self.version.version,
                                                                                            mobility_impaired_access=self.wheelchairToNeTEx(wheelchair_boardings[i])) if wheelchair_boardings[i] is not None else None,
                                           info_links=InfoLinksRelStructure(info_link=[InfoLink(type_of_info_link=[TypeOfInfoLinkEnumeration.RESOURCE], value=stop_urls[i])]) if stop_urls[i] is not None else None,
                                           centroid=SimplePointVersionStructure(location=
                                                                              LocationStructure2(latitude=Decimal(str(stop_lats[i])),
                                                                                                 longitude=Decimal(str(stop_lons[i])),
                                                                                                 srs_name="EPSG:4326")),
                                           level_ref=LevelRef(ref=level_ids[0], version=self.version.version) if level_ids[i] is not None else None,
                                           )

                    stop_place.access_spaces.access_space_ref_or_access_space.append(access_space)

        return list(stop_places.values()), passenger_stop_assignments

    #
    # def getPaths(self):
    #     pl = PathLink()
    #
    #
    def getRoutes(self) -> (list[Route], list[RoutePoint], list[RouteLink]):
        lines = getIndex(self.lines)

        shape_route_mapping = {}

        # Within NeTEx it is not possible to have a route (GTFS-shape) pointing to multiple lines (GTFS-route)
        shape_route_sql = """select distinct shape_id, array_agg(distinct route_id) as route_ids from trips where shape_id is not null group by shape_id;""";
        with self.conn.cursor() as cur:
            cur.execute(shape_route_sql)

            df = cur.df()
            shape_ids = df.get('shape_id')
            route_ids = df.get('route_ids')

            for i in range(0, len(shape_ids)):
                if len(route_ids[i]) > 0:
                    shape_route_mapping[shape_ids[i]] = [(shape_ids[i] + '-' + x, x) for x in route_ids[i]]
                else:
                    # Stale route, why should we add them at all?
                    shape_route_mapping[shape_ids[i]] = [(shape_ids[i], None,)]

        shape_sql = """select shape_id, shape_pt_lat, shape_pt_lon, shape_pt_sequence, shape_dist_traveled from shapes order by shape_id, shape_pt_sequence, shape_dist_traveled;"""

        routes = {}
        route_points = []
        route_links = []

        with self.conn.cursor() as cur:
            cur.execute(shape_sql)

            df = cur.df()
            shape_ids = df.get('shape_id')
            shape_pt_lats = df.get('shape_pt_lat')
            shape_pt_lons = df.get('shape_pt_lon')
            shape_pt_sequences = df.get('shape_pt_sequence')
            shape_dist_traveleds = df.get('shape_dist_traveled')

            prev_order = 1
            prev_route = None
            prev_distance = 0
            prev_route_point = None
            prev_shape_id = None

            for i in range(0, len(shape_ids)):
                route_point = RoutePoint(
                    id=getId(RoutePoint, self.codespace, "{}-{}".format(shape_ids[i], shape_pt_sequences[i])),
                    version=self.version.version,
                    location=LocationStructure2(longitude=Decimal(str(shape_pt_lons[i])),
                                                latitude=Decimal(str(shape_pt_lats[i])),
                                                srs_name="EPSG:4326"))
                route_points.append(route_point)

                if shape_ids[i] == prev_shape_id:
                    # It is the same route, and still being extended
                    distance = None
                    if shape_dist_traveleds[i]:
                        distance = shape_dist_traveleds[i] - prev_distance

                    route_link = RouteLink(id=getId(RouteLink, self.codespace, "{}-{}".format(shape_ids[i], shape_pt_sequences[i])),
                                           version=self.version.version,
                                           from_point_ref=getRef(prev_route_point),
                                           to_point_ref=getRef(route_point),
                                           distance=Decimal(str(distance)))
                    route_links.append(route_link)

                    for route in prev_route:
                        route.points_in_sequence.point_on_route[-1].onward_route_link_ref = getRef(route_link)

                else:
                    prew_order = 1
                    prev_route = []
                    prev_distance = 0
                    prev_route_point = None
                    prev_shape_id = None

                    route_ids = shape_route_mapping.get(shape_ids[i], [(shape_ids[i], None)])
                    for route_id, line_id in route_ids:
                        route = Route(id=getId(Route, self.codespace, route_id), version=self.version.version)
                        route.private_code = PrivateCode(value = shape_ids[i], type_value = "shape_id")
                        route.points_in_sequence = PointsOnRouteRelStructure()
                        if line_id:
                            line = lines[getId(Line, self.codespace, line_id)]
                            route.line_ref = getRef(line, LineRef)

                        routes[route_id] = route
                        prev_route.append(route)

                for route in prev_route:
                    point_on_route = PointOnRoute(id=getId(PointOnRoute, self.codespace, "{}-{}".format(route_id, shape_pt_sequences[i])), version=self.version.version, order=prev_order, point_ref_or_infrastructure_point_ref_or_activation_point_ref_or_timing_point_ref_or_scheduled_stop_point_ref_or_parking_point_ref_or_relief_point_ref_or_route_point_ref=getRef(route_point, RoutePointRef)) # shape_pt_sequence is non-negative integer
                    route.points_in_sequence.point_on_route.append(point_on_route)

                prev_shape_id = shape_ids[i]
                prev_route_point = route_point
                prev_distance = shape_dist_traveleds[i]
                prev_order += 1

        return (list(routes.values()), route_points, route_links)

    def getLineStrings(self, shape_sql = {'query': """select shape_id, shape_pt_lat, shape_pt_lon, shape_pt_sequence, shape_dist_traveled from shapes order by shape_id, shape_pt_sequence, shape_dist_traveled;"""}) -> List[LinkSequenceProjection]:
        link_sequence_projection = []

        with self.conn.cursor() as cur:
            cur.execute(**shape_sql)

            df = cur.df()
            shape_ids = df.get('shape_id')
            shape_pt_lats = df.get('shape_pt_lat')
            shape_pt_lons = df.get('shape_pt_lon')
            # shape_pt_sequences = df.get('shape_pt_sequence')
            shape_dist_traveleds = df.get('shape_dist_traveled')

            prev_distance = 0
            prev_shape_id = None
            pos_list = []

            for i in range(0, len(shape_ids)):
                if shape_ids[i] != prev_shape_id and prev_shape_id is not None:
                    de_distance = None
                    if prev_distance is not None and not numpy.isnan(prev_distance):
                        de_distance = Decimal(prev_distance)

                    link_sequence_projection.append(LinkSequenceProjection(id=getId(LinkSequenceProjection, self.codespace, prev_shape_id), version=self.version.version,
                                                                           distance=de_distance, points_or_line_string=LineString(id=prev_shape_id, srs_name="EPSG:4326", srs_dimension=2, pos_or_point_property_or_pos_list=[PosList(value=pos_list)])))
                    pos_list = []
                    prev_distance = 0

                pos_list += [Decimal(str(shape_pt_lats[i])), Decimal(str(shape_pt_lons[i]))]

                prev_shape_id = shape_ids[i]
                prev_distance = get_or_none(shape_dist_traveleds, i)

            if len(pos_list) > 0:
                de_distance = None
                if prev_distance is not None and not numpy.isnan(prev_distance):
                    de_distance = Decimal(str(prev_distance))

                link_sequence_projection.append(
                    LinkSequenceProjection(id=getId(LinkSequenceProjection, self.codespace, prev_shape_id),
                                           version=self.version.version, distance=de_distance,
                                           points_or_line_string=LineString(id=getId(LinkSequenceProjection, self.codespace, prev_shape_id).replace(":", "_"), srs_name="EPSG:4326",
                                                                            srs_dimension=2,
                                                                            pos_or_point_property_or_pos_list=[
                                                                                PosList(value=pos_list)])))

        return link_sequence_projection


    def getServiceFrame(self, lines, stop_areas, scheduled_stop_points, id="ServiceFrame") -> ServiceFrame:
        if lines is None:
            lines = self.lines

        if stop_areas is None:
            stop_areas = self.stop_areas

        if scheduled_stop_points is None:
            scheduled_stop_points = self.scheduled_stop_points

        service_frame = ServiceFrame(id=getId(ServiceFrame, self.codespace, id), version=self.version.version)
        # service_frame.prerequisites.resource_frame_ref
        # setIdVersion(service_frame, self.codespace, "ServiceFrame", self.version)
        service_frame.lines = LinesInFrameRelStructure(line=lines)

        stop_areas = sorted(stop_areas, key=lambda x: x.id)
        if stop_areas:
            service_frame.stop_areas = StopAreasInFrameRelStructure(stop_area=stop_areas)

        scheduled_stop_points = sorted(scheduled_stop_points, key=lambda x: x.id)
        service_frame.scheduled_stop_points = ScheduledStopPointsInFrameRelStructure(scheduled_stop_point=scheduled_stop_points)

    #     """
    #     destination_displays = getDestinationDisplays(codespace, version)
    #     stop_areas = getStopAreas(codespace, version)
    #     scheduled_stop_points, passenger_stop_assignments = getScheduledStopPoints(codespace, version, route_points,
    #                                                                                stop_areas)
    #     service_journey_patterns, timing_links, service_journey_patterns_transport_mode = getServiceJourneyPatterns(
    #         codespace, version, routes, lines, scheduled_stop_points, operational_contexts, destination_displays)
    #
    #     service_journey_patterns = sorted(service_journey_patterns, key=lambda x: x.id)
    #     timing_links = sorted(timing_links, key=lambda x: x.id)
    #     """
    #
    #     self.stop_areas = sorted(self.stop_areas, key=lambda x: x.id)
    #     self.scheduled_stop_points = sorted(self.scheduled_stop_points, key=lambda x: x.id)
    #
    #     """
    #     destination_displays = sorted(destination_displays, key=lambda x: x.id)
    #     passenger_stop_assignments = sorted(passenger_stop_assignments, key=lambda x: x.id)
    #
    #     """
    #     self.route_points = sorted(self.route_points, key=lambda x: x.id)
    #     service_frame.route_points = RoutePointsInFrameRelStructure(route_point=self.route_points)
    #
    #     self.route_links = sorted(self.route_links, key=lambda x: x.id)
    #     service_frame.route_links = RouteLinksInFrameRelStructure(route_link=self.route_links)
    #
    #    self.routes = sorted(self.routes, key=lambda x: x.id)
    #    service_frame.routes = RoutesInFrameRelStructure(route=self.routes)
    #
    #     if self.stop_areas:
    #         service_frame.stop_areas = StopAreasInFrameRelStructure(stop_area=self.stop_areas)
    #
    #     service_frame.scheduled_stop_points = ScheduledStopPointsInFrameRelStructure(
    #         scheduled_stop_point=self.scheduled_stop_points)
    #
    #     if self.timing_links:
    #         service_frame.timing_links = TimingLinksInFrameRelStructure(timing_link=self.timing_links)
    #
    #     if self.time_demand_types:
    #         self.time_demand_types = sorted(self.time_demand_types, key=lambda x: x.id)
    #         service_frame.time_demand_types = TimeDemandTypesInFrameRelStructure(time_demand_type=self.time_demand_types)
    #
    #     """
    #     service_frame.destination_displays = DestinationDisplaysInFrameRelStructure(
    #         destination_display=destination_displays)
    #     service_frame.stop_assignments = StopAssignmentsInFrameRelStructure(
    #         passenger_stop_assignment=passenger_stop_assignments)
    #     """
    #
    #     if self.service_journey_patterns:
    #         service_frame.journey_patterns = JourneyPatternsInFrameRelStructure(choice=self.service_journey_patterns)
    #
    #
        return service_frame


    def getAvailabilityConditions(self, availability_condition_sql={'query': """select * from calendar order by service_id;"""}, exceptions_sql={'query': """select service_id, exception_type, array_agg(date order by date) as dates from calendar_dates group by service_id, exception_type;"""}) -> list[AvailabilityCondition]:
        availability_conditions = []

        with self.conn.cursor() as cur:
            cur.execute(**exceptions_sql)
            exceptions_df = cur.df()
            exceptions = {}

            service_ids = exceptions_df.get('service_id')
            for i in range(0, len(service_ids)):
                exception_type = int(exceptions_df['exception_type'][i])
                if exception_type in (1, 2):
                    ac = AvailabilityCondition(id = getId(AvailabilityCondition, self.codespace, service_ids[i] + '_' + str(exception_type)),
                                               version=self.version.version, is_available=exception_type == 1,
                                               from_date=date_to_xmldatetime(gtfs_date(exceptions_df['dates'][i][0])),
                                               to_date=date_to_xmldatetime(gtfs_date(exceptions_df['dates'][i][-1])),
                                               valid_day_bits=getBitString2([gtfs_date(d) for d in exceptions_df['dates'][i]]))
                    l = exceptions.get(service_ids[i], [])
                    l.append(ac)
                    exceptions[service_ids[i]] = l
                    availability_conditions.append(ac)

            cur.execute(**availability_condition_sql)
            df = cur.df()

            service_ids = df.get('service_id')
            mondays = df.get('monday')
            tuesdays = df.get('tuesday')
            wednesdays = df.get('wednesday')
            thursdays = df.get('thursday')
            fridays = df.get('friday')
            saturdays = df.get('saturday')
            sundays = df.get('sunday')
            start_dates = df.get('start_date')
            end_dates = df.get('end_date')

            for i in range(0, len(service_ids)):
                days_of_week = []
                if mondays[i] == 1:
                    days_of_week.append(DayOfWeekEnumeration.MONDAY)
                if tuesdays[i] == 1:
                    days_of_week.append(DayOfWeekEnumeration.TUESDAY)
                if wednesdays[i] == 1:
                    days_of_week.append(DayOfWeekEnumeration.WEDNESDAY)
                if thursdays[i] == 1:
                    days_of_week.append(DayOfWeekEnumeration.THURSDAY)
                if fridays[i] == 1:
                    days_of_week.append(DayOfWeekEnumeration.FRIDAY)
                if saturdays[i] == 1:
                    days_of_week.append(DayOfWeekEnumeration.SATURDAY)
                if sundays[i] == 1:
                    days_of_week.append(DayOfWeekEnumeration.SUNDAY)

                availability_conditions.append(AvailabilityCondition(id=getId(AvailabilityCondition, self.codespace, service_ids[i]), version=self.version.version,
                                                                     is_available=True,
                                                                     from_date=date_to_xmldatetime(gtfs_date(start_dates[i])), to_date=date_to_xmldatetime(gtfs_date(end_dates[i])),
                                                                     day_types=DayTypesRelStructure(day_type_ref_or_day_type=[DayType(id=getId(DayType, self.codespace, service_ids[i]), version=self.version.version,
                                                                                                                    properties=PropertiesOfDayRelStructure(property_of_day=[PropertyOfDay(tides=None, weeks_of_month=None, holiday_types=None, seasons=None, days_of_week=days_of_week)]))])))

        return availability_conditions

    @staticmethod
    def noonTimeToNeTEx(time: str):
        hour, minute, second = time.split(':')
        hour = int(hour)
        day_offset = int(math.floor(hour / 24))
        return (XmlTime(hour=hour % 24, minute=int(minute), second=int(second)), day_offset)

    @staticmethod
    def directionToNeTEx(direction_id: int):
        if direction_id is None:
            return None

        elif direction_id == 1:
            return DirectionTypeEnumeration.INBOUND

        return DirectionTypeEnumeration.OUTBOUND

    @staticmethod
    def wheelchairToNeTEx(wheelchair_accessible: int):
        if wheelchair_accessible == 1:
            return LimitationStatusEnumeration.TRUE

        elif wheelchair_accessible == 2:
            return LimitationStatusEnumeration.FALSE

        return LimitationStatusEnumeration.UNKNOWN

    @staticmethod
    def bicyclesToNeTEx(bikes_allowed: int):
        if bikes_allowed == 1:
            return LuggageCarriageEnumeration.TRUE

        elif bikes_allowed == 2:
            return LuggageCarriageEnumeration.FALSE

        return LuggageCarriageEnumeration.UNKNOWN

    def gtfs_shape_to_linestring(self, shape_sql={'query': """select * from shapes order by shape_id;"""}):

        with self.conn.cursor() as cur:
            cur.execute(**shape_sql)

    def getServiceJourneys(self, availability_conditions, trips_sql={'query': """select * from trips order by trip_id;"""}, stop_times_sql = {'query': """select * from stop_times order by trip_id, stop_sequence;"""}) -> Generator[ServiceJourney, None, None]:
        availability_conditions = getIndex(availability_conditions)

        service_journeys = {}
        shape_used = set([])

        with self.conn.cursor() as cur:
            cur.execute(**trips_sql)

            df = cur.df()

            route_ids = df.get('route_id')
            trip_ids = df.get('trip_id')
            service_ids = df.get('service_id')
            trip_short_names = df.get('trip_short_name')
            trip_headsigns = df.get('trip_headsign')
            # route_short_names = df.get('route_short_name')
            direction_ids = df.get('direction_id')
            block_ids = df.get('block_id')
            shape_ids = df.get('shape_id')
            wheelchair_accessibles = df.get('wheelchair_accessible')
            # trip_bikes_alloweds = df.get('trip_bikes_allowed')
            bikes_alloweds = df.get('bikes_allowed')
            ticketing_trip_ids = df.get('ticketing_trip_id')
            ticketing_types = df.get('ticketing_type')

            for i in range(0, len(route_ids)):
                availability_condition_key = getId(AvailabilityCondition, self.codespace, service_ids[i])

                availability_conditions_journey = [availability_conditions.get(availability_condition_key, None),
                                                   availability_conditions.get(availability_condition_key + "_1", None),
                                                   availability_conditions.get(availability_condition_key + "_2", None)]

                journey_pattern_view = None
                if trip_headsigns[i] is not None:
                    journey_pattern_view = JourneyPatternView(
                        destination_display_ref_or_destination_display_view=DestinationDisplayView(
                            name=MultilingualString(value=trip_headsigns[i]), front_text=MultilingualString(value=trip_headsigns[i])))

                accessibility_assessment = None
                if wheelchair_accessibles is not None and wheelchair_accessibles[i] is not None:
                    accessibility_assessment = AccessibilityAssessment(id=getId(AccessibilityAssessment, self.codespace, trip_ids[i]),
                                                                       version=self.version.version,
                                                                       mobility_impaired_access=self.wheelchairToNeTEx(wheelchair_accessibles[i]))

                block_ref = None
                if block_ids[i] is not None:
                    block_ref = getFakeRef(getId(Block, self.codespace, block_ids[i]), BlockRef, None)

                route_ref = None
                lsp = None
                shape_id = get_or_none(shape_ids, i)
                if shape_id is not None:
                    if shape_id in shape_used:
                        lsp = getFakeRef(getId(LinkSequenceProjection, self.codespace, shape_id), LinkSequenceProjectionRef, self.version.version)
                    else:
                        lsps = self.getLineStrings({'query': """select shape_id, shape_pt_lat, shape_pt_lon, shape_pt_sequence, shape_dist_traveled from shapes where shape_id = ? order by shape_id, shape_pt_sequence, shape_dist_traveled;""", 'parameters': (shape_id,)})
                        if len(lsps) > 0:
                            lsp = lsps[0]

                        shape_used.add(shape_id)

                luggage_carriage_facility_list = []
                facitities = None
                bikes_allowed = get_or_none(bikes_alloweds, i)
                if bikes_allowed is not None:
                    if bikes_allowed == 1:
                        luggage_carriage_facility_list.append(LuggageCarriageEnumeration.CYCLES_ALLOWED)
                    elif bikes_allowed == 2:
                        luggage_carriage_facility_list.append(LuggageCarriageEnumeration.NO_CYCLES)

                if len(luggage_carriage_facility_list) > 0:
                    facitities = ServiceFacilitySetsRelStructure(
                            service_facility_set_ref_or_service_facility_set=[ServiceFacilitySet(
                                id=getId(ServiceFacilitySet, self.codespace, trip_ids[i]), version=self.version.version,
                                luggage_carriage_facility_list=LuggageCarriageFacilityList(value=luggage_carriage_facility_list))])

                service_journey = ServiceJourney(id=getId(ServiceJourney, self.codespace, trip_ids[i]),
                                                 version=self.version.version,
                                                 flexible_line_ref_or_line_ref_or_line_view_or_flexible_line_view=getFakeRef(getId(Line, self.codespace, route_ids[i]), LineRef, self.version.version),
                                                 private_code=PrivateCode(value=trip_ids[i], type_value="trip_id"),
                                                 short_name=getOptionalString(get_or_none(trip_short_names, i)),
                                                 validity_conditions_or_valid_between=[ValidityConditionsRelStructure(choice=[getRef(x, AvailabilityConditionRef) for x in availability_conditions_journey if x is not None])],
                                                 journey_pattern_view=journey_pattern_view,
                                                 direction_type=self.directionToNeTEx(get_or_none(direction_ids, i)),
                                                 block_ref=block_ref,
                                                 accessibility_assessment=accessibility_assessment,
                                                 facilities=facitities,
                                                 link_sequence_projection_ref_or_link_sequence_projection=lsp
                                                 )

                service_journeys[trip_ids[i]] = service_journey

        with self.conn.cursor() as cur:
            cur.execute(**stop_times_sql)
            trip_id = None
            service_journey = None
            prev_call = None
            prev_shape_traveled = 0
            prev_order = 1

            df = cur.df()

            trip_ids = df.get('trip_id')
            stop_headsigns = df.get('stop_headsign')
            stop_ids = df.get('stop_id')
            arrival_times = df.get('arrival_time')
            departure_times = df.get('departure_time')
            shape_dist_traveleds = df.get('shape_dist_traveled')
            drop_off_types = df.get('drop_off_type')
            pickup_types = df.get('pickup_type')
            stop_sequences = df.get('stop_sequence')


            for i in range(0, len(trip_ids)):
                if trip_ids[i] != trip_id:
                    if trip_id is not None:
                        yield service_journey
                        service_journey.calls = None # Free memory

                    trip_id = trip_ids[i]
                    service_journey = service_journeys[trip_id]
                    service_journey.calls = CallsRelStructure()
                    prev_call = None
                    prev_shape_traveled = 0
                    prev_order = 1

                destination_display_view = None
                stop_headsign = get_or_none(stop_headsigns, i)
                if stop_headsign is not None:
                    destination_display_view = DestinationDisplayView(name=MultilingualString(value=stop_headsign),
                                                                      front_text=MultilingualString(value=stop_headsign))

                from_point_ref = getId(ScheduledStopPoint, self.codespace, stop_ids[i])
                arrival_time, arrival_dayoffset = self.noonTimeToNeTEx(arrival_times[i])
                departure_time, departure_dayoffset = self.noonTimeToNeTEx(departure_times[i])

                shape_dist_traveled = get_or_none(shape_dist_traveleds, i)
                if prev_call and shape_dist_traveled:
                    distance = shape_dist_traveled - prev_shape_traveled
                    prev_call.onward_service_link_view = OnwardServiceLinkView(distance=distance)

                call = Call(id=getId(Call, self.codespace, "{}_{}".format(trip_ids[i], stop_sequences[i])), version=self.version.version,
                             fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=getFakeRef(from_point_ref, ScheduledStopPointRef, self.version.version),
                             destination_display_ref_or_destination_display_view=destination_display_view,
                             arrival=ArrivalStructure(time=arrival_time, day_offset=arrival_dayoffset,
                                                      for_alighting=bool(drop_off_types[i] != 1)),
                             departure=DepartureStructure(time=departure_time, day_offset=departure_dayoffset,
                                                      for_boarding=bool(pickup_types[i] != 1)),
                             request_stop=bool(pickup_types[i] == 2 or pickup_types[i] == 3 or drop_off_types[i] == 2 or drop_off_types[i] == 3),
                             order=prev_order) # stop_sequence is non-negative integer

                service_journey.calls.call.append(call)

                prev_call = call
                prev_shape_traveled = shape_dist_traveled
                prev_order += 1

            if trip_id is not None:
                yield service_journey


    def getServiceJourneys2(self, availability_conditions, trips_sql={'query': """select * from trips order by trip_id;"""}) -> Generator[ServiceJourney, None, None]:
        availability_conditions = getIndex(availability_conditions)

        shape_used = set([])

        with self.conn.cursor() as cur:
            cur.execute(**trips_sql)

            df = cur.df()

            route_ids = df.get('route_id')
            trip_ids = df.get('trip_id')
            service_ids = df.get('service_id')
            trip_short_names = df.get('trip_short_name')
            trip_headsigns = df.get('trip_headsign')
            # route_short_names = df.get('route_short_name')
            direction_ids = df.get('direction_id')
            block_ids = df.get('block_id')
            shape_ids = df.get('shape_id')
            wheelchair_accessibles = df.get('wheelchair_accessible')
            # trip_bikes_alloweds = df.get('trip_bikes_allowed')
            bikes_alloweds = df.get('bikes_allowed')
            ticketing_trip_ids = df.get('ticketing_trip_id')
            ticketing_types = df.get('ticketing_type')

            for i in range(0, len(route_ids)):
                availability_condition_key = getId(AvailabilityCondition, self.codespace, service_ids[i])

                availability_conditions_journey = [availability_conditions.get(availability_condition_key, None),
                                                   availability_conditions.get(availability_condition_key + "_1", None),
                                                   availability_conditions.get(availability_condition_key + "_2", None)]

                journey_pattern_view = None
                if trip_headsigns[i] is not None:
                    journey_pattern_view = JourneyPatternView(
                        destination_display_ref_or_destination_display_view=DestinationDisplayView(
                            name=MultilingualString(value=trip_headsigns[i]), front_text=MultilingualString(value=trip_headsigns[i])))

                accessibility_assessment = None
                if wheelchair_accessibles is not None and wheelchair_accessibles[i] is not None:
                    accessibility_assessment = AccessibilityAssessment(id=getId(AccessibilityAssessment, self.codespace, trip_ids[i]),
                                                                       version=self.version.version,
                                                                       mobility_impaired_access=self.wheelchairToNeTEx(wheelchair_accessibles[i]))

                block_ref = None
                if block_ids[i] is not None:
                    block_ref = getFakeRef(getId(Block, self.codespace, block_ids[i]), BlockRef, None)

                route_ref = None
                lsp = None
                shape_id = get_or_none(shape_ids, i)
                if shape_id is not None:
                    if shape_id in shape_used:
                        lsp = getFakeRef(getId(LinkSequenceProjection, self.codespace, shape_id), LinkSequenceProjectionRef, self.version.version)
                    else:
                        lsps = self.getLineStrings({'query': """select shape_id, shape_pt_lat, shape_pt_lon, shape_pt_sequence, shape_dist_traveled from shapes where shape_id = ? order by shape_id, shape_pt_sequence, shape_dist_traveled;""", 'parameters': (shape_id,)})
                        if len(lsps) > 0:
                            lsp = lsps[0]

                        shape_used.add(shape_id)

                luggage_carriage_facility_list = []
                facitities = None
                bikes_allowed = get_or_none(bikes_alloweds, i)
                if bikes_allowed is not None:
                    if bikes_allowed == 1:
                        luggage_carriage_facility_list.append(LuggageCarriageEnumeration.CYCLES_ALLOWED)
                    elif bikes_allowed == 2:
                        luggage_carriage_facility_list.append(LuggageCarriageEnumeration.NO_CYCLES)

                if len(luggage_carriage_facility_list) > 0:
                    facitities = ServiceFacilitySetsRelStructure(
                            service_facility_set_ref_or_service_facility_set=[ServiceFacilitySet(
                                id=getId(ServiceFacilitySet, self.codespace, trip_ids[i]), version=self.version.version,
                                luggage_carriage_facility_list=LuggageCarriageFacilityList(value=luggage_carriage_facility_list))])

                calls = CallsRelStructure()

                with self.conn.cursor() as cur2:
                    cur2.execute(**{'query': """select * from stop_times where trip_id = ? order by stop_sequence;""", 'parameters': (trip_ids[i],)})
                    trip_id = None
                    service_journey = None
                    prev_call = None
                    prev_shape_traveled = 0
                    prev_order = 1

                    df2 = cur2.df()

                    stop_headsigns = df2.get('stop_headsign')
                    stop_ids = df2.get('stop_id')
                    arrival_times = df2.get('arrival_time')
                    departure_times = df2.get('departure_time')
                    shape_dist_traveleds = df2.get('shape_dist_traveled')
                    drop_off_types = df2.get('drop_off_type')
                    pickup_types = df2.get('pickup_type')
                    stop_sequences = df2.get('stop_sequence')

                    for index_j in range(0, len(stop_ids)):
                        destination_display_view = None
                        stop_headsign = get_or_none(stop_headsigns, index_j)
                        if stop_headsign is not None:
                            destination_display_view = DestinationDisplayView(
                                name=MultilingualString(value=stop_headsign),
                                front_text=MultilingualString(value=stop_headsign))

                        from_point_ref = getId(ScheduledStopPoint, self.codespace, stop_ids[index_j])
                        arrival_time, arrival_dayoffset = self.noonTimeToNeTEx(arrival_times[index_j])
                        departure_time, departure_dayoffset = self.noonTimeToNeTEx(departure_times[index_j])

                        shape_dist_traveled = get_or_none(shape_dist_traveleds, index_j)
                        if prev_call and shape_dist_traveled:
                            distance = shape_dist_traveled - prev_shape_traveled
                            prev_call.onward_service_link_view = OnwardServiceLinkView(distance=distance)

                        call = Call(id=getId(Call, self.codespace, "{}_{}".format(trip_ids[i], stop_sequences[index_j])),
                                    version=self.version.version,
                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=getFakeRef(
                                        from_point_ref, ScheduledStopPointRef, self.version.version),
                                    destination_display_ref_or_destination_display_view=destination_display_view,
                                    arrival=ArrivalStructure(time=arrival_time, day_offset=arrival_dayoffset,
                                                             for_alighting=bool(drop_off_types[index_j] != 1)),
                                    departure=DepartureStructure(time=departure_time, day_offset=departure_dayoffset,
                                                                 for_boarding=bool(pickup_types[index_j] != 1)),
                                    request_stop=bool(
                                        pickup_types[index_j] == 2 or pickup_types[index_j] == 3 or drop_off_types[index_j] == 2 or
                                        drop_off_types[index_j] == 3),
                                    order=prev_order)  # stop_sequence is non-negative integer

                        calls.call.append(call)

                        prev_call = call
                        prev_shape_traveled = shape_dist_traveled
                        prev_order += 1

                service_journey = ServiceJourney(id=getId(ServiceJourney, self.codespace, trip_ids[i]),
                                                 version=self.version.version,
                                                 flexible_line_ref_or_line_ref_or_line_view_or_flexible_line_view=getFakeRef(getId(Line, self.codespace, route_ids[i]), LineRef, self.version.version),
                                                 private_code=PrivateCode(value=trip_ids[i], type_value="trip_id"),
                                                 short_name=getOptionalString(get_or_none(trip_short_names, i)),
                                                 validity_conditions_or_valid_between=[ValidityConditionsRelStructure(choice=[getRef(x, AvailabilityConditionRef) for x in availability_conditions_journey if x is not None])],
                                                 journey_pattern_view=journey_pattern_view,
                                                 direction_type=self.directionToNeTEx(get_or_none(direction_ids, i)),
                                                 block_ref=block_ref,
                                                 accessibility_assessment=accessibility_assessment,
                                                 facilities=facitities,
                                                 link_sequence_projection_ref_or_link_sequence_projection=lsp,
                                                 calls=calls
                                                 )

                yield service_journey

    def getTimetableFrame(self, availability_conditions, service_journeys, id="TimetableFrame") -> TimetableFrame:
        timetable_frame = TimetableFrame(id=getId(TimetableFrame, self.codespace, id), version=self.version.version)

        timetable_frame.vehicle_journeys = JourneysInFrameRelStructure(vehicle_journey_or_dated_vehicle_journey_or_normal_dated_vehicle_journey_or_service_journey_or_dated_service_journey_or_dead_run_or_special_service_or_template_service_journey=service_journeys)
        timetable_frame.content_validity_conditions = ValidityConditionsRelStructure(choice=availability_conditions)

        return timetable_frame

    def getCompositeFrame(self, operators, lines, stop_areas, scheduled_stop_points, service_journeys, availability_conditions) -> CompositeFrame:
        composite_frame = CompositeFrame(id=getId(CompositeFrame, self.codespace, self.data_source.short_name.value), version=self.version.version)
        composite_frame.frame_defaults = self.frame_defaults
        composite_frame.codespaces = CodespacesRelStructure(codespace_ref_or_codespace=[self.codespace])
        composite_frame.versions = VersionsRelStructure(version_ref_or_version=[self.version])
        composite_frame.frames = FramesRelStructure(common_frame=[self.getResourceFrame(operators)] + [self.getServiceFrame(lines, stop_areas, scheduled_stop_points)] + [self.getTimetableFrame(availability_conditions, service_journeys)])
        return composite_frame

    def getPublicationDelivery(self, operators, lines, stop_areas, scheduled_stop_points, service_journeys, availability_conditions) -> PublicationDelivery:
        composite_frame = self.getCompositeFrame(operators, lines, stop_areas, scheduled_stop_points, service_journeys, availability_conditions)

        publication_delivery = PublicationDelivery(
            publication_timestamp=XmlDateTime.from_datetime(datetime.datetime.now()),
            version = "ntx:1.1",
            participant_ref = ParticipantRef(value="NDOV"),
            description = MultilingualString(value="NeTEx export")
        )
        publication_delivery.data_objects = DataObjectsRelStructure(choice=[composite_frame])

        return publication_delivery

    def full(self):
        with open('netex-output/out.xml', 'w', encoding='utf-8') as out:
            operators = self.getOperators()
            stop_areas = self.getStopAreas()
            scheduled_stop_points = self.getScheduledStopPoints(stop_areas)
            availability_conditions = self.getAvailabilityConditions()
            service_journeys = self.getServiceJourneys(availability_conditions)

            self.serializer.write(out, self.getPublicationDelivery(operators, self.lines, stop_areas, scheduled_stop_points,
                                                                   service_journeys, availability_conditions),
                                  self.ns_map)

        with open('netex-output/out.xml', 'w',encoding='utf-8') as out:
            self.serializer.write(out, self.getPublicationDelivery(operators, self.lines, stop_areas, scheduled_stop_points, service_journeys, availability_conditions), self.ns_map)

    def incremental(self):
        for line in self.lines:
            with open('netex-output/{}.xml'.format(line.id.replace(':', '_')), 'w', encoding='utf-8') as out:
                operators = self.getOperators({'query': """select distinct agency.* from agency join routes using (agency_id) where route_id = ? ;""", 'parameters': (line.private_code.value,)})
                stop_areas = self.getStopAreas({'query': """select stops.* from stops where stop_id in (select distinct stops.parent_station from trips join stop_times using (trip_id) join stops using (stop_id) where (location_type = 0 or location_type is null) and parent_station is not null and route_id = ?) order by stop_id;""", 'parameters': (line.private_code.value,)})
                scheduled_stop_points = self.getScheduledStopPoints(stop_areas, {'query': """select distinct stops.* from trips join stop_times using (trip_id) join stops using (stop_id) where (location_type = 0 or location_type is null) and route_id = ? order by stop_id;""", 'parameters': (line.private_code.value,)})
                availability_conditions = self.getAvailabilityConditions(availability_condition_sql = {
                    'query': """select distinct calendar.* from trips join calendar using (service_id) where route_id = ? order by service_id;""", 'parameters': (line.private_code.value,)}, exceptions_sql = {
                    'query': """select service_id, exception_type, array_agg(date order by date) as dates from (select calendar_dates.* from trips join calendar_dates using (service_id) where route_id = ?) as x group by service_id, exception_type;""", 'parameters': (line.private_code.value,)})

                service_journeys = self.getServiceJourneys(availability_conditions, {
                    'query': """select * from trips where route_id = ? order by trip_id;""",
                    'parameters': (line.private_code.value,)},
                    {'query': """select stop_times.* from trips join stop_times using (trip_id) where route_id = ? order by trip_id, stop_sequence;""", 'parameters': (line.private_code.value,)})

                self.serializer.write(out, self.getPublicationDelivery(operators, [line], stop_areas, scheduled_stop_points, service_journeys, availability_conditions), self.ns_map)

    def database(self, con):
        write_objects(con, self.lines, empty=True, many=True)

        # This still sucks :-) shape is in every ServiceJourney now
        # in order to solve it, we must find the route point that matches the
        # shape point exactly, but if the GTFS shape is provided as an abstract
        # shape there may not be a one-to-one RouteLink.
        #
        # self.routes, self.route_points, self.route_links = self.getRoutes()
        # write_objects(con, self.route_points, True, True)
        # write_objects(con, self.route_links, True, True)
        # write_objects(con, self.routes, True, True)

        write_objects(con, [self.codespace], empty=True, many=True)
        write_objects(con, [self.data_source], empty=True, many=True)
        write_objects(con, [self.version], empty=True, many=True)

        write_objects(con, self.getOperators(), empty=True, many=True)
        stop_areas = self.getStopAreas()
        write_objects(con, stop_areas, empty=True, many=True)
        write_objects(con, self.getScheduledStopPoints(stop_areas), empty=True, many=True)
        stop_areas = None

        stop_places, passenger_stop_assignments = self.getStopPlaces()
        write_objects(con, stop_places, empty=True, many=True)
        write_objects(con, passenger_stop_assignments, empty=True, many=True)
        stop_places = stop_passenger_stop_assignments = None


        availability_conditions = self.getAvailabilityConditions()
        write_objects(con, availability_conditions, empty=True, many=True)

        write_generator(con, ServiceJourney, self.getServiceJourneys2(availability_conditions), empty=True)


    def __init__(self, conn, serializer):
        self.conn = conn
        self.serializer = serializer

        self.ns_map = {'': 'http://www.netex.org.uk/netex', 'gml': 'http://www.opengis.net/gml/3.2'}
        self.codespace, self.data_source, self.version, self.frame_defaults = self.getCodespaceAndDataSource()
        self.lines = self.getLines()
        # self.stop_areas = self.getStopAreas()
        # self.scheduled_stop_points = self.getScheduledStopPoints()
        # self.availability_conditions = self.getAvailabilityConditions()

        # if full:
        #     self.full()
        # else:
        #     self.incremental()

        # print('.')
        # self.routes, self.route_points, self.route_links = self.getRoutes()

        #
        # self.service_journeys = self.getServiceJourneys()
        # self.service_journey_patterns, self.timing_links = self.getServiceJourneyPatterns()
        # self.time_demand_types = self.getTimeDemandTypes()

def main(database_gtfs: str, database_netex: str):
    serializer_config = SerializerConfig(ignore_default_attributes=True)
    serializer_config.pretty_print = True
    serializer_config.ignore_default_attributes = True
    serializer = XmlSerializer(config=serializer_config)

    gtfs = GtfsNeTexProfile(conn=duckdb.connect(database=database_gtfs, read_only=True),
                            serializer=serializer)

    # Workaround for https://github.com/duckdb/duckdb/issues/8261
    try:
        os.remove(database_netex)
    except:
        pass

    with duckdb.connect(database_netex) as con:
        gtfs.database(con)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Convert a GTFS database to a NeTEx database')
    parser.add_argument('gtfs', type=str, help='GTFS database to convert, for example: gtfs-import.duckdb')
    parser.add_argument('database', type=str, help='DuckDB file to overwrite and store contents of the conversion.')
    args = parser.parse_args()

    main(args.gtfs, args.database)