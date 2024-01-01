from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class MachineReadableEnumeration(Enum):
    NONE = "none"
    MAGNETIC_STRIP = "magneticStrip"
    CHIP = "chip"
    OCR = "ocr"
    APNR = "apnr"
    BAR_CODE = "barCode"
    SHOT_CODE = "shotCode"
    NFC = "nfc"
    OTHER = "other"
