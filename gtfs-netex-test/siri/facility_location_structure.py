from dataclasses import dataclass, field
from typing import List, Optional, Union

from .compound_train_ref import CompoundTrainRef
from .connection_link_ref import ConnectionLinkRef
from .dated_vehicle_journey_ref import DatedVehicleJourneyRef
from .entrance_to_vehicle_ref import EntranceToVehicleRef
from .interchange_ref import InterchangeRef
from .line_ref import LineRef
from .operator_ref_structure import OperatorRefStructure
from .product_category_ref_structure import ProductCategoryRefStructure
from .service_feature_ref import ServiceFeatureRef
from .stop_place_component_ref_structure import StopPlaceComponentRefStructure
from .stop_place_ref_structure import StopPlaceRefStructure
from .stop_point_ref import StopPointRef
from .train_component_ref import TrainComponentRef
from .train_element_ref import TrainElementRef
from .train_in_compound_train_ref import TrainInCompoundTrainRef
from .train_ref import TrainRef
from .vehicle_feature_ref_structure import VehicleFeatureRefStructure
from .vehicle_ref import VehicleRef

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class FacilityLocationStructure:
    line_ref: Optional[LineRef] = field(
        default=None,
        metadata={
            "name": "LineRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_point_ref: Optional[StopPointRef] = field(
        default=None,
        metadata={
            "name": "StopPointRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    vehicle_ref: Optional[VehicleRef] = field(
        default=None,
        metadata={
            "name": "VehicleRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    compound_train_ref: Optional[CompoundTrainRef] = field(
        default=None,
        metadata={
            "name": "CompoundTrainRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    train_ref_or_train_in_compound_train_ref: Optional[Union[TrainRef, TrainInCompoundTrainRef]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TrainRef",
                    "type": TrainRef,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "TrainInCompoundTrainRef",
                    "type": TrainInCompoundTrainRef,
                    "namespace": "http://www.siri.org.uk/siri",
                },
            ),
        },
    )
    train_element_ref_or_train_component_ref: Optional[Union[TrainElementRef, TrainComponentRef]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TrainElementRef",
                    "type": TrainElementRef,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "TrainComponentRef",
                    "type": TrainComponentRef,
                    "namespace": "http://www.siri.org.uk/siri",
                },
            ),
        },
    )
    entrance_to_vehicle_ref: Optional[EntranceToVehicleRef] = field(
        default=None,
        metadata={
            "name": "EntranceToVehicleRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    dated_vehicle_journey_ref: Optional[DatedVehicleJourneyRef] = field(
        default=None,
        metadata={
            "name": "DatedVehicleJourneyRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    connection_link_ref: Optional[ConnectionLinkRef] = field(
        default=None,
        metadata={
            "name": "ConnectionLinkRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    interchange_ref: Optional[InterchangeRef] = field(
        default=None,
        metadata={
            "name": "InterchangeRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_place_ref: Optional[StopPlaceRefStructure] = field(
        default=None,
        metadata={
            "name": "StopPlaceRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_place_component_id: Optional[StopPlaceComponentRefStructure] = field(
        default=None,
        metadata={
            "name": "StopPlaceComponentId",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    operator_ref: Optional[OperatorRefStructure] = field(
        default=None,
        metadata={
            "name": "OperatorRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    product_category_ref: Optional[ProductCategoryRefStructure] = field(
        default=None,
        metadata={
            "name": "ProductCategoryRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    service_feature_ref: List[ServiceFeatureRef] = field(
        default_factory=list,
        metadata={
            "name": "ServiceFeatureRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    vehicle_feature_ref: List[VehicleFeatureRefStructure] = field(
        default_factory=list,
        metadata={
            "name": "VehicleFeatureRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
