#Python routine to implement a COAP server using aiocoap

import aiocoap.resource as resource
import threading
import datetime
import aiocoap
import asyncio
import socket
import time
import sys
import os

# Blocking connection for CoAP Server
class BlockResource(resource.Resource):

    def set_content(self, content):
        self.content = content

    async def render_put(self, request):
        self.set_content(request.payload)
        print(request.payload)
        return aiocoap.Message(code=aiocoap.CHANGED, payload=self.content)
    
# Handler for CoAp server
def CoAPserver():
    # Resource tree creation
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    root = resource.Site()

    root.add_resource(('.well-known', 'core'),
            resource.WKCResource(root.get_resources_as_linkheader))

    root.add_resource(('other', 'block'), BlockResource())

    asyncio.Task(aiocoap.Context.create_server_context(root))

    loop = asyncio.get_event_loop()
    loop.run_forever()
    
CoAPserver();