from dataclasses import dataclass

from .general_message_subscription_structure import GeneralMessageSubscriptionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class GeneralMessageSubscriptionRequest(GeneralMessageSubscriptionStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
