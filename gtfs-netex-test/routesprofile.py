from typing import List, Dict

import refs
import utils
from netex import Codespace, ServiceLink, RouteLink, RoutePoint, RoutePointRefStructure, TimingLink, PointRefStructure, \
    TimingPoint, ScheduledStopPoint, TimingPointVersionStructure


class RoutesProfile:
    @staticmethod
    def projectServiceLinkToRouteLink(service_link: ServiceLink, route_point_refs: Dict[str, RoutePointRefStructure]) -> RouteLink:
        route_link: RouteLink = utils.project(service_link, RouteLink)

        # Because the input has 'non-compatible from and to' we have to project these as well
        # here we do assume that all points have been taken care of for us.
        route_link.from_point_ref = route_point_refs.get(route_link.from_point_ref.ref)
        route_link.to_point_ref = route_point_refs.get(route_link.to_point_ref.ref)

        return route_link

    @staticmethod
    def projectTimingLinkToRouteLink(timing_link: TimingLink, route_point_refs: Dict[str, RoutePointRefStructure]) -> RouteLink:
        route_link: RouteLink = utils.project(timing_link, RouteLink)

        # Because the input has 'non-compatible from and to' we have to project these as well
        # here we do assume that all points have been taken care of for us.
        route_link.from_point_ref = route_point_refs.get(route_link.from_point_ref.ref)
        route_link.to_point_ref = route_point_refs.get(route_link.to_point_ref.ref)

        return route_link


    # TODO: The input for this function is using a TimingPointVersionStructure, because a TimingLink may refer to a
    # ScheduledStopPoint or a TimingPoint. We are using str matching now on id (and ref), in our ideal case we
    # would use references that take in account the class of the object as well. For this we would need to have a
    # "magic" RefStructure that is consistently hashable.
    #
    # TODO: Ideally we would like to use the ContainerStructures as dicts.

    @staticmethod
    def projectLinksToRouteLinks(service_links: List[ServiceLink], timing_links: List[TimingLink], timing_points: List[TimingPointVersionStructure], route_points: List[RoutePoint], route_links: List[RouteLink]):
        route_links_index: Dict[str, RouteLink] = {}
        route_point_refs: Dict[str, RoutePointRefStructure] = {}

        route_points_index = refs.getIndex(route_points)
        timing_points_index = refs.getIndex(timing_points)

        for route_point in route_points_index:
            route_point_refs[route_point.id] = refs.getRef(route_point)

        for service_link in service_links:
            route_point: RoutePoint = utils.project(timing_points_index[service_link.from_point_ref.ref], RoutePoint)
            if route_point.id not in route_points_index:
                route_points_index[route_point.id] = route_point
                route_point_refs[route_point.id] = refs.getRef(route_point)

        for timing_link in timing_links:
            route_point: RoutePoint = utils.project(timing_points_index[timing_link.from_point_ref.ref], RoutePoint)
            if route_point.id not in route_points_index:
                route_points_index[route_point.id] = route_point
                route_point_refs[route_point.id] = refs.getRef(route_point)


        for service_link in service_links:
            route_link = RoutesProfile.projectServiceLinkToRouteLink(service_link, route_point_refs)
            if route_link.id in route_links_index:
                print(f"{route_link.id} is already part of the set.")

            route_links_index[route_link.id] = route_link

        for timing_link in timing_links:
            route_link = RoutesProfile.projectTimingLinkToRouteLink(timing_link, route_point_refs)
            if route_link.id in route_links_index:
                print(f"{route_link.id} is already part of the set.")

            route_links_index[route_link.id] = route_link

        route_links.clear()
        route_links += route_links_index.values()

