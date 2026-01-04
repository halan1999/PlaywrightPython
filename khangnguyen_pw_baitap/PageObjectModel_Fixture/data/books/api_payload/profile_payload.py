def build_profile_payload(register_payload: dict, address: str) -> dict:
    return {
        "name": register_payload["name"],
        "email": register_payload["email"],
        "address": address
    }