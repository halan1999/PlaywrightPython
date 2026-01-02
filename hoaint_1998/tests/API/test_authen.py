import pytest
from faker import Faker
from playwright.sync_api import APIResponse, APIRequestContext
import json

def assert_response_ok(res: APIResponse):
    assert res.ok, f"Request failed: {res.status} - {res.text()}"

def register(api_context_antester, email: str = None, name: str = None, password: str = None, address: str = None, phone: str = None):
    payload = {"email": email, 
               "name": name, 
               "password": password,
                # "avatarUrl":avatarUrl,
                "phone": phone,
                "address": address}
    res = api_context_antester.post("/api/register", data=payload)
    assert_response_ok(res)

def login(api_context_antester, email: str = None, password: str = None):
    payload = {"email": email, 
               "password": password}
    res = api_context_antester.post("/api/login", data=payload)
    assert_response_ok(res)
    data = res.json()
    return data["accessToken"]

def get_me(api_context_antester, token: str, email: str, name: str, address: str, phone: str):
    res = api_context_antester.get("/api/me", headers={"Authorization": f"Bearer {token}",})
    assert_response_ok(res)
    data = res.json()
    assert data["email"] == email
    assert data["name"] == name
    assert data["address"] == address
    assert data["phone"] == phone


def refetch_token(api_context_antester):
    res = api_context_antester.post("/api/refetch-token")
    assert_response_ok(res)    
    data = res.json()
    return data["accessToken"]

def logout(api_context_antester, token: str):
    res = api_context_antester.delete("/api/logout", headers={"Authorization": f"Bearer {token}",})
    assert_response_ok(res)    

def profile(api_context_antester: APIRequestContext, token: str, email: str = None, name: str = None, password: str = None, password_old: str = None, address: str = None, phone: str = None):
    payload = {
        "email": email,
        "name": name,
        "password": password,
        "password_old": password_old,
        "address": address,
        "phone": phone
    }
    payload = {k:v for k, v in payload.items() if v is not None}
    res = api_context_antester.patch("/api/profile", 
                                     headers={"Authorization": f"Bearer {token}",
                                            "Content-Type": "application/json",
                                            "Accept": "application/json",}, 
                                     data={"fields": payload})
    assert_response_ok(res)    


def test_register(api_context_antester):
    faker = Faker()
    email = faker.email()
    name = faker.name_female()
    password = "HoaiNT1998"
    phone = faker.phone_number()
    address = faker.address()
    register(api_context_antester, email=email, password=password, name=name, phone=phone, address=address)
    token = login(api_context_antester, email=email, password=password)
    get_me(api_context_antester, token, email=email, name=name, phone=phone, address=address)
    profile(api_context_antester, token, password="check", password_old="check")
    token = refetch_token(api_context_antester)
    logout(api_context_antester, token)

