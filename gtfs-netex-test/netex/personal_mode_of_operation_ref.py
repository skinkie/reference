from dataclasses import dataclass

from .personal_mode_of_operation_ref_structure import PersonalModeOfOperationRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class PersonalModeOfOperationRef(PersonalModeOfOperationRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
