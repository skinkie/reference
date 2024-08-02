from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class VehicleStatusEnumeration(Enum):
    EXPECTED = "expected"
    NOT_EXPECTED = "notExpected"
    CANCELLED = "cancelled"
    ASSIGNED = "assigned"
    SIGNED_ON = "signedOn"
    AT_ORIGIN = "atOrigin"
    IN_PROGRESS = "inProgress"
    ABORTED = "aborted"
    OFF_ROUTE = "offRoute"
    COMPLETED = "completed"
    ASSUMED_COMPLETED = "assumedCompleted"
    NOT_RUN = "notRun"
