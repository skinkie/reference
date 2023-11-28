from dataclasses import dataclass
from netex.personal_mode_of_operation_ref_structure import PersonalModeOfOperationRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PersonalModeOfOperationRef(PersonalModeOfOperationRefStructure):
    """Reference to a PERSONAL MODE OF OPERATION.

    +V1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
