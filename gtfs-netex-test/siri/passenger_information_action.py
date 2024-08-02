from dataclasses import dataclass

from .passenger_information_action_structure import PassengerInformationActionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class PassengerInformationAction(PassengerInformationActionStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
