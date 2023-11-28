from dataclasses import dataclass, field
from typing import Optional
from netex.data_managed_object_view_structure import DataManagedObjectViewStructure
from netex.flexible_mode_of_operation_ref import FlexibleModeOfOperationRef
from netex.personal_mode_of_operation_ref import PersonalModeOfOperationRef
from netex.scheduled_mode_of_operation_ref import ScheduledModeOfOperationRef
from netex.transport_modes_rel_structure import TransportModesRelStructure
from netex.vehicle_pooling_ref import VehiclePoolingRef
from netex.vehicle_rental_ref import VehicleRentalRef
from netex.vehicle_sharing_ref import VehicleSharingRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ModeRestrictionAssessmentVersionStructure(DataManagedObjectViewStructure):
    """
    Type for MODE RESTRICTION ASSESSMENT.

    :ivar exclude: Whether modes is to be excluded. Default is true.
    :ivar transport_modes: Transport MODES to which restriction applies
    :ivar choice:
    :ivar minimum_number_of_passengers: Minimum number of passengers to
        be able to use.
    """
    class Meta:
        name = "ModeRestrictionAssessment_VersionStructure"

    exclude: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Exclude",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    transport_modes: Optional[TransportModesRelStructure] = field(
        default=None,
        metadata={
            "name": "transportModes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    choice: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "PersonalModeOfOperationRef",
                    "type": PersonalModeOfOperationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehiclePoolingRef",
                    "type": VehiclePoolingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleSharingRef",
                    "type": VehicleSharingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleRentalRef",
                    "type": VehicleRentalRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FlexibleModeOfOperationRef",
                    "type": FlexibleModeOfOperationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ScheduledModeOfOperationRef",
                    "type": ScheduledModeOfOperationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    minimum_number_of_passengers: Optional[int] = field(
        default=None,
        metadata={
            "name": "MinimumNumberOfPassengers",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
