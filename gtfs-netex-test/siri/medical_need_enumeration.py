from enum import Enum

__NAMESPACE__ = "http://www.ifopt.org.uk/acsb"


class MedicalNeedEnumeration(Enum):
    ALLERGIC = "allergic"
    HEART_CONDITION = "heartCondition"
    OTHER_MEDICAL_NEED = "otherMedicalNeed"
