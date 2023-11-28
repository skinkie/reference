from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class CateringFacilityEnumeration(Enum):
    """Allowed values for Catering Facility: TPEG pti_table 23.

    :cvar BAR: pti23_18
    :cvar BISTRO: pti23_26
    :cvar BUFFET:
    :cvar NO_FOOD_AVAILABLE: pti23_19
    :cvar NO_BEVERAGES_AVAILABLE: pti23_20
    :cvar RESTAURANT: pti23_1
    :cvar FIRST_CLASS_RESTAURANT:
    :cvar TROLLEY: pti23_23
    :cvar COFFEE_SHOP:
    :cvar HOT_FOOD_SERVICE:
    :cvar SELF_SERVICE:
    :cvar SNACKS: pti23_2
    :cvar FOOD_VENDING_MACHINE:
    :cvar BEVERAGE_VENDING_MACHINE:
    :cvar MINI_BAR: pti23_18_1
    :cvar BREAKFAST_IN_CAR:
    :cvar MEAL_AT_SEAT:
    :cvar OTHER:
    :cvar UNKNOWN:
    """
    BAR = "bar"
    BISTRO = "bistro"
    BUFFET = "buffet"
    NO_FOOD_AVAILABLE = "noFoodAvailable"
    NO_BEVERAGES_AVAILABLE = "noBeveragesAvailable"
    RESTAURANT = "restaurant"
    FIRST_CLASS_RESTAURANT = "firstClassRestaurant"
    TROLLEY = "trolley"
    COFFEE_SHOP = "coffeeShop"
    HOT_FOOD_SERVICE = "hotFoodService"
    SELF_SERVICE = "selfService"
    SNACKS = "snacks"
    FOOD_VENDING_MACHINE = "foodVendingMachine"
    BEVERAGE_VENDING_MACHINE = "beverageVendingMachine"
    MINI_BAR = "miniBar"
    BREAKFAST_IN_CAR = "breakfastInCar"
    MEAL_AT_SEAT = "mealAtSeat"
    OTHER = "other"
    UNKNOWN = "unknown"
