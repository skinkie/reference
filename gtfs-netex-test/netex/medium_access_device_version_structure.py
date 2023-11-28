from dataclasses import dataclass, field
from typing import Optional
from netex.alternative_texts_rel_structure import DataManagedObjectStructure
from netex.customer_ref import CustomerRef
from netex.medium_application_instance_rel_structure import MediumApplicationInstanceRelStructure
from netex.multilingual_string import MultilingualString
from netex.type_of_medium_access_device_ref import TypeOfMediumAccessDeviceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class MediumAccessDeviceVersionStructure(DataManagedObjectStructure):
    """
    Type for MEDIUM ACCESS DEVICE restricts id.

    :ivar name: Name for device
    :ivar customer_ref:
    :ivar identity_token: Secure token used to identify MEDIUM ACCESS
        DEVICE.
    :ivar type_of_medium_access_device_ref:
    :ivar application_instances: MEDIUM APPLICATION INSTANCES for
        device.
    """
    class Meta:
        name = "MediumAccessDevice_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    customer_ref: Optional[CustomerRef] = field(
        default=None,
        metadata={
            "name": "CustomerRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    identity_token: Optional[str] = field(
        default=None,
        metadata={
            "name": "IdentityToken",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_medium_access_device_ref: Optional[TypeOfMediumAccessDeviceRef] = field(
        default=None,
        metadata={
            "name": "TypeOfMediumAccessDeviceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    application_instances: Optional[MediumApplicationInstanceRelStructure] = field(
        default=None,
        metadata={
            "name": "applicationInstances",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
