from dataclasses import dataclass
from .envelope_type import EnvelopeType


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass(kw_only=True)
class Envelope(EnvelopeType):
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
