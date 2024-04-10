from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class MachineReadableEnumeration(Enum):
    NONE = "none"
    MAGNETIC_STRIP = "magneticStrip"
    CHIP = "chip"
    OCR = "ocr"
    APNR = "apnr"
    BAR_CODE = "barCode"
    QR_CODE = "qrCode"
    SHOT_CODE = "shotCode"
    NFC = "nfc"
    OTHER = "other"
