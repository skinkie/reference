from dataclasses import dataclass
from .other_error_structure import OtherErrorStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class OtherError(OtherErrorStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
