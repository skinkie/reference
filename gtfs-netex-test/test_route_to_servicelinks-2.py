import datetime
import sys
from typing import List

import duckdb

from netex import ServiceJourneyPattern, Route, ScheduledStopPoint, Codespace, ServiceLink, StopPlace, \
    PassengerStopAssignment, Quay, EquipmentPlace, AccessSpace, Authority, TariffZone, Line, ResponsibilitySet, \
    RouteLink, ServiceJourney
from netexio.dbaccess import load_local, load_generator, write_generator, write_objects, get_interesting_classes
from refs import getRef
from routesprofile import RoutesProfile
from transformers.direction import infer_directions_from_sjps_and_apply
from transformers.projection import get_transformer_by_srs_name, project_linestring2, project_location_4326, \
    project_polygon

generator_defaults = {'codespace': Codespace(xmlns='OPENOV'), 'version': 1}

with duckdb.connect(sys.argv[1], read_only=True) as con:
    with duckdb.connect(sys.argv[2], read_only=False) as con_write:
        """
        route_point_projection = {}
        for ssp in load_generator(con, ScheduledStopPoint):
            route_point_ref = list(RoutesProfile.route_point_projection(ssp))[0]
            route_point_projection[getRef(ssp).ref] = route_point_ref

        for sjp in load_generator(con, ServiceJourneyPattern):
            sjp: ServiceJourneyPattern
            route: Route = load_local(con, Route, filter=sjp.route_ref_or_route_view.ref)[0]
            write_generator(con_write, ServiceLink, RoutesProfile.projectRouteToServiceLinks(con, sjp, route, route_point_projection, generator_defaults))
            write_objects(con_write, [sjp])g

        infer_directions_from_sjps_and_apply(sys.argv[2], sys.argv[2], generator_defaults)

        # Rewrite in Generator approach
        crs_to = 'urn:ogc:def:crs:EPSG::4326'
        for sl in load_generator(con_write, ServiceLink):
            sl: ServiceLink
            if sl.line_string:
                transformer = get_transformer_by_srs_name(sl.line_string, crs_to)
                project_linestring2(transformer, sl.line_string)
                sl.line_string.srs_name = crs_to
                sl.line_string.pos_or_point_property_or_pos_list[0].srs_name = crs_to
                write_objects(con_write, [sl], cursor=True)
        """
        """
        for sp in load_generator(con, StopPlace):
            sp: StopPlace
            project_location_4326(sp.centroid.location)
            for q in sp.quays.taxi_stand_ref_or_quay_ref_or_quay:
                if isinstance(q, Quay):
                    q: Quay
                    if q.centroid is not None and q.centroid.location is not None:
                        project_location_4326(q.centroid.location)
                    elif q.polygon_or_multi_surface:
                        project_polygon(q.polygon_or_multi_surface, crs_to)
                    else:
                        print('NO Location: ' + q.id)

                    if q.equipment_places is not None:
                        for ep in q.equipment_places.equipment_place_ref_or_equipment_place:
                            if isinstance(ep, EquipmentPlace):
                                if ep.centroid is not None and ep.centroid.location is not None:
                                    project_location_4326(ep.centroid.location)
                                elif ep.polygon_or_multi_surface:
                                    project_polygon(ep.polygon_or_multi_surface, crs_to)

            if sp.equipment_places is not None:
                for ep in sp.equipment_places.equipment_place_ref_or_equipment_place:
                    if isinstance(ep, EquipmentPlace):
                        if ep.centroid is not None and ep.centroid.location is not None:
                            project_location_4326(ep.centroid.location)
                        elif ep.polygon_or_multi_surface:
                            project_polygon(ep.polygon_or_multi_surface, crs_to)

            if sp.access_spaces is not None:
                for asp in sp.access_spaces.access_space_ref_or_access_space:
                    if isinstance(asp, AccessSpace):
                        if asp.centroid is not None and asp.centroid.location is not None:
                            project_location_4326(asp.centroid.location)
                        elif asp.polygon_or_multi_surface:
                            project_polygon(asp.polygon_or_multi_surface, crs_to)

            write_objects(con_write, [sp], cursor=True)

        sp = load_local(con, StopPlace, limit=1)[0]

        for psa in load_generator(con, PassengerStopAssignment):
            psa: PassengerStopAssignment
            psa.taxi_stand_ref_or_quay_ref_or_quay.ref = psa.taxi_stand_ref_or_quay_ref_or_quay.ref.replace('NL:Q:', 'NL:CHB:Quay:')
            psa.taxi_rank_ref_or_stop_place_ref_or_stop_place.version = sp.version
            write_objects(con_write, [psa], cursor=True)
        """

        """
        for tz in load_generator(con, TariffZone):
            tz.id = 'DOVA:TariffZone:' + tz.id
            write_objects(con_write, [tz], cursor=True)

        for ssp in load_generator(con_write, ScheduledStopPoint):
            ssp: ScheduledStopPoint
            if ssp.tariff_zones:
                for tz in ssp.tariff_zones.tariff_zone_ref:
                    tz.version = 'any'

            write_objects(con_write, [ssp], cursor=True)

        for line in load_generator(con_write, Line):
            line: Line
            if line.authority_ref:
                line.authority_ref.version = 'any'
                write_objects(con_write, [line], cursor=True)

        for responsibilityset in load_generator(con, ResponsibilitySet):
            responsibilityset: ResponsibilitySet
            for role in responsibilityset.roles.responsibility_role_assignment:
                if role.responsible_organisation_ref and role.responsible_organisation_ref.version is None:
                    role.responsible_organisation_ref.version = 'any'
                if role.responsible_area_ref and role.responsible_area_ref.version is None:
                    role.responsible_area_ref.version = 'any'

            write_objects(con_write, [responsibilityset], cursor=True)
        """

        con_write.execute("SET wal_autocheckpoint='1TB';")
        sjs = []

        count = 0 
        for sj in load_generator(con_write, ServiceJourney):
            sj: ServiceJourney
            sj.time_demand_type_ref = None
            count += 1

            sjs.append(sj)

            if (count % 1000) == 0:
                write_objects(con_write, sjs)
                sjs = []
                print(count)
                con_write.execute("CHECKPOINT;")

        if len(sjs) > 0:
            write_objects(con_write, sjs, cursor=True)

        """
        for rl in load_generator(con, RouteLink):
            rl: RouteLink
            rl.line_string = None
            rl.operational_context_ref = None
            write_objects(con_write, [rl], cursor=True)
        """
