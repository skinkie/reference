from dataclasses import dataclass
from .alternative_texts_rel_structure import ValidBetweenVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SimpleValidityCondition(ValidBetweenVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    validity_conditions: RestrictedVar
    valid_between: RestrictedVar
    alternative_texts: RestrictedVar
    key_list: RestrictedVar
    extensions: RestrictedVar
    branding_ref: RestrictedVar
    name: RestrictedVar
    description: RestrictedVar
    conditioned_object_ref: RestrictedVar
    with_condition_ref: RestrictedVar
