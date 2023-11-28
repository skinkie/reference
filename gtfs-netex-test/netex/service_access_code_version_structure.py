from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime
from netex.travel_document_version_structure import TravelDocumentVersionStructure
from netex.vehicle_access_credentials_assignment_ref import VehicleAccessCredentialsAssignmentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ServiceAccessCodeVersionStructure(TravelDocumentVersionStructure):
    """
    Type for SERVICE ACCESS CODE restricts id.

    :ivar access_code: ACCESS Code value
    :ivar expiry_date: Expiry timpestamp for code.
    :ivar vehicle_access_credentials_assignment_ref:
    """
    class Meta:
        name = "ServiceAccessCode_VersionStructure"

    access_code: str = field(
        metadata={
            "name": "AccessCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    expiry_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ExpiryDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_access_credentials_assignment_ref: Optional[VehicleAccessCredentialsAssignmentRef] = field(
        default=None,
        metadata={
            "name": "VehicleAccessCredentialsAssignmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
