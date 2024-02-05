from netex import Line, MultilingualString, AllVehicleModesOfTransportEnumeration, InfoLinksRelStructure, \
    ScheduledStopPoint


class GtfsProfile:
    @staticmethod
    def getOptionalMultilingualString(multilingual_string: MultilingualString):
        if multilingual_string is not None:
            return multilingual_string.value

        return ''

    @staticmethod
    def projectVehicleModeToRouteType(vehicle_mode: AllVehicleModesOfTransportEnumeration):
        if vehicle_mode == AllVehicleModesOfTransportEnumeration.TRAM:
            return 0
        elif vehicle_mode == AllVehicleModesOfTransportEnumeration.METRO:
            return 1
        elif vehicle_mode == AllVehicleModesOfTransportEnumeration.RAIL:
            return 2
        elif vehicle_mode == AllVehicleModesOfTransportEnumeration.BUS:
            return 3
        elif vehicle_mode in (AllVehicleModesOfTransportEnumeration.WATER, AllVehicleModesOfTransportEnumeration.FERRY):
            return 4

        # We don't have a Cable Tram in NeTEx route_type = 5?

        elif vehicle_mode == AllVehicleModesOfTransportEnumeration.CABLEWAY:
            return 6
        elif vehicle_mode == AllVehicleModesOfTransportEnumeration.FUNICULAR:
            return 7
        elif vehicle_mode == AllVehicleModesOfTransportEnumeration.TROLLEY_BUS:
            return 11

        # We don't have a Monorail in NeTEx route_type = 11?

        return 0

    @staticmethod
    def getInfoLinkWithUrl(info_links: InfoLinksRelStructure):
        if info_links is not None:
            # TODO: we would like to sort this based on some kind of priority, based on type_of_info_link
            for info_link in info_links.info_link:
                return info_link.value
        return ''

    @staticmethod
    def projectLineToRoute(line: Line):

        if line.branding_ref is not None:
            agency_id = line.branding_ref.ref
        else:
            agency_id = line.authority_ref_or_operator_ref.ref

        route = {'route_id': line.id,
                 'agency_id': agency_id,
                 'route_short_name': line.public_code, # This is used as VehicleType or PublicCode
                 'route_long_name': line.name, # This is used as destination
                 'route_desc': GtfsProfile.getOptionalMultilingualString(line.description),
                 'route_type': GtfsProfile.projectVehicleModeToRouteType(line.transport_mode),
                 'route_url': GtfsProfile.getInfoLinkWithUrl(line.document_links),
                 'route_color': line.presentation.colour,
                 'route_text_color': line.presentation.text_colour,
                 'route_sort_order': '',
                 'continuous_pickup': '',
                 'continuous_drop_off': '',
                 'network_id': ''}

        return route

    @staticmethod
    def getTariffZoneFromScheduledStopPoint(scheduled_stop_point: ScheduledStopPoint):
        if scheduled_stop_point.tariff_zones and len(scheduled_stop_point.tariff_zones.tariff_zone_ref) > 0:
            return scheduled_stop_point.tariff_zones.tariff_zone_ref[0].ref

        return ''

    @staticmethod
    def getStopAreaFromScheduledStopPoint(scheduled_stop_point: ScheduledStopPoint):
        if scheduled_stop_point.stop_areas and len(scheduled_stop_point.stop_areas.stop_area_ref) > 0:
            return scheduled_stop_point.stop_areas.stop_area_ref[0].ref

        return ''

    @staticmethod
    def projectScheduledStopPointToStop(scheduled_stop_point: ScheduledStopPoint):
        # TODO: parent_station could be obtained from StopPlace or StopArea

        stop = {'stop_id': scheduled_stop_point.id,
                'stop_code': GtfsProfile.getOptionalMultilingualString(scheduled_stop_point.public_code),
                'stop_name': GtfsProfile.getOptionalMultilingualString(scheduled_stop_point.short_name),
                'stop_desc': GtfsProfile.getOptionalMultilingualString(scheduled_stop_point.description),
                'stop_lat': scheduled_stop_point.location.longitude,
                'stop_lon': scheduled_stop_point.location.latitude,
                'zone_id': GtfsProfile.getTariffZoneFromScheduledStopPoint(scheduled_stop_point),
                'stop_url': '',
                'location_type': 0,
                'parent_station': GtfsProfile.getStopAreaFromScheduledStopPoint(scheduled_stop_point)
                'stop_timezone': ''
                'wheelchair_boarding':
                'level_id':
                'platform_code':
        }

        return stop