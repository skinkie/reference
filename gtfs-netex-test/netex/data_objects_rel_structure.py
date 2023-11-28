from dataclasses import dataclass, field
from typing import List
from netex.driver_schedule_frame import DriverScheduleFrame
from netex.entities_in_version_rel_structure import (
    CompositeFrame,
    GeneralFrame,
)
from netex.fare_frame import FareFrame
from netex.infrastructure_frame import InfrastructureFrame
from netex.mobility_journey_frame import MobilityJourneyFrame
from netex.mobility_service_frame import MobilityServiceFrame
from netex.resource_frame import ResourceFrame
from netex.sales_transaction_frame import SalesTransactionFrame
from netex.service_calendar_frame import ServiceCalendarFrame
from netex.service_frame import ServiceFrame
from netex.site_frame import SiteFrame
from netex.timetable_frame import TimetableFrame
from netex.vehicle_schedule_frame import VehicleScheduleFrame

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DataObjectsRelStructure:
    """
    Type for a list of objects.
    """
    class Meta:
        name = "dataObjects_RelStructure"

    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "CompositeFrame",
                    "type": CompositeFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MobilityJourneyFrame",
                    "type": MobilityJourneyFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MobilityServiceFrame",
                    "type": MobilityServiceFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesTransactionFrame",
                    "type": SalesTransactionFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareFrame",
                    "type": FareFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DriverScheduleFrame",
                    "type": DriverScheduleFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleScheduleFrame",
                    "type": VehicleScheduleFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceFrame",
                    "type": ServiceFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimetableFrame",
                    "type": TimetableFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SiteFrame",
                    "type": SiteFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "InfrastructureFrame",
                    "type": InfrastructureFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeneralFrame",
                    "type": GeneralFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ResourceFrame",
                    "type": ResourceFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceCalendarFrame",
                    "type": ServiceCalendarFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
