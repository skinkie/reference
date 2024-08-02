from dataclasses import dataclass

from .publish_to_tv_action_structure import PublishToTvActionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class PublishToTvAction(PublishToTvActionStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
