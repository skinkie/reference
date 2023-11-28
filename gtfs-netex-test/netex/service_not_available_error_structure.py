from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime
from netex.error_code_structure import ErrorCodeStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(unsafe_hash=True, kw_only=True)
class ServiceNotAvailableErrorStructure(ErrorCodeStructure):
    """
    Type for Service Not Available error.

    :ivar expected_restart_time: Expected time for reavailability of
        service.  +SIRI v2.0
    """
    expected_restart_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ExpectedRestartTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
