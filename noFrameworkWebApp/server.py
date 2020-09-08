# gunicorn

def app(environ, start_response):
    data = "Hello World"
    data = data.encode("utf-8")

    start_response(
        '200 OK', 
        [
            ("Content-Type", 'text/plain'),
            ("Content-Lenght", str(len(data)))
        ]
    )

    return iter([data])