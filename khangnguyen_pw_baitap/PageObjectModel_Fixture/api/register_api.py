def register_user(api_context, payload: dict):
    # Try 1: send flat payload
    res = api_context.post("/api/register", data=payload)
    if res.ok:
        return res.json()

    # Try 2: fallback with "fields"
    res2 = api_context.post("/api/register", data={"fields": payload})
    if res2.ok:
        return res2.json()

    raise AssertionError(
        "Register failed.\n"
        f"Try1: {res.status} - {res.text()}\n"
        f"Try2: {res2.status} - {res2.text()}"
    )