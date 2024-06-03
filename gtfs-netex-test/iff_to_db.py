import datetime
from decimal import Decimal
from typing import List, Tuple, Generator, Dict, Set
from zipfile import ZipFile
from itertools import combinations

from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.models.datatype import XmlDateTime, XmlDuration, XmlTime

from netex import PublicationDelivery, ParticipantRef, MultilingualString, DataObjectsRelStructure, CompositeFrame, \
    Codespace, ValidBetween, StopPlace, InterchangeWeightingEnumeration, OperatorRef, ScheduledStopPoint, Locale, \
    SimplePointVersionStructure, LocationStructure2, Pos, InterchangeRule, DefaultInterchange, PassengerStopAssignment, \
    Country, TypeOfService, TypeOfProductCategory, Operator, DataSource, UicOperatingPeriod, Notice, KeyList, \
    TypeOfNotice, AlternativeText, ServiceJourney, JourneyPartsRelStructure, JourneyPart, TrainBlock, \
    ScheduledStopPointRef, TrainNumberRef, TrainNumber, NoticeAssignment, TypeOfProductCategoryRef, NoticeRef, \
    TrainNumberRefsRelStructure, TimetabledPassingTimesRelStructure, TimetabledPassingTime, StopPointInJourneyPattern, \
    StopPointInJourneyPatternRef, Call, ArrivalStructure, DepartureStructure, CallsRelStructure, RouteRef, Route, \
    ValidityConditionsRelStructure, AvailabilityConditionRef, AvailabilityCondition, FramesRelStructure, SiteFrame, \
    StopPlacesInFrameRelStructure, ServiceFrame, ScheduledStopPointsInFrameRelStructure, \
    StopAssignmentsInFrameRelStructure, RoutesInFrameRelStructure, RoutePointsInFrameRelStructure, \
    RouteLinksInFrameRelStructure, TimetableFrame, JourneysInFrameRelStructure, InterchangeRulesInFrameRelStructure, \
    DefaultInterchangseInFrameRelStructure, ProjectionsRelStructure, PointProjection, RoutePoint, RouteLink, \
    NoticeAssignmentsInFrameRelStructure, NoticesInFrameRelStructure, ResourceFrame, TypesOfValueInFrameRelStructure, \
    OrganisationsInFrameRelStructure, RoutePointRef, PointOnRoute, RouteLinkRef, PointsOnRouteRelStructure, \
    PointRefStructure, Quay, QuaysRelStructure, VersionFrameDefaultsStructure, LocaleStructure, SystemOfUnits, \
    CodespaceRefStructure, RoutePointRefStructure, RouteLinkRefStructure, VersionOfObjectRefStructure, \
    ScheduledStopPointRefStructure, TrainNumbersInFrameRelStructure, CodespacesRelStructure, \
    DataSourcesInFrameRelStructure, DataSourceRefStructure, ServiceJourneyInterchange, ServiceJourneyRefStructure, \
    ConnectionCertaintyEnumeration, JourneyInterchangesInFrameRelStructure, AccessibilityAssessment, \
    LimitationStatusEnumeration, SiteFacilitySetsRelStructure, SiteFacilitySet, AssistanceFacilityList, \
    AssistanceFacilityEnumeration, ServiceJourneyPatternInterchange, InterchangeRuleParameterStructure, StopPlaceRef, \
    AllVehicleModesOfTransportEnumeration, VehicleJourneyRefStructure, EmptyType2

import io

import pytz

from refs import getId, getRef, getFakeRef
import datetime

from utils import project

tz = pytz.timezone('Europe/Amsterdam')

codespace = Codespace(id="BISON:Codespace:NS", xmlns="NS", xmlns_url="http://bison.dova.nu/ns/NS", description=MultilingualString(value="Dienstencentrum Reisinformatie"))

def iff_slice(line: str, first: int, last: int) -> str:
    return line[first - 1:last].strip()

def iff_date(value: str) -> datetime.date:
    return datetime.date(int(value[4:8]), int(value[2:4]), int(value[0:2]))



def station_to_interchange_weighting(station_of_train_changes: int) -> InterchangeWeightingEnumeration:
    match station_of_train_changes:
        case 0:
            return InterchangeWeightingEnumeration.NO_INTERCHANGE
        case 1:
            return InterchangeWeightingEnumeration.INTERCHANGE_ALLOWED
        case 2:
            return InterchangeWeightingEnumeration.NO_INTERCHANGE

def parse_delivery(g):
    line = g.readline()
    record_id = iff_slice(line, 1, 1)
    assert record_id == '@'
    company_number = iff_slice(line, 2, 4)
    first_day = iff_slice(line, 6, 13)
    last_day = iff_slice(line, 15, 22)
    version_number = iff_slice(line, 24, 27)
    description = iff_slice(line, 29, 58)
    return OperatorRef(ref=getId(Operator, codespace, company_number), version=str(version_number)), XmlDateTime.from_datetime(datetime.datetime.combine(iff_date(first_day), datetime.datetime.min.time())), XmlDateTime.from_datetime(datetime.datetime.combine(iff_date(last_day), datetime.datetime.min.time())), version_number, MultilingualString(value=description)

def iff_siteframe(stop_places: List[StopPlace], from_date, to_date, version) -> SiteFrame:

    return SiteFrame(id=getId(SiteFrame, codespace, "IFF"), version=str(version),
              validity_conditions_or_valid_between=[ValidBetween(
                  from_date=from_date,
                  to_date=to_date,
              )
              ],
              stop_places=StopPlacesInFrameRelStructure(stop_place=stop_places))

def iff_resourceframe(type_of_product_categories: List[TypeOfProductCategory],
                      operators: List[Operator],
                      data_source,
                     from_date, to_date, version) -> ResourceFrame:
    return ResourceFrame(id=getId(ResourceFrame, codespace, "IFF"), version=str(version),
              validity_conditions_or_valid_between=[ValidBetween(
                  from_date=from_date,
                  to_date=to_date,
              )
              ],
                         types_of_value=TypesOfValueInFrameRelStructure(choice=type_of_product_categories + list(trnsattr_type_of_notice.values()), ),
                         data_sources=DataSourcesInFrameRelStructure(data_source=data_source),
                         organisations=OrganisationsInFrameRelStructure(organisation_or_transport_organisation=operators)
                        )

def iff_serviceframe(scheduled_stop_points: List[ScheduledStopPoint],
                     passenger_stop_assignments: List[PassengerStopAssignment], routes: List[Route],
                     route_points: List[RoutePoint], route_links: List[RouteLink],
                     notices: List[Notice],
                     notice_assignments: List[NoticeAssignment],
                     from_date, to_date, version) -> ServiceFrame:
    return ServiceFrame(id=getId(ServiceFrame, codespace, "IFF"), version=str(version),
              validity_conditions_or_valid_between=[ValidBetween(
                  from_date=from_date,
                  to_date=to_date,
              )
              ],
            scheduled_stop_points=ScheduledStopPointsInFrameRelStructure(scheduled_stop_point=scheduled_stop_points),
                        stop_assignments=StopAssignmentsInFrameRelStructure(stop_assignment=passenger_stop_assignments),
                        routes=RoutesInFrameRelStructure(route=routes),
                        route_points=RoutePointsInFrameRelStructure(route_point=route_points),
                        route_links=RouteLinksInFrameRelStructure(route_link=route_links),
                        notice_assignments=NoticeAssignmentsInFrameRelStructure(notice_assignment=notice_assignments),
                        notices=NoticesInFrameRelStructure(notice=notices)
                        )

def xchanges(zf: ZipFile) -> Generator[InterchangeRule, None, None]:
    year, month, day, hour, minute, second = zf.getinfo('xchanges.dat').date_time

    with zf.open('xchanges.dat', 'r') as f:
        station_short_name = None
        g = io.TextIOWrapper(f, 'ISO-8859-1')
        operator_ref, from_date, to_date, version, description = parse_delivery(g)

        for line in g:
            match line[0]:
                case '#':
                    station_short_name = iff_slice(line, 2, 8)
                case '-':
                    from_company_number = iff_slice(line, 2, 4)
                    from_transport_mode_code = iff_slice(line, 6, 9)
                    to_company_number = iff_slice(line, 11, 13)
                    to_transport_mode_code = iff_slice(line, 15, 18)
                    time_to_change = int(iff_slice(line, 20, 22))
                    footnote_number = int(iff_slice(line, 24, 28))

                    yield InterchangeRule(id=getId(InterchangeRule, codespace, f"{station_short_name}-{from_company_number}-{from_transport_mode_code}-{to_company_number}-{to_transport_mode_code}-{footnote_number}"), version=version,
                                          validity_conditions_or_valid_between=[ValidityConditionsRelStructure(choice=[getFakeRef(getId(AvailabilityCondition, codespace, f"X{footnote_number}"), AvailabilityConditionRef, version)])],
                                          advertised=True, planned=True, standard_transfer_time=XmlDuration(value=f"PT{time_to_change}M"),

                                          feeder_filter=InterchangeRuleParameterStructure(stop_place_ref=getFakeRef(getId(StopPlace, codespace, station_short_name), StopPlaceRef, version),
                                                                                          transport_mode=get_best_effort_mapping_transport_mode(from_transport_mode_code) if from_transport_mode_code != '*' else None,
                                                                                          operator_ref=getFakeRef(getId(Operator, codespace, from_company_number), OperatorRef, version) if from_company_number != '*' else None,
                                                                                          all_lines_or_lines_in_direction_refs_or_line_in_direction_ref=[EmptyType2(value='')]
                                                                                          ),

                                          distributor_filter=InterchangeRuleParameterStructure(stop_place_ref=getFakeRef(
                                              getId(StopPlace, codespace, station_short_name), StopPlaceRef,
                                              version),
                                                                                          transport_mode=get_best_effort_mapping_transport_mode(
                                                                                              to_transport_mode_code) if to_transport_mode_code != '*' else None,
                                                                                          operator_ref=getFakeRef(
                                                                                              getId(Operator,
                                                                                                       codespace,
                                                                                                       to_company_number), OperatorRef, version) if to_company_number != '*' else None,
                    all_lines_or_lines_in_direction_refs_or_line_in_direction_ref = [EmptyType2(value='')]
                                                                                          )




                    )

def iff_timetableframe(service_journeys: List[ServiceJourney],
                       availability_conditions: List[AvailabilityCondition],
                       default_interchanges: List[DefaultInterchange],
                       service_journey_interchanges: List[ServiceJourneyInterchange],
                       interchange_rules: List[InterchangeRule],
                       train_numbers: List[TrainNumber],
                     from_date, to_date,
                     version) -> TimetableFrame:
    return TimetableFrame(id=getId(TimetableFrame, codespace, "IFF"), version=str(version),
                        validity_conditions_or_valid_between=[ValidBetween(
                            from_date=from_date,
                            to_date=to_date,
                        )
                        ],
                        vehicle_journeys=JourneysInFrameRelStructure(
                            vehicle_journey_or_dated_vehicle_journey_or_normal_dated_vehicle_journey_or_service_journey_or_dated_service_journey_or_dead_run_or_special_service_or_template_service_journey=service_journeys),
                          default_interchanges=DefaultInterchangseInFrameRelStructure(default_interchange=default_interchanges),
                          journey_interchanges=JourneyInterchangesInFrameRelStructure(service_journey_pattern_interchange_or_service_journey_interchange=service_journey_interchanges),
                          content_validity_conditions=ValidityConditionsRelStructure(choice=availability_conditions),
                          train_numbers=TrainNumbersInFrameRelStructure(train_number_or_train_number_ref=train_numbers),
                          interchange_rules=InterchangeRulesInFrameRelStructure(interchange_rule=interchange_rules)
                          )

def stations_to_stopplace(zf: ZipFile, extra_quays: Dict[str, Tuple[str]]) -> Generator[Tuple[StopPlace, List[RoutePoint],
List[ScheduledStopPoint], List[DefaultInterchange], List[PassengerStopAssignment]], None, None]:
    year, month, day, hour, minute, second = zf.getinfo('stations.dat').date_time

    accessibility: dict[str, Set[str]] = {}
    low_priority_transfers = set([])

    with zf.open('attributesonstation.dat', 'r') as f:
        g = io.TextIOWrapper(f, 'ISO-8859-1')

        for line in g:
            station_short_name = iff_slice(line, 0, 7)
            low_priority_transfers.add(station_short_name)

    with zf.open('attributesonstation.dat', 'r') as f:
        station_short_name = None
        g = io.TextIOWrapper(f, 'ISO-8859-1')

        for line in g:
            match line[0]:
                case '#':
                    station_short_name = iff_slice(line, 1, 8)
                    accessibility[station_short_name] = set([])
                case '-':
                    attr = iff_slice(line, 1, 8)
                    accessibility[station_short_name].add(attr)


    with zf.open('stations.dat', 'r') as f:
        g = io.TextIOWrapper(f, 'ISO-8859-1')
        operator_ref, from_date, to_date, version, description = parse_delivery(g)
        for line in g:
            station_of_train_changes = int(iff_slice(line, 1, 1))
            station_short_name = iff_slice(line, 3, 9)
            min_interchange_time = iff_slice(line, 11, 12)
            max_interchange_time = iff_slice(line, 14, 15) # deprecated
            country_code = iff_slice(line, 17, 20)
            time_zone_offset = iff_slice(line, 22, 25)
            attribute = iff_slice(line, 27, 28) # deprecated
            x_coordinate = None
            y_coordinate = None
            try:
                x_coordinate = int(iff_slice(line, 30, 35))
            except:
                pass
            try:
                y_coordinate = int(iff_slice(line, 37, 42))
            except:
                pass
            station_name = iff_slice(line, 44, 73)

            weighting = station_to_interchange_weighting(station_of_train_changes)
            low_priority_transfer = station_short_name in low_priority_transfers

            route_points = []
            quays = []
            ssps = []
            default_interchanges = []
            psas = []

            sub_ssp = []

            for quay in extra_quays.get(station_short_name, []):
                route_point = RoutePoint(id=getId(RoutePoint, codespace, f"{station_short_name}-{quay}"),
                                         version=version,
                                         location=LocationStructure2(
                                             pos=Pos(value=[x_coordinate, y_coordinate], srs_dimension=2)) if x_coordinate is not None else None)
                route_points.append(route_point)

                ssp = ScheduledStopPoint(id=getId(ScheduledStopPoint, codespace, f"{station_short_name}-{quay}"), version=version,
                                         name=MultilingualString(value=f"{station_name} {quay}"),
                                         short_name=MultilingualString(value=quay),
                                         location=LocationStructure2(
                                             pos=Pos(value=[x_coordinate, y_coordinate], srs_dimension=2)) if x_coordinate is not None else None,
                                         projections=ProjectionsRelStructure(projection_ref_or_projection=[
                                             PointProjection(id=getId(PointProjection, codespace, f"{station_short_name}-{quay}"),
                                                             version=version, project_to_point_ref=getRef(route_point,
                                                                                                          PointRefStructure))]), )
                ssps.append(ssp)

                if weighting != InterchangeWeightingEnumeration.NO_INTERCHANGE:
                    default_interchange = DefaultInterchange(id=getId(DefaultInterchange, codespace, f"{station_short_name}-{quay}"),
                                                             version=version,
                                                             from_stop_point_ref=getRef(ssp, ScheduledStopPointRefStructure),
                                                             to_stop_point_ref=getRef(ssp, ScheduledStopPointRefStructure),
                                                             standard_transfer_time=XmlDuration(
                                                                 value=f"PT{min_interchange_time}M"),
                                                             maximum_transfer_time=XmlDuration(
                                                                 value=f"PT{max_interchange_time}M"))
                    default_interchanges.append(default_interchange)
                    sub_ssp.append(ssp)

                quay_i = Quay(id=getId(Quay, codespace, f"{station_short_name}-{quay}"),
                      version=version,
                      short_name=MultilingualString(value=quay),
                      name=MultilingualString(value=f"{station_name} {quay}"))
                quays.append(quay_i)

                psa = PassengerStopAssignment(id=getId(PassengerStopAssignment, codespace, f"{station_short_name}-{quay}"),
                                              version=version,
                                              order=1,
                                              taxi_stand_ref_or_quay_ref_or_quay=getRef(quay_i),
                                              fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point=getRef(
                                                  ssp))
                psas.append(psa)

            if weighting != InterchangeWeightingEnumeration.NO_INTERCHANGE:
                for f,t in list(combinations(sub_ssp, 2)):
                    default_interchange = DefaultInterchange(id=getId(DefaultInterchange, codespace, f"{station_short_name}-{f.short_name.value}-{t.short_name.value}"),
                                                             version=version,
                                                             from_stop_point_ref=getRef(f, ScheduledStopPointRefStructure),
                                                             to_stop_point_ref=getRef(t, ScheduledStopPointRefStructure),
                                                             standard_transfer_time=XmlDuration(
                                                                 value=f"PT{min_interchange_time}M"),
                                                             maximum_transfer_time=XmlDuration(
                                                                 value=f"PT{max_interchange_time}M"))
                    default_interchanges.append(default_interchange)

                    default_interchange = DefaultInterchange(id=getId(DefaultInterchange, codespace, f"{station_short_name}-{t.short_name.value}-{f.short_name.value}"),
                                                             version=version,
                                                             from_stop_point_ref=getRef(t, ScheduledStopPointRefStructure),
                                                             to_stop_point_ref=getRef(f, ScheduledStopPointRefStructure),
                                                             standard_transfer_time=XmlDuration(
                                                                 value=f"PT{min_interchange_time}M"),
                                                             maximum_transfer_time=XmlDuration(
                                                                 value=f"PT{max_interchange_time}M"))
                    default_interchanges.append(default_interchange)

            # TODO: station_of_train_changes == 2, TimingPoint?

            stop_place = StopPlace(id=getId(StopPlace, codespace, station_short_name),
                      version=version,
                      weighting=weighting,
                      short_name=MultilingualString(value=station_short_name),
                      name=MultilingualString(value=station_name),
                      centroid=SimplePointVersionStructure(location=LocationStructure2(pos=Pos(value=[x_coordinate, y_coordinate], srs_dimension=2))) if x_coordinate is not None else None,
                      locale=Locale(time_zone_offset=Decimal(int(time_zone_offset[0:2]))),
                                   quays=QuaysRelStructure(taxi_stand_ref_or_quay_ref_or_quay=quays) if len(quays) > 0 else None,
                                   facilities=SiteFacilitySetsRelStructure(site_facility_set_ref_or_site_facility_set=[SiteFacilitySet(assistance_facility_list=AssistanceFacilityList(value=[AssistanceFacilityEnumeration.BOARDING_ASSISTANCE]))]) if 'RAST' in accessibility.get(station_short_name, []) else None,
                                   accessibility_assessment=AccessibilityAssessment(id=getId(AccessibilityAssessment, codespace, station_short_name), version=version, mobility_impaired_access=LimitationStatusEnumeration.TRUE if 'TGST' in accessibility.get(station_short_name, []) else LimitationStatusEnumeration.FALSE)

                                   )

            route_point = RoutePoint(id=getId(RoutePoint, codespace, station_short_name),
                                     version=version,
                                     location=LocationStructure2(pos=Pos(value=[x_coordinate, y_coordinate], srs_dimension=2)) if x_coordinate is not None else None)
            route_points.append(route_point)

            ssp = ScheduledStopPoint(id=getId(ScheduledStopPoint, codespace, station_short_name), version=version,
                                     name=MultilingualString(value=f"{station_name}"),
                                     short_name=MultilingualString(value=station_short_name),
                                     location=LocationStructure2(pos=Pos(value=[x_coordinate, y_coordinate], srs_dimension=2)) if x_coordinate is not None else None,  projections=ProjectionsRelStructure(projection_ref_or_projection=[PointProjection(id=getId(PointProjection, codespace, station_short_name), version=version, project_to_point_ref=getRef(route_point, PointRefStructure))]),)
            ssps.append(ssp)

            if weighting != InterchangeWeightingEnumeration.NO_INTERCHANGE:
                default_interchange = DefaultInterchange(id=getId(DefaultInterchange, codespace, station_short_name),
                                   version=version,
                                   from_stop_point_ref=getRef(ssp, ScheduledStopPointRefStructure),
                                   to_stop_point_ref=getRef(ssp, ScheduledStopPointRefStructure),
                                   standard_transfer_time=XmlDuration(value=f"PT{min_interchange_time}M"),
                                   maximum_transfer_time=XmlDuration(value=f"PT{max_interchange_time}M"))
                default_interchanges.append(default_interchange)

            psa = PassengerStopAssignment(id=getId(PassengerStopAssignment, codespace, station_short_name),
                                    version=version,
                                     order=1,
                                    taxi_rank_ref_or_stop_place_ref_or_stop_place=getRef(stop_place),
                                    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point=getRef(ssp))
            psas.append(psa)

            yield stop_place, route_points, ssps, default_interchanges, psas



def country_to_country(zf: ZipFile) -> Generator[Country, None, None]:
    year, month, day, hour, minute, second = zf.getinfo('country.dat').date_time
    with zf.open('country.dat', 'r') as f:
        g = io.TextIOWrapper(f, 'ISO-8859-1')
        operator_ref, from_date, to_date, version, description = parse_delivery(g)
        for line in g:
            country_code = iff_slice(line, 1, 4)
            inland = int(iff_slice(line, 6, 6)) == 1
            country_name = iff_slice(line, 8, 37)

            yield Country(id=getId(Country, codespace, country_code), version=version, name=MultilingualString(value=country_name), short_name=MultilingualString(value=country_code))

def get_best_effort_mapping_transport_mode(transmode_code: str) -> AllVehicleModesOfTransportEnumeration:
    lc = transmode_code.lower()
    if lc in ('bus', 'belbus') or 'stopbus' in lc or 'snelbus' in lc:
        return AllVehicleModesOfTransportEnumeration.BUS
    elif lc == 'metro' or 'metro' in lc:
        return AllVehicleModesOfTransportEnumeration.METRO
    elif lc == 'tram' or 'tram' in lc:
        return AllVehicleModesOfTransportEnumeration.TRAM
    else:
        return AllVehicleModesOfTransportEnumeration.RAIL

def trnsmode_to_type_of_product_category(zf: ZipFile) -> Generator[TypeOfProductCategory, None, None]:
    year, month, day, hour, minute, second = zf.getinfo('trnsmode.dat').date_time
    with zf.open('trnsmode.dat', 'r') as f:
        g = io.TextIOWrapper(f, 'ISO-8859-1')
        operator_ref, from_date, to_date, version, description = parse_delivery(g)
        for line in g:
            transmode_code = iff_slice(line,1, 4)
            description = iff_slice(line,6, 35)

            yield TypeOfProductCategory(id=getId(TypeOfProductCategory, codespace, transmode_code), version=version, description=MultilingualString(value=description))

def company_to_operator(zf: ZipFile) -> Generator[Operator, None, None]:
    year, month, day, hour, minute, second = zf.getinfo('company.dat').date_time
    with zf.open('company.dat', 'r') as f:
        g = io.TextIOWrapper(f, 'ISO-8859-1')
        operator_ref, from_date, to_date, version, description = parse_delivery(g)
        for line in g:
            company_number = int(iff_slice(line, 1, 3))
            company_code = iff_slice(line, 5, 14)
            company_name = iff_slice(line, 16, 45)
            turn_time = iff_slice(line, 47, 50) # TODO: time of the turn of the day in the concerned timetable format HHMM ( < 2400)

            yield Operator(id=getId(Operator, codespace, str(company_number)), version=version,
                           short_name=MultilingualString(value=company_code),
                           name=MultilingualString(value=company_name))

def footnote_to_availability_condition(zf: ZipFile) -> Generator[AvailabilityCondition, None, None]:
    year, month, day, hour, minute, second = zf.getinfo('footnote.dat').date_time
    with (zf.open('footnote.dat', 'r') as f):
        g = io.TextIOWrapper(f, 'ISO-8859-1')
        operator_ref, from_date, to_date, version, description = parse_delivery(g)
        delta = to_date.to_datetime() - from_date.to_datetime()
        for line in g:
            record_id = iff_slice(line, 1, 1)
            assert record_id == '#'
            footnote_number = int(iff_slice(line, 2, 6))
            line = g.readline().rstrip()
            assert len(line) == (delta.days + 1)

            yield AvailabilityCondition(id=getId(AvailabilityCondition, codespace, str(footnote_number)),
                                        version=version,
                                        valid_day_bits=line, from_date=from_date, to_date=to_date)

def xfootnote_to_availability_condition(zf: ZipFile) -> Generator[AvailabilityCondition, None, None]:
    year, month, day, hour, minute, second = zf.getinfo('xfootnote.dat').date_time
    with (zf.open('xfootnote.dat', 'r') as f):
        g = io.TextIOWrapper(f, 'ISO-8859-1')
        operator_ref, from_date, to_date, version, description = parse_delivery(g)
        delta = to_date.to_datetime() - from_date.to_datetime()
        for line in g:
            record_id = iff_slice(line, 1, 1)
            assert record_id == '#'
            footnote_number = int(iff_slice(line, 2, 6))
            line = g.readline().rstrip()
            assert len(line) == (delta.days + 1)

            yield AvailabilityCondition(id=getId(AvailabilityCondition, codespace, f"X{footnote_number}"),
                                        version=version,
                                        valid_day_bits=line, from_date=from_date, to_date=to_date)


trnsattr_type_of_notice: dict[int, TypeOfNotice] = {
    0: TypeOfNotice(id=getId(TypeOfNotice, codespace, '0'), version="any", description=MultilingualString(value="not in use")),
    1: TypeOfNotice(id=getId(TypeOfNotice, codespace, '1'), version="any", description=MultilingualString(value="search attribute")),
    2: TypeOfNotice(id=getId(TypeOfNotice, codespace, '2'), version="any", description=MultilingualString(value="stretch, attribute is given when at least a part of the journey has the attribute")),
    3: TypeOfNotice(id=getId(TypeOfNotice, codespace, '3'), version="any", description=MultilingualString(value="shrink, attribute is only given when the whole journey has the attribute")),
    4: TypeOfNotice(id=getId(TypeOfNotice, codespace, '4'), version="any", description=MultilingualString(value="non-search attribute")),
    5: TypeOfNotice(id=getId(TypeOfNotice, codespace, '5'), version="any", description=MultilingualString(value="attribute for one stop")),
    6: TypeOfNotice(id=getId(TypeOfNotice, codespace, '6'), version="any", description=MultilingualString(value="boarding only")),
    7: TypeOfNotice(id=getId(TypeOfNotice, codespace, '7'), version="any", description=MultilingualString(value="unboarding only")),
    8: TypeOfNotice(id=getId(TypeOfNotice, codespace, '8'), version="any", description=MultilingualString(value="non-concatenation: this attribute will not be concatenated during processing when multiple occurrences are present on a service. These separate stretches will still be available in the output journeys. Attribute is valid if journey uses only one stretch.")),
    53: TypeOfNotice(id=getId(TypeOfNotice, codespace, '53'), version="any", description=MultilingualString(value="stop attribute connected to departure station")),
    54: TypeOfNotice(id=getId(TypeOfNotice, codespace, '54'), version="any", description=MultilingualString(value="attribute only shown if attribute arrival and departure-station have the connected attributes")),
    55: TypeOfNotice(id=getId(TypeOfNotice, codespace, '55'), version="any", description=MultilingualString(value="stop attribute connected to arrival station")),
}
def trnsattr_to_notice(zf: ZipFile) -> Generator[Notice, None, None]:
    year, month, day, hour, minute, second = zf.getinfo('trnsattr.dat').date_time
    with zf.open('trnsattr.dat', 'r') as f:
        g = io.TextIOWrapper(f, 'ISO-8859-1')
        operator_ref, from_date, to_date, version, description = parse_delivery(g)
        for line in g:
            attribute_code = iff_slice(line, 1, 4)
            processing_code = int(iff_slice(line, 6, 9))
            description = iff_slice(line, 11, 40)

            yield Notice(id=getId(Notice, codespace, str(attribute_code)), version=version,
                         type_of_notice_ref=getRef(trnsattr_type_of_notice[processing_code]),
                         text=MultilingualString(value=str(description)))


def iff_time(iff_time: str):
    if iff_time == '9999':
        return None

    hour = int(iff_time[0:2])
    day_offset = hour // 24
    hour -= (day_offset * 24)
    return XmlTime(hour, int(iff_time[2:4]), second=0, fractional_second=0), day_offset if day_offset > 0 else None


def iff_any_time(t: Tuple[str, str, str], arrival: bool):
    _station_name, arrival_time, departure_time = t
    if arrival:
        if arrival_time is None:
            arrival_time = departure_time
        return arrival_time
    else:
        if departure_time is None:
            departure_time = arrival_time
        return departure_time

import hashlib

def timetbls_to_service_journey(zf: ZipFile) -> Generator[Tuple[ServiceJourney, List[NoticeAssignment], Route, List[RouteLink], Tuple[str, str], List[int]], None, None]:
    def process(service_identification: int, service_numbers: List[Tuple[int, int, str, int, int, str]],
                validity_records: List[Tuple[int, int, int]], transport_mode_records: List[Tuple[int, int, int]],
                attribute_records: List[Tuple[str, int, int]],
                stations: List[List[Tuple]], extra_pairs: Tuple[str, str]
                ) -> Tuple[ServiceJourney, List[NoticeAssignment], Route, List[RouteLink], Tuple[str, str], List[int]]:

        def get_stop_point_ref(station):
            from_station = station[0][0]
            if len(station) > 1:
                from_platform = station[1][1]
                from_stop_point_ref = f"{from_station}-{from_platform}"
            else:
                from_stop_point_ref = f"{from_station}"

            return from_stop_point_ref

        def get_route_hash(stations: List[List[Tuple]], version):
            l = []
            for i in range(0, len(stations)):
                from_stop_point_ref = get_stop_point_ref(stations[i])
                l.append(from_stop_point_ref)
            route_hash = hashlib.md5((';'.join(l)).encode('utf-8')).hexdigest()[0:5]

            points_in_sequence = []
            route_links = []
            for i in range(0, len(l)):
                route_link = None
                if i < len(l) - 1:
                    route_link = RouteLink(id=getId(RouteLink, codespace, f"{l[i]}-{l[i+1]}"), version=version, from_point_ref=getFakeRef(getId(RoutePoint, codespace, l[i]), RoutePointRefStructure, version), to_point_ref=getFakeRef(getId(RoutePoint, codespace, l[i+1]), RoutePointRefStructure, version))
                    route_links.append(route_link)

                points_in_sequence.append(PointOnRoute(id=getId(PointOnRoute, codespace, f"{route_hash}-{i}"), order=i+1, version=version,
                    onward_route_link_ref=getRef(route_link, RouteLinkRefStructure) if route_link is not None else None,
                    point_ref_or_infrastructure_point_ref_or_activation_point_ref_or_timing_point_ref_or_scheduled_stop_point_ref_or_parking_point_ref_or_relief_point_ref_or_route_point_ref=getFakeRef(getId(RoutePoint, codespace, l[i]), RoutePointRef, version)))

            return Route(id=getId(Route, codespace, route_hash), version=version, points_in_sequence=PointsOnRouteRelStructure(point_on_route=points_in_sequence)), route_links

        def get_calls(service_identification: int, stations: List[List[Tuple]]):
            order = 1
            stop_sequence = [station for station in stations if station[0][1] is not None or station[0][2] is not None]
            for i in range(0, len(stop_sequence)):
                arrival_time, arrival_day_offset = iff_time(stop_sequence[i][0][1]) if stop_sequence[i][0][1] is not None else (None, None)
                departure_time, departure_day_offset = iff_time(stop_sequence[i][0][2]) if stop_sequence[i][0][2] is not None else (None, None)

                from_station = stop_sequence[i][0][0]
                if len(stop_sequence[i]) > 1:
                    # Different arrival than departure platform
                    if stop_sequence[i][1][0] != stop_sequence[i][1][1]:
                        from_platform = stop_sequence[i][1][0]
                        from_stop_point_ref = getFakeRef(
                            getId(ScheduledStopPoint, codespace, f"{from_station}-{from_platform}"), ScheduledStopPointRef,
                            version)

                        yield Call(id=getId(TimetabledPassingTime, codespace, f"{service_identification}-{i+1}"), version=version, order=order,
                                   arrival=ArrivalStructure(for_alighting=stop_sequence[i][0][1] != '9999' if stop_sequence[i][0][1] == '9999' else None, time=arrival_time, day_offset=arrival_day_offset) if arrival_time is not None or stop_sequence[i][0][1] == '9999' else None,
                                   fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=from_stop_point_ref
                                   )

                        order += 1

                        from_platform = stop_sequence[i][1][1]
                        from_stop_point_ref = getFakeRef(
                            getId(ScheduledStopPoint, codespace, f"{from_station}-{from_platform}"), ScheduledStopPointRef,
                            version)

                        yield Call(id=getId(TimetabledPassingTime, codespace, f"{service_identification}-{i + 1}"),
                                   version=version, order=order,
                                   departure=DepartureStructure(
                                       for_boarding=stop_sequence[i][0][2] != '9999' if stop_sequence[i][0][
                                                                                            2] == '9999' else None,
                                       time=departure_time, day_offset=departure_day_offset) if departure_time is not None  or
                                                                                                stop_sequence[i][0][
                                                                                                    2] == '9999' else None,
                                   fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=from_stop_point_ref
                                   )

                        order += 1

                        # So we really get an individual call
                        continue
                    else:
                        from_platform = stop_sequence[i][1][0]
                        from_stop_point_ref = getFakeRef(
                            getId(ScheduledStopPoint, codespace, f"{from_station}-{from_platform}"), ScheduledStopPointRef,
                            version)

                else:
                    from_stop_point_ref = getFakeRef(getId(ScheduledStopPoint, codespace, f"{from_station}"),
                                                     ScheduledStopPointRef, version)

                yield Call(id=getId(TimetabledPassingTime, codespace, f"{service_identification}-{i+1}"), version=version, order=order,
                           arrival=ArrivalStructure(for_alighting=stop_sequence[i][0][1] != '9999' if stop_sequence[i][0][1] == '9999' else None, time=arrival_time, day_offset=arrival_day_offset) if arrival_time is not None or stop_sequence[i][0][1] == '9999' else None,
                           departure=DepartureStructure(for_boarding=stop_sequence[i][0][2] != '9999' if stop_sequence[i][0][2] == '9999' else None, time=departure_time, day_offset=departure_day_offset) if departure_time is not None or stop_sequence[i][0][2] == '9999'  else None,
                           fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=from_stop_point_ref
                           )
                order += 1

        # If we hit this assert, we must implement calendar merging, and our future checks (platforms) will be incomplete
        assert len(validity_records) == 1

        notice_assignments = []
        journey_parts = []

        # Stop Sequence without intermediate points (used to reference)
        stop_sequence = [station for station in stations if station[0][1] is not None or station[0][2] is not None]

        stops_len = len(stop_sequence)

        parts = set([])
        for sn in service_numbers:
            first_stop, last_stop, _, _, _, _ = sn
            if first_stop == 0:
                first_stop = 1
            if last_stop == 999:
                last_stop = stops_len
            parts = parts.union({first_stop, last_stop})

        for vr in validity_records:
            first_stop, last_stop, _ = vr
            if first_stop == 0:
                first_stop = 1
            if last_stop == 999:
                last_stop = stops_len
            parts = parts.union({first_stop, last_stop})

        for tm in transport_mode_records:
            first_stop, last_stop, _ = tm
            if first_stop == 0:
                first_stop = 1
            if last_stop == 999:
                last_stop = stops_len
            parts = parts.union({first_stop, last_stop})

        for at in attribute_records:
            first_stop, last_stop, _ = at
            if first_stop == 0:
                first_stop = 1
            if last_stop == 999:
                last_stop = stops_len
            parts = parts.union({first_stop, last_stop})

        parts = sorted(list(parts))

        if len(parts) > 2:
            for i in range(0, len(parts) - 1):
                from_station = stop_sequence[parts[i] - 1][0][0]
                to_station = stop_sequence[parts[i + 1] - 1][0][0]

                start_time, start_time_day_offset = iff_time(iff_any_time(stop_sequence[parts[i] - 1][0], False))
                end_time, end_time_day_offset = iff_time(iff_any_time(stop_sequence[parts[i + 1] - 1][0], True))


                # TODO: IFF allows (albeit not implement validaty on platforms, hence platform validity by day
                # If we hit these asserts, we must implement conditional platforms
                if len(stop_sequence[parts[i] - 1]) > 1:
                    from_platform = stop_sequence[parts[i] - 1][1][1] if len(stop_sequence[parts[i] - 1]) > 0 else None
                    assert stop_sequence[parts[i] - 1][1][2] == validity_records[0][2]
                    from_stop_point_ref = getFakeRef(
                        getId(ScheduledStopPoint, codespace, f"{from_station}-{from_platform}"), ScheduledStopPointRefStructure,
                        version)
                else:
                    from_stop_point_ref = getFakeRef(getId(ScheduledStopPoint, codespace, f"{from_station}"), ScheduledStopPointRefStructure, version)

                if len(stop_sequence[parts[i + 1] - 1]) > 1:
                    to_platform = stop_sequence[parts[i + 1] - 1][1][0]
                    assert stop_sequence[parts[i + 1] - 1][1][2] == validity_records[0][2]
                    to_stop_point_ref = getFakeRef(getId(ScheduledStopPoint, codespace, f"{to_station}-{to_platform}"), ScheduledStopPointRefStructure,
                                                 version)
                else:
                    to_stop_point_ref = getFakeRef(getId(ScheduledStopPoint, codespace, f"{to_station}"),
                                                                                                       ScheduledStopPointRefStructure,
                                                                                                       version)

                train_number = None
                for sn in service_numbers:
                    if sn[0] in range(parts[i], parts[i + 1]):
                        train_number = sn[3]
                        break

                type_of_product_category = None
                for tm in transport_mode_records:
                    if tm[0] in range(parts[i], parts[i + 1]):
                        type_of_product_category = tm[2]
                        transport_mode = get_best_effort_mapping_transport_mode(tm[2])
                        break

                journey_part = JourneyPart(id=getId(JourneyPart, codespace, f"{service_identification}-{parts[i]}-{parts[i + 1]}"), version=version,
                            order = i + 1,
                            start_time=start_time,
                            start_time_day_offset=start_time_day_offset,
                            end_time=end_time,
                            end_time_day_offset = end_time_day_offset,
                            from_stop_point_ref=from_stop_point_ref, to_stop_point_ref=to_stop_point_ref,
                            type_of_product_category_ref=getFakeRef(getId(TypeOfProductCategory, codespace, str(type_of_product_category)), TypeOfProductCategoryRef, version) if type_of_product_category is not None else None,
                            train_number_ref=getFakeRef(getId(TrainNumber, codespace, str(train_number)), TrainNumberRef, version) if train_number is not None else None)

                journey_parts.append(journey_part)

                for at in attribute_records:
                    if at[0] in range(parts[i], parts[i + 1]):
                        notice_assignments.append(NoticeAssignment(id=getId(NoticeAssignment, codespace, f"{service_identification}-{parts[i]}-{parts[i + 1]}-{at[2]}"), version=version, order=1,
                                                                   notice_ref_or_group_of_notices_ref_or_notice=getFakeRef(getId(Notice, codespace, str(at[2])), NoticeRef, version),
                                                                   noticed_object_ref=getRef(journey_part, VersionOfObjectRefStructure)))


        train_number_int = []
        train_number_refs = []
        for sn in service_numbers:
            train_number_refs.append(getFakeRef(getId(TrainNumber, codespace, str(sn[3])), TrainNumberRef, version))
            train_number_int.append(sn[3])

        type_of_product_category = None
        transport_mode = None
        for tm in transport_mode_records:
            if tm[0] == 1 and tm[1] == stops_len:
                type_of_product_category = tm[2]
                transport_mode = get_best_effort_mapping_transport_mode(tm[2])
                break

        route, route_links = get_route_hash(stations, version)

        service_journey = ServiceJourney(
            id=getId(ServiceJourney, codespace, str(service_identification)), version=version,
            operator_ref_or_operator_view=getFakeRef(getId(Operator, codespace, str(service_numbers[0][2])), OperatorRef, version),
            validity_conditions_or_valid_between=[ValidityConditionsRelStructure(choice=[getFakeRef(getId(AvailabilityCondition, codespace, str(validity_record[0])), AvailabilityConditionRef, version) for validity_record in validity_records])],
            parts=JourneyPartsRelStructure(journey_part_ref_or_journey_part=journey_parts) if len(journey_parts) > 0 else None,
            type_of_product_category_ref=getFakeRef(getId(TypeOfProductCategory, codespace, str(type_of_product_category)), TypeOfProductCategoryRef,
                                                    version) if type_of_product_category is not None else None,
            train_numbers=TrainNumberRefsRelStructure(train_number_ref=train_number_refs) if len(train_number_refs) > 0 else None,
            transport_mode=transport_mode,
            calls=CallsRelStructure(call=list(get_calls(service_identification, stations))),
            route_ref=getRef(route)
        )

        for at in attribute_records:
            if at[0] == 1 and at[1] == stops_len:
                notice_assignments.append(NoticeAssignment(id=getId(NoticeAssignment, codespace, f"{service_identification}-{at[2]}"),
                                                           version=version, order=1,
                                                           notice_ref_or_group_of_notices_ref_or_notice=getFakeRef(getId(Notice, codespace, str(at[2])), NoticeRef, version), noticed_object_ref=getRef(service_journey, VersionOfObjectRefStructure)))

        return service_journey, notice_assignments, route, route_links, extra_pairs, train_number_int

    year, month, day, hour, minute, second = zf.getinfo('timetbls.dat').date_time
    with zf.open('timetbls.dat', 'r') as f:
        g = io.TextIOWrapper(f, 'ISO-8859-1')
        operator_ref, from_date, to_date, version, description = parse_delivery(g)
        service_identification = None
        service_numbers = []
        validity_records = []
        transport_mode_records = []
        attribute_records = []
        stations = []
        extra_pairs = set([])

        for line in g:
            record_id = iff_slice(line, 1, 1)

            match record_id:
                case '#':
                    # This announces a new transport service
                    if service_identification is not None:
                        yield process(service_identification, service_numbers, validity_records, transport_mode_records, attribute_records, stations, extra_pairs)

                    service_identification = int(iff_slice(line, 2, 9))
                    service_numbers = []
                    validity_records = []
                    transport_mode_records = []
                    attribute_records = []
                    stations = []
                    extra_pairs = set([])

                case '%':
                    # Service Number record
                    company_number = int(iff_slice(line, 2, 4))
                    service_number = int(iff_slice(line, 6, 10))
                    variant_or_line_code = iff_slice(line, 12, 17)
                    first_stop = int(iff_slice(line, 19, 21))
                    last_stop = int(iff_slice(line, 23, 25))
                    service_name = iff_slice(line, 27, 57)

                    service_numbers.append((first_stop, last_stop, company_number, service_number, variant_or_line_code, service_name,))

                case '-':
                    # Validity Record
                    footnote_number = int(iff_slice(line, 2, 6))
                    first_stop = int(iff_slice(line, 8, 10))
                    last_stop = int(iff_slice(line, 12, 14))

                    validity_records.append((first_stop, last_stop, footnote_number))

                case '&':
                    # Transport Mode Record
                    transport_mode_code = iff_slice(line, 2, 5)
                    first_stop = int(iff_slice(line, 7, 9))
                    last_stop = int(iff_slice(line, 11, 13))

                    transport_mode_records.append((first_stop, last_stop, transport_mode_code))

                case '*':
                    # Attribute Record
                    attribute_code = iff_slice(line, 2, 5)
                    first_stop = int(iff_slice(line, 7, 9))
                    last_stop = int(iff_slice(line, 11, 13))

                    attribute_records.append((first_stop, last_stop, attribute_code))

                case '>':
                    # Start Record
                    station_short_name = iff_slice(line, 2, 8)
                    departure_time = iff_slice(line, 10, 13)

                    stations.append([(station_short_name, None, departure_time)])

                case '.':
                    # Continuation Record
                    station_short_name = iff_slice(line, 2, 8)
                    departure_time = iff_slice(line, 10, 13)

                    stations.append([(station_short_name, departure_time, departure_time)])

                case ';':
                    # Passing Record
                    station_short_name = iff_slice(line, 2, 8)
                    stations.append([(station_short_name, None, None)])

                case '+':
                    # Interval Record
                    station_short_name = iff_slice(line, 2, 8)
                    arrival_time = iff_slice(line, 10, 13)
                    departure_time = iff_slice(line, 15, 18)

                    stations.append([(station_short_name, arrival_time, departure_time)])

                case '?':
                    # Platform Record
                    arr_platform_name = iff_slice(line, 2, 6)
                    dep_platform_name = iff_slice(line, 8, 12)
                    footnote_number = int(iff_slice(line, 14, 18))

                    stations[-1].append((arr_platform_name, dep_platform_name, footnote_number))
                    extra_pairs.add((stations[-1][0][0], arr_platform_name))
                    extra_pairs.add((stations[-1][0][0], dep_platform_name))

                case '<':
                    # Final Record, platform may follow
                    station_short_name = iff_slice(line, 2, 8)
                    arrival_time = iff_slice(line, 10, 13)
                    stations.append([(station_short_name, arrival_time, None)])

        if service_identification is not None:
            yield process(service_identification, service_numbers, validity_records, transport_mode_records,
                    attribute_records, stations, extra_pairs)

def map_connection_certainty(possibility: int):
    match possibility:
        case 0:
            return ConnectionCertaintyEnumeration.NEVER_GUARANTEED
        case 1:
            return ConnectionCertaintyEnumeration.NORMALLY_GUARANTEED
        case 2:
            return ConnectionCertaintyEnumeration.GUARANTEED


def changes_to_service_journey_interchange(zf: ZipFile, service_journeys: Dict[str, ServiceJourney]) -> Generator[ServiceJourneyInterchange, None, None]:
    year, month, day, hour, minute, second = zf.getinfo('changes.dat').date_time
    with zf.open('changes.dat', 'r') as f:
        g = io.TextIOWrapper(f, 'ISO-8859-1')
        operator_ref, from_date, to_date, version, description = parse_delivery(g)
        station_short_name = None
        dedup = {}
        for line in g:
            match line[0]:
                case '#':
                    station_short_name = iff_slice(line, 2, 8)
                case '-':
                    from_service = int(iff_slice(line, 2, 9))
                    to_service = int(iff_slice(line, 11, 18))
                    possible = int(iff_slice(line, 20, 21))

                    key = f"{station_short_name}_{from_service}_{to_service}"
                    value = dedup.get(key, 0)
                    if possible >= value:
                        dedup[key] = possible

        for key, possible in dedup.items():
            station_short_name, from_service, to_service = key.split('_')
            from_service_journey = service_journeys[getId(ServiceJourney, codespace, str(from_service))]
            to_service_journey = service_journeys[getId(ServiceJourney, codespace, str(to_service))]
            ssp_ref = getId(ScheduledStopPoint, codespace, station_short_name)

            # Om dit correct te doen, zouden we de rit moeten aflopen, en daar bepalen welke ssp (dus incl. platform het om gaat)
            from_ssp = [call.fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view for call in from_service_journey.calls.call if call.fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view.ref == ssp_ref or call.fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view.ref.startswith(ssp_ref + '-')][0]
            to_ssp = [call.fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view for call in from_service_journey.calls.call if call.fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view.ref == ssp_ref or call.fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view.ref.startswith(ssp_ref + '-')][-1]

            yield ServiceJourneyInterchange(id=getId(ServiceJourneyInterchange, codespace, f"{station_short_name}-{from_service}-{to_service}"),
                                            version=version,
                                            from_journey_ref=getRef(from_service_journey, VehicleJourneyRefStructure),
                                            to_journey_ref=getRef(to_service_journey, VehicleJourneyRefStructure),
                                            planned=possible in (1, 2),
                                            guaranteed=possible == 2,
                                            connection_certainty=map_connection_certainty(possible),
                                            from_point_ref=getFakeRef(from_ssp.ref, ScheduledStopPointRefStructure, from_ssp.version),
                                            to_point_ref=getFakeRef(to_ssp.ref, ScheduledStopPointRefStructure, to_ssp.version)
                                            )



def delivery_to_publication_delivery(zf: ZipFile) -> PublicationDelivery:
    stop_places = []
    route_points = []
    scheduled_stop_points = []
    default_interchanges = []
    passenger_stop_assignments = []


    notices = list(trnsattr_to_notice(zf))

    service_journeys = {}
    notice_assignments = []
    routes = {}
    route_links = {}
    extra_quays: Dict[str, Set[str]] = {}
    train_numbers: Set[int] = set([])
    for sj, nas, route, myroute_links, extra_pairs, my_train_numbers in timetbls_to_service_journey(zf):
        service_journeys[sj.id] = sj
        notice_assignments += nas
        routes[route.id] = route
        for route_link in myroute_links:
            route_links[route_link.id] = route_link
        for pair in extra_pairs:
            if pair[0] in extra_quays:
                extra_quays[pair[0]].add(pair[1])
            else:
                extra_quays[pair[0]] = {pair[1]}
        train_numbers = train_numbers.union(my_train_numbers)


    for stop_place, my_route_points, my_scheduled_stop_points, my_default_interchanges, my_passenger_stop_assignments in stations_to_stopplace(zf, extra_quays):
        stop_places.append(stop_place)
        route_points += my_route_points
        scheduled_stop_points += my_scheduled_stop_points
        default_interchanges += my_default_interchanges
        passenger_stop_assignments += my_passenger_stop_assignments


    availability_conditions = list(footnote_to_availability_condition(zf)) + list(xfootnote_to_availability_condition(zf))

    type_of_product_category = list(trnsmode_to_type_of_product_category(zf))
    operators = list(company_to_operator(zf))

    service_journey_interchanges = list(changes_to_service_journey_interchange(zf, service_journeys))
    interchange_rules = list(xchanges(zf))

    # my_zip.getinfo(screenshot_filename).date_time
    year, month, day, hour, minute, second = zf.getinfo('delivery.dat').date_time
    with zf.open('delivery.dat', 'r') as f:
        g = io.TextIOWrapper(f, 'ISO-8859-1')
        operator_ref, from_date, to_date, version, description = parse_delivery(g)

        train_numbers_element = [TrainNumber(id=getId(TrainNumber, codespace, str(tn)), version=version,
                                     description=MultilingualString(value=str(tn))) for tn in train_numbers]

        operator = [operator for operator in operators if operator.id == operator_ref.ref][0]

        data_source = project(operator, DataSource)

        return PublicationDelivery(publication_timestamp=XmlDateTime.from_datetime(datetime.datetime(year, month, day, hour, minute, second, 0, tzinfo=tz)),
                                   participant_ref=ParticipantRef(value=operator_ref.ref), description=description,
                                   version="ntx:1.1",
                                   data_objects=DataObjectsRelStructure(choice=[
                                       CompositeFrame(id=getId(CompositeFrame, codespace, "IFF"), version=str(version),
                                                      codespaces=CodespacesRelStructure(codespace_ref_or_codespace=[codespace]),
                                                      frame_defaults=VersionFrameDefaultsStructure(
                                                          default_codespace_ref=getRef(codespace, CodespaceRefStructure),
                                                          default_data_source_ref=getRef(data_source, DataSourceRefStructure),
                                                          default_locale=LocaleStructure(time_zone="Europe/Amsterdam",
                                                                                         default_language="nl"),
                                                          default_location_system="EPSG:28992",
                                                          default_system_of_units=SystemOfUnits.SI_METRES,
                                                          default_currency="EUR",
                                                      ),

                                                      validity_conditions_or_valid_between=[ValidBetween(
                                           from_date=from_date,
                                           to_date=to_date)
                                   ],
                                                      frames=FramesRelStructure(common_frame=[
                                                          iff_resourceframe(type_of_product_category, operators, data_source, from_date, to_date, version),
                                                          iff_siteframe(stop_places, from_date, to_date, version),
                                                          iff_serviceframe(scheduled_stop_points, passenger_stop_assignments, list(routes.values()), route_points, list(route_links.values()), notices, notice_assignments, from_date, to_date, version),
                                                          iff_timetableframe(list(service_journeys.values()), availability_conditions, default_interchanges, service_journey_interchanges, interchange_rules, train_numbers_element, from_date, to_date, version)
                                                      ])

                                                      )]))



with ZipFile('/tmp/ns-latest.zip') as zf:

    # list(stations_to_stopplace(zf, {}))
    # country_to_country(zf)
    # trnsmode_to_type_of_product_category(zf)
    # op = list(company_to_operator(zf))

    # footnote_to_uic_operating_period(zf)
    # xfootnote_to_uic_operating_period(zf)

    publication_delivery = delivery_to_publication_delivery(zf)

    ns_map = {'': 'http://www.netex.org.uk/netex', 'gml': 'http://www.opengis.net/gml/3.2'}
    serializer_config = SerializerConfig(ignore_default_attributes=True)
    serializer_config.pretty_print = True
    serializer_config.ignore_default_attributes = True
    serializer = XmlSerializer(config=serializer_config)

    with open('netex-output/iff.xml', 'w', encoding='utf-8') as out:
        serializer.write(out, publication_delivery, ns_map)

