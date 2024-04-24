from typing import List

from netex import Codespace, ScheduledStopPoint, StopPlace, SiteFrame, StopPlacesInFrameRelStructure, \
    PassengerStopAssignment, StopPlaceRef, SimplePointVersionStructure, StopTypeEnumeration, QuaysRelStructure, Quay, \
    QuayTypeEnumeration, QuayRef, TypeOfFrameRef
from refs import getId, getRef


class SiteFrameEPIP:
    codespace: Codespace
    @staticmethod
    def getQuay(scheduled_stop_point: ScheduledStopPoint):
        quay = Quay(id=scheduled_stop_point.id.replace('ScheduledStopPoint', 'Quay'),
                    version=scheduled_stop_point.version,
                    derived_from_object_ref=scheduled_stop_point.id,
                    derived_from_version_ref_attribute=scheduled_stop_point.version,
                    name=scheduled_stop_point.name,
                    name_suffix=scheduled_stop_point.name_suffix,
                    alternative_texts=scheduled_stop_point.alternative_texts,
                    centroid=SimplePointVersionStructure(location=scheduled_stop_point.location),
                    quay_type=QuayTypeEnumeration.BUS_STOP)
        return quay

    @staticmethod
    def getStopPlace(scheduled_stop_point: ScheduledStopPoint):
        stop_place = StopPlace(id=scheduled_stop_point.id.replace('ScheduledStopPoint', 'StopPlace'),
                               version=scheduled_stop_point.version,
                               derived_from_object_ref=scheduled_stop_point.id,
                               derived_from_version_ref_attribute=scheduled_stop_point.version,
                               name=scheduled_stop_point.name,
                               name_suffix=scheduled_stop_point.name_suffix,
                               alternative_texts=scheduled_stop_point.alternative_texts,
                               centroid=SimplePointVersionStructure(location=scheduled_stop_point.location),
                               stop_place_type=StopTypeEnumeration.BUS_STATION,
                               quays=QuaysRelStructure(taxi_stand_ref_or_quay_ref_or_quay=[SiteFrameEPIP.getQuay(scheduled_stop_point)])
                               )
        return stop_place
    @staticmethod
    def getStopPlaces(scheduled_stop_points: List[ScheduledStopPoint]):
        return [SiteFrameEPIP.getStopPlace(scheduled_stop_point) for scheduled_stop_point in scheduled_stop_points]


    @staticmethod
    def getPassengerStopAssignment(scheduled_stop_point: ScheduledStopPoint):
        return PassengerStopAssignment(id=scheduled_stop_point.id.replace('ScheduledStopPoint', 'PassengerStopAssignment'),
                                version=scheduled_stop_point.version,
                                order=1,
                                fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point=getRef(scheduled_stop_point),
                                taxi_rank_ref_or_stop_place_ref_or_stop_place=StopPlaceRef(ref=scheduled_stop_point.id.replace('ScheduledStopPoint', 'StopPlace'), version=scheduled_stop_point.version),
                                taxi_stand_ref_or_quay_ref_or_quay=QuayRef(ref=scheduled_stop_point.id.replace('ScheduledStopPoint', 'Quay'), version=scheduled_stop_point.version)
                                )
    @staticmethod
    def getPassengerStopAssignments(scheduled_stop_points: List[ScheduledStopPoint]):
        return [SiteFrameEPIP.getPassengerStopAssignment(scheduled_stop_point) for scheduled_stop_point in scheduled_stop_points]

    def getSiteFrame(self, scheduled_stop_points: List[ScheduledStopPoint]):
        site_frame = SiteFrame(id=getId(SiteFrame, self.codespace, "SiteFrame"),
                               version=scheduled_stop_points[0].version,
                               type_of_frame_ref=TypeOfFrameRef(ref="epip:EU_PI_STOP", version_ref="1.0"),
                               stop_places=StopPlacesInFrameRelStructure(stop_place=SiteFrameEPIP.getStopPlaces(scheduled_stop_points)))
        return site_frame


    def __init__(self, codespace: Codespace):
        self.codespace = codespace