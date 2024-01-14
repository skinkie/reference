import asyncio

from aiohttp import web

import client
import server
import storage
import generic
from mqtt_communication import mqtt_subscriber

routes = web.RouteTableDef()

@routes.post('/{sender}/anfrage')
async def create_sender(request):
    return await storage.create_sender(request)

@routes.post('/{sender}/aus/datenabrufen.xml')
async def aus_datenabrufen(request):
    return await server.aus_datenabrufen(request)

@routes.post('/{sender}/aus/aboverwalten.xml')
async def aus_aboverwalten(request):
    return await server.aus_aboverwalten(request)

@routes.post('/{sender}/aus/datenbereit.xml')
async def aus_datenbereit(request):
    return await client.aus_datenbereit(request)

@routes.post('/{sender}/aus/status.xml')
async def aus_status(request):
    return await generic.aus_status(request)

app = web.Application()
app.add_routes(routes)

async def main():
    await asyncio.gather(web._run_app(app, port=8081),
                         mqtt_subscriber(),
                         client.abo_anfrage("http://192.168.202.75:8092/test"),
                         storage.queue_garbage_collector(),
                         storage.queue_daten_bereit())

if __name__ == '__main__':
    asyncio.run(storage.check_or_create_tables())
    asyncio.run(main())
