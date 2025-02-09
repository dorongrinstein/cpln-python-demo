async def app(scope, receive, send):
    assert scope['type'] == 'http'

    print("This is a sample log message written to stdout.")
    await send({
        'type': 'http.response.start',
        'status': 200,
        'headers': [
            [b'content-type', b'text/plain'],
        ],
    })
    await send({
        'type': 'http.response.body',
        'body': b'Hello from Jame in Minnesota!',
    })
