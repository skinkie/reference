from dataclasses import dataclass, field

from .report_type_enumeration import ReportTypeEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ReportType:
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: ReportTypeEnumeration = field(
        default=ReportTypeEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
