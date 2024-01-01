from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class CompressionMethodEnumeration(Enum):
    GZIP = "gzip"
    NONE = "none"
    OTHER = "other"
