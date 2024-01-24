from typing import List

from xsdata.models.datatype import XmlDateTime

from netex import Codespace, DataSource, Version, VehicleJourney, TimetableFrame, ServiceJourney, ServiceJourneyPattern, \
    ServiceFrame, ResourceFrame, PublicationDelivery, Line, MultilingualString, DataObjectsRelStructure, \
    JourneysInFrameRelStructure
from timetabledpassingtimesprofile import TimetablePassingTimesProfile


class NordicProfile:
    codespace: Codespace
    data_source: DataSource
    version: Version

    def __init__(self, codespace: Codespace, data_source: DataSource, version: Version):
        self.codespace = codespace
        self.data_source = data_source
        self.version = version

    def getDataSources(self, data_sources: List[DataSource]) -> List[DataSource]:
        return data_sources

    def getTimetableFrame(self, line: Line, service_journeys: List[ServiceJourney]) -> TimetableFrame:
        return TimetableFrame(id=line.id.replace("Line", "TimetableFrame"), vehicle_journeys=JourneysInFrameRelStructure(choice=service_journeys))

    def getLineDelivery(self, line: Line, resource_frame: [ResourceFrame], service_frame: [ServiceFrame], timetable_frame: [TimetableFrame]) -> PublicationDelivery:
        return PublicationDelivery(version="1.08:NO-NeTEx-networktimetable:1.3",
                                   publication_timestamp=XmlDateTime.now(),
                                   participant_ref="PyNeTExConv",
                                   description=line.description,
                                   data_objects=DataObjectsRelStructure(choice=resource_frame + service_frame + timetable_frame)
                                   )
