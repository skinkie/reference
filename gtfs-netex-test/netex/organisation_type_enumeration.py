from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class OrganisationTypeEnumeration(Enum):
    """
    Allowed values for ORGANISATION TYPE.

    :cvar AUTHORITY: ORGANISATION is a Transport Authority or Agency.
    :cvar OPERATOR: ORGANISATION is a Public Transport OPERATOR.
    :cvar RAIL_OPERATOR: ORGANISATION is a Rail OPERATOR.
    :cvar RAIL_FREIGHT_OPERATOR: ORGANISATION is a rail freight
        OPERATOR.
    :cvar STATUTORY_BODY: ORGANISATION is a statutory body or government
        department.
    :cvar FACILITY_OPERATOR: ORGANISATION operates a facility such as a
        station.
    :cvar TRAVEL_AGENT: ORGANISATION is a Travel Agent.
    :cvar SERVICED_ORGANISATION: ORGANISATION is a business or
        organisation served by public transport.
    :cvar RETAIL_CONSORTIUM: ORGANISATION is a trade association
        representing independent retailers.
    :cvar ALTERNATIVE_MODE_OPERATOR: ORGANISATION is a transport
        OPERATOR.
    :cvar ONLINE_PROVIDER: ORGANISATION is a third party online service.
    :cvar OTHER: Other type of ORGANISATION.
    """
    AUTHORITY = "authority"
    OPERATOR = "operator"
    RAIL_OPERATOR = "railOperator"
    RAIL_FREIGHT_OPERATOR = "railFreightOperator"
    STATUTORY_BODY = "statutoryBody"
    FACILITY_OPERATOR = "facilityOperator"
    TRAVEL_AGENT = "travelAgent"
    SERVICED_ORGANISATION = "servicedOrganisation"
    RETAIL_CONSORTIUM = "retailConsortium"
    ALTERNATIVE_MODE_OPERATOR = "alternativeModeOperator"
    ONLINE_PROVIDER = "onlineProvider"
    OTHER = "other"
