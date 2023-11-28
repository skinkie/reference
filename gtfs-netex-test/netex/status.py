from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(unsafe_hash=True, kw_only=True)
class Status:
    """Whether the request was processed successfully or not.

    Default is 'true'.
    """
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: bool = field(
        default=True,
        metadata={
            "required": True,
        }
    )
