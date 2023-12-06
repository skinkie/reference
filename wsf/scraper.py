

"https://tickets.westerscheldeferry.nl/api/v1/1ca871fc-2bb9-4326-acb6-7244d0b5b90d/03035ad3-94d3-4665-9d59-3d814687cabc/calendardates/2023-12-06/2024-02-29/nl-NL?journey=afvaart-vlissingen-breskens-dag"

"https://tickets.westerscheldeferry.nl/api/v1/1ca871fc-2bb9-4326-acb6-7244d0b5b90d/03035ad3-94d3-4665-9d59-3d814687cabc/calendardates/2024-04-30/2024-06-30/nl-NL?journey=afvaart-breskens-vlissingen-dag"


"https://tickets.westerscheldeferry.nl/api/v1/1ca871fc-2bb9-4326-acb6-7244d0b5b90d/03035ad3-94d3-4665-9d59-3d814687cabc/calendardates/2024-04-30/2024-06-30/nl-NL?journey=afvaart-breskens-vlissingen-dag"

import requests
import datetime
import json

headers = {
    'User-Agent': 'openOV/1.0',
    'From': 'ndovloket+wsf@opengeo.nl'  # This is another valid field
}

session = requests.Session()
from_date = datetime.date.today()
to_date = from_date + datetime.timedelta(days=60)
response = session.get(f"https://tickets.westerscheldeferry.nl/api/v1/1ca871fc-2bb9-4326-acb6-7244d0b5b90d/03035ad3-94d3-4665-9d59-3d814687cabc/calendardates/{from_date}/{to_date}/nl-NL?journey=afvaart-vlissingen-breskens-tijdslot", headers=headers)
date_range = response.json()

departures = {'V_B': [], 'B_V': []}

for operational_date in date_range:
    response = session.get(f"https://tickets.westerscheldeferry.nl/api/v1/1ca871fc-2bb9-4326-acb6-7244d0b5b90d/03035ad3-94d3-4665-9d59-3d814687cabc/pricetypes/{operational_date}/nl-NL")
    price_keys = response.json()

    directions = [x for x in price_keys if x['category']['id'] == 1 and x['externalPriceTypeId'] == 'V' and ' jr ' not in x['priceTypeTicketName']] + [x for x in price_keys if x['category']['id'] == 2 and x['externalPriceTypeId'] == 'V' and ' jr ' not in x['priceTypeTicketName']]

    for direction in directions:
        tmp = direction['priceTypeTicketName']
        if 'V-B' in tmp:
            direction_name = 'V_B'
        else:
            direction_name = 'B_V'

        for sj in direction['priceKeyCapacity']:
            departures[direction_name].append(sj['startTime'])



duration = 23

with open('scrape-output/wsf-{}.csv'.format(from_date.isoformat().replace('-', '')), 'w') as out:
    out.write("date,from,time,to,duration\n")

    for direction_name, departure_datetimes in departures.items():
        for departure_datetime in departure_datetimes:
            date, time = departure_datetime.split('T')
            f, t = direction_name.split('_')
            out.write(','.join([date, f, time, t, str(duration)]) + '\n')
            out.flush()


# https://tickets.westerscheldeferry.nl/api/v1/1ca871fc-2bb9-4326-acb6-7244d0b5b90d/03035ad3-94d3-4665-9d59-3d814687cabc/calendardates/2023-12-06/2024-02-29/nl-NL?journey=afvaart-vlissingen-breskens-tijdslot
# https://tickets.westerscheldeferry.nl/api/v1/1ca871fc-2bb9-4326-acb6-7244d0b5b90d/03035ad3-94d3-4665-9d59-3d814687cabc/pricetypes/2023-12-07/nl-NL
# https://tickets.westerscheldeferry.nl/api/v1/1ca871fc-2bb9-4326-acb6-7244d0b5b90d/03035ad3-94d3-4665-9d59-3d814687cabc/pricetypes/2023-12-07/nl-NL