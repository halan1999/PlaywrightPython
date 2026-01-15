def mask_token_keep_last_5(token: str) -> str:
    if not token:
        return ""
    last_5 = token[-5:] if len(token) >= 5 else token
    return f"***{last_5}"