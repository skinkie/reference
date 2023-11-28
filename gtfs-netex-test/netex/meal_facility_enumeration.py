from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class MealFacilityEnumeration(Enum):
    """
    Allowed values for Meal Facility.
    """
    BREAKFAST = "breakfast"
    LUNCH = "lunch"
    DINNER = "dinner"
    SNACK = "snack"
    DRINKS = "drinks"
