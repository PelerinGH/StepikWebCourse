def app(env, start_response):
    data=env["QUERY_STRING"].split("&")
    data="\n".join(data)
    data=bytes(data, encoding="utf-8")
    start_response("200 OK", [('Content-Type', 'text/plain')])
    return [data]