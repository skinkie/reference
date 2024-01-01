from dataclasses import dataclass
from .customer_account_status_version_structure import (
    CustomerAccountStatusVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CustomerAccountStatus(CustomerAccountStatusVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
