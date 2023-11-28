from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class RetailFacilityEnumeration(Enum):
    """
    Allowed values for Retail Facility.
    """
    UNKNOWN = "unknown"
    FOOD = "food"
    NEWSPAPER_TOBACCO = "newspaperTobacco"
    RECREATION_TRAVEL = "recreationTravel"
    HYGIENE_HEALTH_BEAUTY = "hygieneHealthBeauty"
    FASHION_ACCESSORIES = "fashionAccessories"
    BANK_FINANCE_INSURANCE = "bankFinanceInsurance"
    CASH_MACHINE = "cashMachine"
    CURRENCY_EXCHANGE = "currencyExchange"
    TOURISM_SERVICE = "tourismService"
    PHOTO_BOOTH = "photoBooth"
