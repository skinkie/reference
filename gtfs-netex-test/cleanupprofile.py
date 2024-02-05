from netex import JourneyPattern, StopPointInJourneyPattern


class CleanupProfile:
    @staticmethod
    def firstAndLastStop(journey_pattern: JourneyPattern):
        for pis in journey_pattern.points_in_sequence.point_in_journey_pattern_or_stop_point_in_journey_pattern_or_timing_point_in_journey_pattern:
            if isinstance(pis, StopPointInJourneyPattern):
                pis.for_alighting = False
                break

        for pis in reversed(journey_pattern.points_in_sequence.point_in_journey_pattern_or_stop_point_in_journey_pattern_or_timing_point_in_journey_pattern):
            if isinstance(pis, StopPointInJourneyPattern):
                pis.for_boarding = False
                break

