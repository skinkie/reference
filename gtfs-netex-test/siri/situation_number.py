from dataclasses import dataclass

from .entry_qualifier_structure import EntryQualifierStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class SituationNumber(EntryQualifierStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
