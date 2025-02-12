from itertools import groupby
from typing import Optional

from aux_logging import log_once
from netex import Direction, Line, LineRef, ServiceJourneyRef, ServiceJourney, RouteRef, ServiceJourneyPatternRef, \
    ServiceJourneyPattern, ScheduledStopPointRef, StopPointInJourneyPattern, StopPlaceRef, StopPlace, RouteView, \
    DirectionRefStructure
from netexio.database import Database
from netexio.dbaccess import load_references_inwards_generator, get_single, write_objects
from refs import getRef
from transformers.embedding import embedding_update
from transformers.site_frame import index_scheduled_stopplace

import re
import copy

from utils import project

def test_iterator(db_read: Database):
    if True:
        new_line_ids = {}
        old_line_ids = set()
        directions = {}

        index_ssp_sp = {sp_ref: ssp_ref for sp_ref, ssp_ref in index_scheduled_stopplace(db_read)}

        prev_new_line_id = None
        prev_direction: Optional[Direction] = None
        for line_ref, group in groupby(load_references_inwards_generator(db_read, Line, cursor=True), key=lambda x: x[0]):
            line = get_single(db_read, Line, line_ref.ref, line_ref.version, True)
            line_new_id = re.sub(r'_\d+$', '', line.id)
            old_line_ids.add(line.id)
            if line_new_id not in new_line_ids:
                new_line = copy.deepcopy(line)
                new_line.id = line_new_id
                new_line.private_codes = None
                new_line_ids[new_line.id] = new_line # This might get big
                new_line_ref: LineRef = getRef(new_line)
            else:
                new_line = new_line_ids[line_new_id]
                new_line_ref: LineRef = getRef(new_line)

            if True:
                for _, reference in group:
                    # klass = getClassFromRefClass(reference)
                    if isinstance(reference, ServiceJourneyRef):
                        sj: ServiceJourney = get_single(db_read, ServiceJourney, reference.ref, reference.version, True)
                        if isinstance(sj.flexible_line_ref_or_line_ref_or_line_view_or_flexible_line_view, LineRef):
                            sj.flexible_line_ref_or_line_ref_or_line_view_or_flexible_line_view = new_line_ref
                            write_objects(db_read, [sj], silent=True, cursor=True)

                    elif isinstance(reference, RouteRef):
                        for key2, group2 in groupby(load_references_inwards_generator(db_read, filter=reference.ref, cursor=True), key=lambda y: y[0]):
                            for reference2 in group2:
                                # klass = getClassFromRefClass(reference)
                                # If the class is route, we would likely have ServiceJourneyPatterns pointing into a Direction by a DirectionType
                                if reference2 is ServiceJourneyPatternRef:
                                    sjp = get_single(db_read, ServiceJourneyPattern, reference2.ref, reference2.version, True)

                                    if sjp.direction_type is not None: # and sjp.direction_ref_or_direction_view is None:
                                        # Should we use DestinationDisplay or the Last Stop, or the StopPlace of the last stop?
                                        last_stop_ref: ScheduledStopPointRef = None
                                        for stop in reversed(
                                                sjp.points_in_sequence.point_in_journey_pattern_or_stop_point_in_journey_pattern_or_timing_point_in_journey_pattern):
                                            if isinstance(stop, StopPointInJourneyPattern):
                                                # TODO: get the stopplace of the last stop, so more patterns can use the same Direction
                                                last_stop_ref = stop.scheduled_stop_point_ref
                                                break

                                        if last_stop_ref is not None:
                                            last_sp_ref: StopPlaceRef = index_ssp_sp[last_stop_ref]
                                            last_sp: StopPlace = get_single(db_read, StopPlace, last_sp_ref.ref, last_sp_ref.version, True)
                                            if isinstance(sjp.route_ref_or_route_view, RouteView):
                                                sjp.route_ref_or_route_view.flexible_line_ref_or_line_ref_or_line_view = new_line_ref

                                            direction: Direction = project(line, Direction)
                                            if direction.id not in directions:
                                                direction.direction_type = sjp.direction_type.value
                                                direction.name = last_sp.name
                                                direction.short_name = last_sp.short_name
                                                directions[direction.id] = direction

                                                # TODO: Technically we might want to check the first stop, but since we only do inbound and outbound...
                                                if prev_direction and prev_new_line_id == line_new_id:
                                                    prev_direction.opposite_direction_ref = getRef(direction, DirectionRefStructure)
                                                    direction.opposite_direction_ref = getRef(prev_direction, DirectionRefStructure)
                                                else:
                                                    prev_direction = direction
                                                    prev_new_line_id = line_new_id

                                            else:
                                                direction = directions[direction.id]

                                            sjp.direction_ref_or_direction_view = getRef(direction)
                                            write_objects(db_read, [sjp], silent=True, cursor=True)
                        else:
                            log_once(
                                f"{sjp.id} does not have point in sequence which meets the StopPointInJourneyPattern criteria")

                    elif isinstance(reference, ServiceJourneyPatternRef):
                        sjp = get_single(db_read, ServiceJourneyPattern, reference.ref, reference.version, True)
                        # print(line_ref.ref, sjp.id, sjp.direction_type)

                        if sjp.direction_type is not None: # and sjp.direction_ref_or_direction_view is None:
                            # Should we use DestinationDisplay or the Last Stop, or the StopPlace of the last stop?
                            last_stop_ref: ScheduledStopPointRef = None
                            for stop in reversed(
                                    sjp.points_in_sequence.point_in_journey_pattern_or_stop_point_in_journey_pattern_or_timing_point_in_journey_pattern):
                                if isinstance(stop, StopPointInJourneyPattern):
                                    # TODO: get the stopplace of the last stop, so more patterns can use the same Direction
                                    last_stop_ref = stop.scheduled_stop_point_ref
                                    break

                            if last_stop_ref is not None:
                                last_sp_ref: StopPlaceRef = index_ssp_sp[last_stop_ref]
                                last_sp: StopPlace = get_single(db_read, StopPlace, last_sp_ref.ref, last_sp_ref.version, True)
                                if isinstance(sjp.route_ref_or_route_view, RouteView):
                                    sjp.route_ref_or_route_view.flexible_line_ref_or_line_ref_or_line_view = new_line_ref

                                direction: Direction = project(line, Direction)
                                if direction.id not in directions:
                                    direction.direction_type = sjp.direction_type.value
                                    direction.name = last_sp.name
                                    direction.short_name = last_sp.short_name
                                    directions[direction.id] = direction

                                    # TODO: Technically we might want to check the first stop, but since we only do inbound and outbound...
                                    if prev_direction and prev_new_line_id == line_new_id:
                                        prev_direction.opposite_direction_ref = getRef(direction, DirectionRefStructure)
                                        direction.opposite_direction_ref = getRef(prev_direction, DirectionRefStructure)
                                    else:
                                        prev_direction = direction
                                        prev_new_line_id = line_new_id
                                else:
                                    direction = directions[direction.id]

                                sjp.direction_ref_or_direction_view = getRef(direction)
                                write_objects(db_read, [sjp], silent=True, cursor=True)

        write_objects(db_read, list(directions.values()), empty=True, many=True, cursor=True)
        write_objects(db_read, list(new_line_ids.values()), empty=True, many=True, cursor=True)
    embedding_update(db_read, filter_clazz = [ServiceJourneyPattern, Direction, Line, ServiceJourney])


if __name__ == '__name__':
    import sys
    with Database(sys.argv[0], read_only=False) as db:
        test_iterator(db)