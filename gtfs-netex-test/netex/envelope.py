from dataclasses import dataclass

from .envelope_type import EnvelopeType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass(kw_only=True)
class Envelope(EnvelopeType):
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
