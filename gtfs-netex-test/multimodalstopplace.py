from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from netex import StopPlace, SiteTypeEnumeration, SiteRefsRelStructure, StopPlaceRef, Site, \
    AllVehicleModesOfTransportEnumeration, Parking, ParkingTypeEnumeration, ParkingVehicleEnumeration, SiteFrame, \
    StopPlacesInFrameRelStructure, ParkingsInFrameRelStructure, SiteRefStructure, SitePathLinksInFrameRelStructure, \
    SitePathLink, SitePathLinkEndStructure, PathDirectionEnumeration, QuaysRelStructure, Quay, MultilingualString, \
    QuayTypeEnumeration, VehicleModeEnumeration, QuayRefStructure, AccessFeatureEnumeration, Line
from refs import getRef

parking = Parking(id="Parkeren", version="20240603",
                  parking_type=ParkingTypeEnumeration.TRAIN_STATION_PARKING,
                  parking_vehicle_types=[ParkingVehicleEnumeration.CAR],
                  )

scheveningen = Quay(id="Scheveningen", quay_type=QuayTypeEnumeration.MULTIMODAL, transport_mode=AllVehicleModesOfTransportEnumeration.TRAM, other_transport_modes=[VehicleModeEnumeration.BUS], version="20240603")
voorburg = Quay(id="Voorburg", quay_type=QuayTypeEnumeration.MULTIMODAL, transport_mode=AllVehicleModesOfTransportEnumeration.TRAM, other_transport_modes=[VehicleModeEnumeration.BUS],  version="20240603")

bustram_tangent = StopPlace(id="NOI-Tram-Tangent", version="20240603",
                   transport_mode=AllVehicleModesOfTransportEnumeration.ANY_MODE,
                            quays=QuaysRelStructure(taxi_stand_ref_or_quay_ref_or_quay=[scheveningen, voorburg])
                   )

tram_naast = StopPlace(id="NOI-Tram-naast", version="20240603",
                   transport_mode=AllVehicleModesOfTransportEnumeration.TRAM,
                   )

parent = StopPlace(id="NOI", version="20240603",
                   transport_mode=AllVehicleModesOfTransportEnumeration.ALL,
                   adjacent_sites=SiteRefsRelStructure(site_ref_or_stop_place_ref=
                                                       [getRef(parking),
                                                        getRef(bustram_tangent), getRef(tram_naast)
                                                        ])
                   )


parking.adjacent_sites = SiteRefsRelStructure(site_ref_or_stop_place_ref = [getRef(parent), getRef(bustram_tangent)])
bustram_tangent.adjacent_sites = SiteRefsRelStructure(site_ref_or_stop_place_ref = [getRef(parent), getRef(parking)])
tram_naast.adjacent_sites = SiteRefsRelStructure(site_ref_or_stop_place_ref = [getRef(parent)])

perron_1 = Quay(id="Perron 1", version="20240603", short_name=MultilingualString(value="1"), quay_type=QuayTypeEnumeration.MULTIMODAL)
perron_2_3 = Quay(id="Perron 2 en 3", version="20240603", short_name=MultilingualString(value="2 en 3"), quay_type=QuayTypeEnumeration.MULTIMODAL)

perron_1a = Quay(id="Perron 1a", version="20240603", short_name=MultilingualString(value="1a"), parent_quay_ref=getRef(perron_1, QuayRefStructure))
perron_2a = Quay(id="Perron 2a", version="20240603", short_name=MultilingualString(value="2a"), parent_quay_ref=getRef(perron_2_3, QuayRefStructure))


tram = StopPlace(id="NOI-Tram", version="20240603",
                   transport_mode=AllVehicleModesOfTransportEnumeration.TRAM,
                   parent_site_ref=getRef(parent, SiteRefStructure),
                   quays=QuaysRelStructure(taxi_stand_ref_or_quay_ref_or_quay=[perron_1a, perron_2a])
                   )

perron_1b = Quay(id="Perron 1b", version="20240603", short_name=MultilingualString(value="1b"), parent_quay_ref=getRef(perron_1, QuayRefStructure))
perron_2b = Quay(id="Perron 2b", version="20240603", short_name=MultilingualString(value="2b"), parent_quay_ref=getRef(perron_2_3, QuayRefStructure))

metro = StopPlace(id="NOI-Metro", version="20240603",
                   transport_mode=AllVehicleModesOfTransportEnumeration.METRO,
                   parent_site_ref=getRef(parent, SiteRefStructure),
                   quays=QuaysRelStructure(taxi_stand_ref_or_quay_ref_or_quay=[perron_1b, perron_2b])
                   )

perron_4_5 = Quay(id="Perron 4 en 5", version="20240603", short_name=MultilingualString(value="4 en 5"), quay_type=QuayTypeEnumeration.RAIL_ISLAND_PLATFORM)

perron_3 = Quay(id="Perron 3", version="20240603", short_name=MultilingualString(value="3"), quay_type=QuayTypeEnumeration.RAIL_PLATFORM, parent_quay_ref=getRef(perron_2_3, QuayRefStructure))
perron_4 = Quay(id="Perron 4", version="20240603", short_name=MultilingualString(value="4"), quay_type=QuayTypeEnumeration.RAIL_PLATFORM_SECTOR, parent_quay_ref=getRef(perron_4_5, QuayRefStructure))
perron_5 = Quay(id="Perron 5", version="20240603", short_name=MultilingualString(value="5"), quay_type=QuayTypeEnumeration.RAIL_PLATFORM_SECTOR, parent_quay_ref=getRef(perron_4_5, QuayRefStructure))
perron_6 = Quay(id="Perron 6", version="20240603", short_name=MultilingualString(value="6"), quay_type=QuayTypeEnumeration.RAIL_PLATFORM)

trein = StopPlace(id="NOI-Trein", version="20240603",
                  transport_mode=AllVehicleModesOfTransportEnumeration.INTERCITY_RAIL,
                  parent_site_ref=getRef(parent, SiteRefStructure),
                  quays=QuaysRelStructure(taxi_stand_ref_or_quay_ref_or_quay=[perron_3, perron_4_5, perron_4, perron_5, perron_6])
                  )

parent.quays = QuaysRelStructure(taxi_stand_ref_or_quay_ref_or_quay=[perron_1, perron_2_3])

tram.adjacent_sites = SiteRefsRelStructure(site_ref_or_stop_place_ref = [getRef(metro), getRef(trein)])
metro.adjacent_sites = SiteRefsRelStructure(site_ref_or_stop_place_ref = [getRef(tram), getRef(trein)])
trein.adjacent_sites = SiteRefsRelStructure(site_ref_or_stop_place_ref = [getRef(metro), getRef(tram)])


parent_tram_naast = SitePathLink(allowed_use=PathDirectionEnumeration.TWO_WAY, from_value=SitePathLinkEndStructure(choice=getRef(parent)), to=SitePathLinkEndStructure(choice=getRef(tram_naast)))
parent_bustram_tangent = SitePathLink(allowed_use=PathDirectionEnumeration.TWO_WAY, from_value=SitePathLinkEndStructure(choice=getRef(parent)), to=SitePathLinkEndStructure(choice=getRef(bustram_tangent)))
parent_parking = SitePathLink(allowed_use=PathDirectionEnumeration.TWO_WAY, from_value=SitePathLinkEndStructure(choice=getRef(parent)), to=SitePathLinkEndStructure(choice=getRef(parking)))

metro_tram = SitePathLink(allowed_use=PathDirectionEnumeration.TWO_WAY, from_value=SitePathLinkEndStructure(choice=getRef(perron_1b)), to=SitePathLinkEndStructure(choice=getRef(perron_1a)), access_feature_type=AccessFeatureEnumeration.RAMP)
metro_trein = SitePathLink(allowed_use=PathDirectionEnumeration.TWO_WAY, from_value=SitePathLinkEndStructure(choice=getRef(perron_2b)), to=SitePathLinkEndStructure(choice=getRef(perron_3)))
tram_trein = SitePathLink(allowed_use=PathDirectionEnumeration.TWO_WAY, from_value=SitePathLinkEndStructure(choice=getRef(perron_2a)), to=SitePathLinkEndStructure(choice=getRef(perron_3)), access_feature_type=AccessFeatureEnumeration.STAIRS)



site_frame = SiteFrame(id="Site", version="20240603",
                       stop_places=StopPlacesInFrameRelStructure(stop_place=[bustram_tangent, tram_naast, tram, metro, trein]),
                       parkings=ParkingsInFrameRelStructure(parking=[parking]),
                       path_links=SitePathLinksInFrameRelStructure(site_path_link_or_off_site_path_link_or_path_link=[parent_tram_naast, parent_bustram_tangent, parent_parking,
                                                                                                                      metro_tram, metro_trein, tram_trein
                                                                                                                      ]))

serializer_config = SerializerConfig(ignore_default_attributes=True, pretty_print=True)
serializer_config.ignore_default_attributes = True
serializer = XmlSerializer(config=serializer_config)

ns_map={'': 'http://www.netex.org.uk/netex', 'gml': 'http://www.opengis.net/gml/3.2'}

print(serializer.render(site_frame, ns_map))

