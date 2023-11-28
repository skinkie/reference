from dataclasses import dataclass, field
from typing import Optional
from netex.access_not_allowed_error import AccessNotAllowedError
from netex.allowed_resource_usage_exceeded_error import AllowedResourceUsageExceededError
from netex.beyond_data_horizon import BeyondDataHorizon
from netex.capability_not_supported_error import CapabilityNotSupportedError
from netex.invalid_data_references_error import InvalidDataReferencesError
from netex.natural_language_string_structure import NaturalLanguageStringStructure
from netex.no_info_for_topic_error import NoInfoForTopicError
from netex.other_error import OtherError
from netex.parameters_ignored_error import ParametersIgnoredError
from netex.service_not_available_error import ServiceNotAvailableError
from netex.unknown_extensions_error import UnknownExtensionsError

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(unsafe_hash=True, kw_only=True)
class ErrorConditionStructure:
    """
    Type for RequestErrorCondition.

    :ivar choice:
    :ivar description: Text description of error.
    """
    choice: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ServiceNotAvailableError",
                    "type": ServiceNotAvailableError,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "CapabilityNotSupportedError",
                    "type": CapabilityNotSupportedError,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "AccessNotAllowedError",
                    "type": AccessNotAllowedError,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "InvalidDataReferencesError",
                    "type": InvalidDataReferencesError,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "BeyondDataHorizon",
                    "type": BeyondDataHorizon,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "NoInfoForTopicError",
                    "type": NoInfoForTopicError,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "ParametersIgnoredError",
                    "type": ParametersIgnoredError,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "UnknownExtensionsError",
                    "type": UnknownExtensionsError,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "AllowedResourceUsageExceededError",
                    "type": AllowedResourceUsageExceededError,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "OtherError",
                    "type": OtherError,
                    "namespace": "http://www.siri.org.uk/siri",
                },
            ),
        }
    )
    description: Optional[NaturalLanguageStringStructure] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
