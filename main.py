from fastapi import FastAPI, Request, Response

app = FastAPI()


def get_counter(request: Request):
    counter = request.cookies.get("counter")
    return int(counter) if counter else 0

@app.get("/cookie")
async def read_cookie(request: Request):
    counter = get_counter(request)
    content = f"""
    <html>
    <body>
    <p>Counter: {counter}</p>
    <form action="/cookie" method="post">
    <input type="submit" value="Cookies!" />
    </form>
    </body>
    </html>
    """
    return Response(content=content, media_type="text/html")

@app.post("/cookie")
async def create_cookie(request: Request):
    counter = get_counter(request)
    new_counter = counter + 1
    response = Response(content=f"""
    <html>
    <body>
    <p>Counter: {new_counter}</p>
    <form action="/cookie" method="post">
    <input type="submit" value="Cookies!" />
    </form>
    </body>
    </html>
    """, media_type="text/html")
    response.set_cookie(key="counter", value=str(new_counter))
    return response
