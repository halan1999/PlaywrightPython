from playwright.sync_api import APIRequestContext
import json

class APIClient:
    def __init__(self, request: APIRequestContext):
        self.request = request
    
    def get_with_auth(self, endpoint, token, params=None):
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        response = self.request.get(endpoint, headers=headers, params=params)
        return response

    def get(self, endpoint, **kwargs):
        return self.request.get(endpoint, **kwargs)

    def post(self, endpoint, data=None, headers=None, **kwargs):
        current_headers = headers or {}
        if data is not None and 'json' not in kwargs:
            kwargs['json'] = data

        return self.request.post(
            endpoint, 
            headers=current_headers, 
            **kwargs
    )
    
    def put(self, endpoint, data=None, **kwargs):
        return self.request.put(endpoint, data=data, **kwargs)

    def delete(self, endpoint, **kwargs):
        return self.request.delete(endpoint, **kwargs)

    def patch(self, endpoint, data=None, **kwargs):
        return self.request.patch(endpoint, data=data, **kwargs)