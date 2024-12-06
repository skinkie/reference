import sys
from typing import List

import duckdb

from netex import ServiceJourneyPattern, Route, ScheduledStopPoint, Codespace
from netexio.dbaccess import load_local, load_generator
from refs import getRef
from routesprofile import RoutesProfile
from transformers.direction import infer_directions_from_sjps_and_apply

generator_defaults = {'codespace': Codespace(xmlns='OPENOV'), 'version': 1}

with duckdb.connect(sys.argv[1]) as con:
    sjp: ServiceJourneyPattern = load_local(con, ServiceJourneyPattern, limit=1)[0]
    route: Route = load_local(con, Route, filter=sjp.route_ref_or_route_view.ref)[0]

    route_point_projection = {}
    for ssp in load_generator(con, ScheduledStopPoint):
        route_point_ref = list(RoutesProfile.route_point_projection(ssp))[0]
        route_point_projection[getRef(ssp).ref] = route_point_ref

    sls = list(RoutesProfile.projectRouteToServiceLinks(con, sjp, route, route_point_projection, generator_defaults))


    pass