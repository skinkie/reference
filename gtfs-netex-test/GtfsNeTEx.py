import datetime
import math

import duckdb
# import psycopg2, psycopg2.extras
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.models.datatype import XmlDateTime, XmlTime, XmlDate

# xsdata generate -p netex  --unsafe-hash -ss clusters --compound-fields  ~/Sources/NeTEx-master/xsd/NeTEx_publication.xsd

from callsprofile import CallsProfile
from netex import Codespace, DataSource, MultilingualString, Version, VersionFrameDefaultsStructure, \
    VersionTypeEnumeration, LocaleStructure, SystemOfUnits, Operator, ContactStructure, Locale, LanguageUsageStructure, \
    LanguageUseEnumeration, Line, PresentationStructure, AllVehicleModesOfTransportEnumeration, PrivateCode, \
    PublicationDelivery, DataObjectsRelStructure, OperationalContext, ResourceFrame, TypeOfFrameRef, \
    DataSourcesInFrameRelStructure, OrganisationsInFrameRelStructure, OperationalContextsInFrameRelStructure, \
    CompositeFrame, VersionsRelStructure, FramesRelStructure, ServiceFrame, LinesInFrameRelStructure, \
    OperatorRefStructure, OperatorRef, StopArea, LocationStructure2, SimplePointVersionStructure, PrivateCodeStructure, \
    ScheduledStopPoint, StopTypeEnumeration, StopAreaRefsRelStructure, StopAreaRefStructure, \
    StopAreasInFrameRelStructure, ScheduledStopPointsInFrameRelStructure, AvailabilityCondition, ServiceJourneyPattern, \
    StopPointInJourneyPattern, DestinationDisplayView, ScheduledStopPointRef, Call, ArrivalStructure, \
    DepartureStructure, CallsRelStructure, ValidityConditionsRelStructure, AvailabilityConditionRef, BlockRef, \
    DirectionTypeEnumeration, AccessibilityAssessment, LimitationStatusEnumeration, TimetableFrame, \
    JourneysInFrameRelStructure, LineRef, JourneyPatternView, CodespacesRelStructure, \
    JourneyPatternsInFrameRelStructure, ServiceJourney, TimingLinksInFrameRelStructure, \
    TimeDemandTypesInFrameRelStructure, OnwardTimingLinkView, OnwardServiceLinkView, PathLink, RouteRef, Route, \
    RoutePoint, PointsOnRouteRelStructure, RoutePointRef, PointOnRoute, RoutePointsInFrameRelStructure, \
    RoutesInFrameRelStructure, RouteLink, RouteLinksInFrameRelStructure, __all__, DayTypesRelStructure, DayType, \
    PropertiesOfDayRelStructure, PropertyOfDay, DayOfWeekEnumeration
from refs import setIdVersion, getRef, getIndex, getIdByRef, getBitString2, getFakeRef, getOptionalString, getId


def get_or_none(l: list, i: int):
    if l is None:
        return l
    return l[i]

def gtfs_date(d: str):
    return datetime.datetime(year=int(str(d)[0:4]), month=int(str(d)[4:6]), day=int(str(d)[6:8]))

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
            codespace = Codespace(id="{}:Codespace:{}".format(short_name, short_name), xmlns=short_name,
                                  xmlns_url=df['feed_publisher_url'][0], description=df['feed_publisher_name'][0])
            data_source = DataSource(id="{}:DataSource:{}".format(short_name, short_name),
                                     name=MultilingualString(value=df['feed_publisher_name'][0]),
                                     short_name=MultilingualString(value=short_name),
                                     description=MultilingualString(value=df['feed_publisher_name'][0]))

            start_date = datetime.datetime.combine(gtfs_date(df['feed_start_date'][0]), datetime.datetime.min.time())
            end_date = datetime.datetime.combine(gtfs_date(df['feed_end_date'][0]), datetime.datetime.min.time())

            version = Version(id="{}:Version:{}".format(short_name, df['feed_version'][0]),
                              version=df['feed_version'][0],
                              start_date=XmlDateTime.from_datetime(start_date),
                              end_date=XmlDateTime.from_datetime(end_date),
                              version_type=VersionTypeEnumeration.BASELINE)

            frame_defaults = VersionFrameDefaultsStructure(default_codespace_ref=getRef(codespace),
                                                           default_data_source_ref=getRef(data_source),
                                                           default_locale=LocaleStructure(default_language=df['feed_lang'][0]),
                                                           default_location_system="EPSG:4326",
                                                           default_system_of_units=SystemOfUnits.SI_METRES
                                                           )

            return (codespace, data_source, version, frame_defaults)

    def getResourceFrame(self) -> ResourceFrame:
        resource_frame = ResourceFrame(id=getId(ResourceFrame, self.codespace, self.version.version))
        resource_frame.data_sources = DataSourcesInFrameRelStructure(data_source=[self.data_source])
        # resource_frame.zones = ZonesInFrameRelStructure(transport_administrative_zone=[transport_administrative_zone])
        resource_frame.organisations = OrganisationsInFrameRelStructure(choice=self.operators)
        resource_frame.operational_contexts = OperationalContextsInFrameRelStructure(
            operational_context=self.getOperationalContexts())
        # resource_frame.vehicle_types = VehicleTypesInFrameRelStructure(compound_train_or_train_or_vehicle_type=getVehicleTypes(codespace))
        # resource_frame.vehicles = VehiclesInFrameRelStructure(train_element_or_vehicle=getVehicles(codespace))
        return resource_frame

    def getOperators(self) -> list[Operator]:
        feed_info_sql = """select * from agency;"""
        results = []

        with self.conn.cursor() as cur:
            cur.execute(feed_info_sql)
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
                                                                                                                             language_use=[LanguageUseEnumeration.NORMALLY_USED])])),
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
            return AllVehicleModesOfTransportEnumeration.SUBWAY
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
            return AllVehicleModesOfTransportEnumeration.TROLLEYBUS

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
        operators = getIndex(self.operators)

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
                    operator_ref = getRef(operators[getId(Operator, self.codespace, get_or_none(agency_ids, i))], OperatorRef)

                line = Line(id=get_or_none(route_ids, i),
                            version=self.version.version,
                            name=MultilingualString(value=get_or_none(route_long_names, i)),
                            short_name=getOptionalString(get_or_none(route_short_names, i)),
                            description=getOptionalString(get_or_none(route_descs, i)),
                            transport_mode=self.gtfsToNeTEx(get_or_none(route_types, i)),
                            presentation=presentation,
                            url=get_or_none(route_urls, i),
                            authority_ref_or_operator_ref=operator_ref,
                            public_code=get_or_none(route_short_names, i),
                            private_code=PrivateCode(value=get_or_none(route_ids, i), type_value="route_id"),
                            payment_methods=None,
                            purchase_moment=None
                            )
                lines.append(line)

        return lines

    def getStopAreas(self) -> list[StopArea]:
        stop_areas = []

        stop_area_sql = """select * from stops where location_type = 1 order by stop_id;"""

        with self.conn.cursor() as cur:
            cur.execute(stop_area_sql)
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
                                     name=MultilingualString(value=stop_names[i]),
                                     public_code=get_or_none(stop_codes, i),
                                     description=getOptionalString(get_or_none(stop_descs, i)),
                                     private_code=PrivateCode(value=stop_ids[i], type_value="stop_id"),
                                     centroid=SimplePointVersionStructure(location=
                                                                          LocationStructure2(latitude=stop_lats[i], longitude=stop_lons[i], srs_name="EPSG:4326")),
                                     )
                stop_areas.append(stop_area)

        return stop_areas

    def getScheduledStopPoints(self, scheduled_stop_points_sql: str = None) -> list[ScheduledStopPoint]:
        stop_areas = getIndex(self.stop_areas)

        scheduled_stop_points = []
        passenger_stop_assignments = []

        if scheduled_stop_points_sql is None:
            scheduled_stop_points_sql = """select * from stops where location_type = 0 or location_type is null order by stop_id;"""

        with self.conn.cursor() as cur:
            cur.execute(scheduled_stop_points_sql)
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

                location = LocationStructure2(longitude=get_or_none(stop_lons, i), latitude=get_or_none(stop_lats, i), srs_name="EPSG:4326")

                stop_areas = None
                parent_station = get_or_none(parent_stations, i)
                if parent_station is not None:
                    stop_area_ref = getId(StopArea, self.codespace, parent_station)
                    stop_areas = StopAreaRefsRelStructure(stop_area_ref=[
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
                                                          stop_areas=stop_areas)
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
    #
    # def getPaths(self):
    #     pl = PathLink()
    #
    #
    # def getRoutes(self) -> (list[Route], list[RoutePoint], list[RouteLink]):
    #     lines = getIndex(self.lines)
    #
    #     shape_route_mapping = {}
    #
    #     # Within NeTEx it is not possible to have a route (GTFS-shape) pointing to multiple lines (GTFS-route)
    #     shape_route_sql = """select distinct shape_id, array_agg(distinct route_id) as route_ids from trips group by shape_id;""";
    #     with self.conn.cursor() as cur:
    #         cur.execute(shape_route_sql)
    #         for row in cur.fetchall():
    #             if len(row['route_ids']) > 0:
    #                 shape_route_mapping[row['shape_id']] = [(row['shape_id'] + '-' + x, x) for x in row['route_ids']]
    #             else:
    #                 shape_route_mapping[row['shape_id']] = [(row['shape_id'], None)]
    #
    #     shape_sql = """select shape_id, shape_pt_lat, shape_pt_lon, shape_pt_sequence, shape_dist_traveled from shapes order by shape_id, shape_pt_sequence, shape_dist_traveled;"""
    #
    #     routes = {}
    #     route_points = []
    #     route_links = []
    #
    #     with self.conn.cursor() as cur:
    #         cur.execute(shape_sql)
    #         prev_order = 1
    #         prev_route = None
    #         prev_distance = 0
    #         prev_route_point = None
    #         prev_shape_id = None
    #
    #         for row in cur.fetchall():
    #             route_point = RoutePoint(location=LocationStructure2(longitude=row['shape_pt_lon'], latitude=row['shape_pt_lat']))
    #             setIdVersion(route_point, self.codespace, "{}-{}".format(row['shape_id'], row['shape_pt_sequence']), self.version)
    #             route_points.append(route_point)
    #
    #             if row['shape_id'] == prev_shape_id:
    #                 # It is the same route, and still being extended
    #                 distance = None
    #                 if row['shape_dist_traveled']:
    #                     distance = row['shape_dist_traveled'] - prev_distance
    #
    #                 route_link = RouteLink(from_point_ref=getRef(prev_route_point),
    #                                        to_point_ref=getRef(route_point),
    #                                        distance=distance)
    #                 setIdVersion(route_link, self.codespace,
    #                              "{}-{}".format(row['shape_id'], row['shape_pt_sequence']), self.version)
    #                 route_links.append(route_link)
    #
    #                 for route in prev_route:
    #                     route.points_in_sequence.point_on_route[-1].onward_route_link_ref = getRef(route_link)
    #
    #             else:
    #                 prew_order = 1
    #                 prev_route = []
    #                 prev_distance = 0
    #                 prev_route_point = None
    #                 prev_shape_id = None
    #
    #                 route_ids = shape_route_mapping.get(row['shape_id'], [row['shape_id']])
    #                 for route_id, line_id in route_ids:
    #                     route = Route()
    #                     setIdVersion(route, self.codespace, route_id, self.version)
    #                     route.private_code = PrivateCode(value = row['shape_id'], type = "shape_id")
    #                     route.points_in_sequence = PointsOnRouteRelStructure()
    #                     if line_id:
    #                         line = lines[getIdByRef(Line(), self.codespace, line_id)]
    #                         route.line_ref = getRef(line, LineRef)
    #
    #                     routes[route_id] = route
    #                     prev_route.append(route)
    #
    #             for route in prev_route:
    #                 point_on_route = PointOnRoute(order=prev_order, route_point_ref=getRef(route_point, RoutePointRef)) # shape_pt_sequence is non-negative integer
    #                 setIdVersion(point_on_route, self.codespace, "{}-{}".format(route_id, row['shape_pt_sequence']), self.version)
    #                 route.points_in_sequence.point_on_route.append(point_on_route)
    #
    #             prev_shape_id = row['shape_id']
    #             prev_route_point = route_point
    #             prev_distance = row['shape_dist_traveled']
    #             prev_order += 1
    #
    #     return (list(routes.values()), route_points, route_links)
    #
    def getServiceFrame(self, id="ServiceFrame") -> ServiceFrame:
        service_frame = ServiceFrame(id=getId(ServiceFrame, self.codespace, id), version=self.version.version)
        # service_frame.prerequisites.resource_frame_ref
        # setIdVersion(service_frame, self.codespace, "ServiceFrame", self.version)
        service_frame.lines = LinesInFrameRelStructure(flexible_line_or_line=self.lines)

        self.stop_areas = sorted(self.stop_areas, key=lambda x: x.id)
        if self.stop_areas:
            service_frame.stop_areas = StopAreasInFrameRelStructure(stop_area=self.stop_areas)

        self.scheduled_stop_points = sorted(self.scheduled_stop_points, key=lambda x: x.id)
        service_frame.scheduled_stop_points = ScheduledStopPointsInFrameRelStructure(scheduled_stop_point=self.scheduled_stop_points)

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
    #     self.routes = sorted(self.routes, key=lambda x: x.id)
    #     service_frame.routes = RoutesInFrameRelStructure(route=self.routes)
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


    def getAvailabilityConditions(self) -> list[AvailabilityCondition]:
        availability_conditions = []
        # availability_condition_sql = """select service_id, array_agg(date) as positivedates from universal_calendar group by service_id;"""

        exceptions_sql = """select service_id, exception_type, array_agg(date order by date) as dates from calendar_dates group by service_id, exception_type;"""
        availability_condition_sql = """select * from calendar order by service_id;"""

        with self.conn.cursor() as cur:
            cur.execute(exceptions_sql)
            exceptions_df = cur.df()
            exceptions = {}

            service_ids = exceptions_df.get('service_id')
            for i in range(0, len(service_ids)):
                exception_type = int(exceptions_df['exception_type'][i])
                if exception_type in (1, 2):
                    ac = AvailabilityCondition(id = getId(AvailabilityCondition, self.codespace, service_ids[i] + '_' + str(exception_type)), version=self.version.version, is_available=exception_type == 1, from_date=XmlDate.from_date(gtfs_date(exceptions_df['dates'][i][0])), to_date=XmlDate.from_date(gtfs_date(exceptions_df['dates'][i][-1])), valid_day_bits=getBitString2([gtfs_date(d) for d in exceptions_df['dates'][i]]))
                    l = exceptions.get(service_ids[i], [])
                    l.append(ac)
                    exceptions[service_ids[i]] = l
                    availability_conditions.append(ac)

            cur.execute(availability_condition_sql)
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
                                                                     from_date=XmlDate.from_date(gtfs_date(start_dates[i])), to_date=XmlDate.from_date(gtfs_date(end_dates[i])),
                                                                     day_types=DayTypesRelStructure(choice=[DayType(id=getId(DayType, self.codespace, service_ids[i]), version=self.version.version,
                                                                                                                    properties=PropertiesOfDayRelStructure(property_of_day=[PropertyOfDay(tides=None, weeks_of_month=None, holiday_types=None, seasons=None, days_of_week=days_of_week)]))])))

        """select service_id, array_agg(date order by date) as positivedates from calendar_dates where exception_type = 2 group by service_id;"""

        """

        with self.conn.cursor() as cur:
            cur.execute(availability_condition_sql)
            for row in cur.fetchall():
                valid_day_bits = getBitString2(row['positivedates'], self.version.start_date.to_datetime().date(), self.version.end_date.to_datetime().date())
                availability_condition = AvailabilityCondition(from_date=self.version.start_date,
                                                               to_date=self.version.end_date,
                                                               valid_day_bits=valid_day_bits)
                setIdVersion(availability_condition, self.codespace, row['service_id'], self.version)
                availability_conditions.append(availability_condition)
        """
        return availability_conditions
    #
    # @staticmethod
    # def noonTimeToNeTEx(time: str):
    #     hour, minute, second = time.split(':')
    #     hour = int(hour)
    #     day_offset = int(math.floor(hour / 24))
    #     return (XmlTime(hour=hour % 24, minute=int(minute), second=int(second), microsecond=0), day_offset)
    #
    # @staticmethod
    # def directionToNeTEx(direction_id: int):
    #     if direction_id is None:
    #         return None
    #
    #     elif direction_id == 1:
    #         return DirectionTypeEnumeration.INBOUND
    #
    #     return DirectionTypeEnumeration.OUTBOUND
    #
    # @staticmethod
    # def wheelchairToNeTEx(wheelchair_accessible: int):
    #     if wheelchair_accessible == 0:
    #         return LimitationStatusEnumeration.UNKNOWN
    #
    #     return LimitationStatusEnumeration.TRUE
    #
    #
    # def getServiceJourneys(self) -> list[ServiceJourney]:
    #     routes = getIndex(self.routes, 'private_code.value')
    #     lines = getIndex(self.lines)
    #     availability_conditions = getIndex(self.availability_conditions)
    #
    #     service_journeys = {}
    #
    #     trips_sql = """select * from trips order by trip_id;"""
    #     with self.conn.cursor() as cur:
    #         cur.execute(trips_sql)
    #
    #         for row in cur.fetchall():
    #             line = lines[getIdByRef(Line(), self.codespace, row['route_id'])]
    #             availability_condition = availability_conditions[getIdByRef(AvailabilityCondition(), self.codespace, row['service_id'])]
    #             destination_display_view = None
    #             if row['trip_headsign']:
    #                 destination_display_view = DestinationDisplayView(name=MultilingualString(row['trip_headsign']),
    #                                                                   front_text=MultilingualString(
    #                                                                       row['trip_headsign']))
    #
    #             accessibility_assessment = None
    #             if row['wheelchair_accessible']:
    #                 accessibility_assessment = AccessibilityAssessment(mobility_impaired_access=self.wheelchairToNeTEx(row['wheelchair_accessible']))
    #                 setIdVersion(accessibility_assessment, self.codespace, row['trip_id'], self.version)
    #
    #             route_ref = None
    #             if row['shape_id']:
    #                 route_ref = getRef(routes[row['shape_id']], RouteRef)
    #                 # route_ref = getFakeRef(row['shape_id'], RouteRef, self.version.version)
    #
    #             service_journey = ServiceJourney(line_ref=getRef(line, LineRef),
    #                                               private_code=PrivateCode(value=row['trip_id'], type="trip_id"),
    #                                               short_name=getOptionalString(row['trip_short_name']),
    #                                               validity_conditions_or_valid_between=ValidityConditionsRelStructure(choice=[getRef(availability_condition, AvailabilityConditionRef)]),
    #                                               route_ref=route_ref, # shape_id
    #                                               journey_pattern_view=JourneyPatternView(destination_display_view=destination_display_view),
    #                                               direction_type=self.directionToNeTEx(row['direction_id']),
    #                                               block_ref=getFakeRef(row['block_id'], BlockRef, "any"),
    #                                               accessibility_assessment=accessibility_assessment
    #                                               )
    #             setIdVersion(service_journey, self.codespace, row['trip_id'], self.version)
    #
    #             service_journeys[row['trip_id']] = service_journey
    #
    #     scheduled_stop_points = getIndex(self.scheduled_stop_points)
    #
    #     stop_times_sql = """select * from stop_times order by trip_id, stop_sequence;"""
    #
    #     with self.conn.cursor() as cur:
    #         cur.execute(stop_times_sql)
    #         trip_id = None
    #         service_journey = None
    #         prev_call = None
    #         prev_shape_traveled = 0
    #         prev_order = 1
    #         for row in cur.fetchall():
    #             if row['trip_id'] != trip_id:
    #                 trip_id = row['trip_id']
    #                 service_journey = service_journeys[trip_id]
    #                 service_journey.calls = CallsRelStructure()
    #                 prev_call = None
    #                 prev_shape_traveled = 0
    #                 prev_order = 1
    #
    #             destination_display_view = None
    #             if row['stop_headsign']:
    #                 destination_display_view = DestinationDisplayView(name=MultilingualString(row['stop_headsign']),
    #                                                                   front_text=MultilingualString(
    #                                                                       row['stop_headsign']))
    #
    #             from_point_ref = getIdByRef(ScheduledStopPoint(), self.codespace, row['stop_id'])
    #             from_ssp = scheduled_stop_points[from_point_ref]
    #             arrival_time, arrival_dayoffset = self.noonTimeToNeTEx(row['arrival_time'])
    #             departure_time, departure_dayoffset = self.noonTimeToNeTEx(row['departure_time'])
    #
    #             if prev_call and row['shape_dist_traveled']:
    #                 distance = row['shape_dist_traveled'] - prev_shape_traveled
    #                 prev_call.onward_service_link_view = OnwardServiceLinkView(distance=distance)
    #
    #             call = Call(scheduled_stop_point_ref=getRef(from_ssp, ScheduledStopPointRef),
    #                          destination_display_view=destination_display_view,
    #                          arrival=ArrivalStructure(time=arrival_time, day_offset=arrival_dayoffset,
    #                                                   for_alighting=(row['drop_off_type'] != 1)),
    #                          departure=DepartureStructure(time=departure_time, day_offset=departure_dayoffset,
    #                                                   for_boarding=(row['pickup_type'] != 1)),
    #                          request_stop=(row['pickup_type'] == 2 or row['pickup_type'] == 3 or row[
    #                              'drop_off_type'] == 2 or row['drop_off_type'] == 3),
    #                          order=prev_order) # stop_sequence is non-negative integer
    #             setIdVersion(call, self.codespace, "{}:{}".format(row['trip_id'], row['stop_sequence']), self.version)
    #
    #             service_journey.calls.call.append(call)
    #
    #             prev_call = call
    #             prev_shape_traveled = row['shape_dist_traveled']
    #             prev_order += 1
    #
    #     return list(service_journeys.values())
    #
    #
    def getTimetableFrame(self, id="TimetableFrame") -> TimetableFrame:
        timetable_frame = TimetableFrame(id=getId(TimetableFrame, self.codespace, id))

        # timetable_frame.vehicle_journeys = JourneysInFrameRelStructure(choice=self.service_journeys)
        timetable_frame.content_validity_conditions = ValidityConditionsRelStructure(choice=self.availability_conditions)

        return timetable_frame

    def getCompositeFrame(self) -> CompositeFrame:
        composite_frame = CompositeFrame(id=getId(CompositeFrame, self.codespace, self.data_source.short_name.value), version=self.version.version)
        composite_frame.frame_defaults = self.frame_defaults
        composite_frame.codespaces = CodespacesRelStructure(codespace_ref_or_codespace=[self.codespace])
        composite_frame.versions = VersionsRelStructure(version_ref_or_version=[self.version])
        composite_frame.frames = FramesRelStructure(choice=[self.getResourceFrame()] + [self.getServiceFrame()] + [self.getTimetableFrame()])
        return composite_frame

    def getPublicationDelivery(self) -> PublicationDelivery:
        composite_frame = self.getCompositeFrame()

        publication_delivery = PublicationDelivery(
            publication_timestamp=XmlDateTime.from_datetime(datetime.datetime.now()),
            version = "ntx:1.1",
            participant_ref = "NDOV",
            description = "NeTEx export"
        )
        publication_delivery.data_objects = DataObjectsRelStructure(choice=[composite_frame])

        return publication_delivery

    def __init__(self, conn):
        self.conn = conn
        self.codespace, self.data_source, self.version, self.frame_defaults = self.getCodespaceAndDataSource()
        self.operators = self.getOperators()
        self.lines = self.getLines()
        self.stop_areas = self.getStopAreas()
        self.scheduled_stop_points = self.getScheduledStopPoints()
        self.availability_conditions = self.getAvailabilityConditions()

        print('.')
        # self.routes, self.route_points, self.route_links = self.getRoutes()

        #
        # self.service_journeys = self.getServiceJourneys()
        # self.service_journey_patterns, self.timing_links = self.getServiceJourneyPatterns()
        # self.time_demand_types = self.getTimeDemandTypes()

if __name__ == '__main__':
    serializer_config = SerializerConfig(ignore_default_attributes=True)
    serializer_config.pretty_print = True
    serializer_config.ignore_default_attributes = True
    serializer = XmlSerializer(serializer_config)

    ns_map = {'': 'http://www.netex.org.uk/netex', 'gml': 'http://www.opengis.net/gml/3.2'}

    with open('/tmp/out.xml', 'w') as out:
        gtfs = GtfsNeTexProfile(conn=duckdb.connect(database='/tmp/gtfs2.duckdb'))
        serializer.write(out, gtfs.getPublicationDelivery(), ns_map)
