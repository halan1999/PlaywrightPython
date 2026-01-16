class BaseAPI:
    def __init__(self, api_context):
        self.api_context = api_context

    def get(self, endpoint):
        return self.api_context.get(endpoint)
    
    def post(self, endpoint, data=None):
        return self.api_context.post(endpoint, data=data)
    
    def patch(self, endpoint, data=None):
        return self.api_context.patch(endpoint, data=data)
    
    def delete(self, endpoint):
        return self.api_context.delete(endpoint)