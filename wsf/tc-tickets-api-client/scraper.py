from tc_tickets_api_client.api.events import get_api_v_2_events_performances
from tc_tickets_api_client.types import Response
from tc_tickets_api_client.models.event_performance_response import EventPerformanceResponse


from tc_tickets_api_client.client import AuthenticatedClient

client = AuthenticatedClient(base_url="https://apiv2acpt.ticketcounter.eu/", token="SuperSecretToken")
with client as client:
    my_data: EventPerformanceResponse = get_api_v_2_events_performances.sync(client=client)

    print(my_data)