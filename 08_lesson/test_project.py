import requests

KEY = "hM48o1oTNFMWhfUxZ+616QNqSRm-obt30bAnkUZtz+ulCxe+xHEG0CIjX1BLxo1y"
headers = {'Authorization': f'Bearer {KEY}','Content-Type': 'application/json'}

def test_create_project():
    body= {
    "title": "First project",
    "users": {
        "a24edb03-ae2b-4d91-9710-10a3dc16eb40": "admin"
    }
    }
    res= requests.post("https://ru.yougile.com/api-v2/projects",headers=headers, json=body)
    assert res.status_code == 201

def test_change_project():
    body= {
    "title": "First project",
    "users": {
        "a24edb03-ae2b-4d91-9710-10a3dc16eb40": "admin"
    }
    }
    res= requests.post("https://ru.yougile.com/api-v2/projects",headers=headers, json=body)
    assert res.status_code == 201
    id = res.json()["id"]
    body = {"title": "First project - my company"}
    res2 = requests.put(f"https://ru.yougile.com/api-v2/projects/{id}",headers=headers, json=body)
    assert res2.status_code == 200

def test_get_project():
    body= {
    "title": "First project",
    "users": {
        "a24edb03-ae2b-4d91-9710-10a3dc16eb40": "admin"
    }
    }
    res= requests.post("https://ru.yougile.com/api-v2/projects",headers=headers, json=body)
    assert res.status_code == 201
    id = res.json()["id"]
    res2 = requests.get(f"https://ru.yougile.com/api-v2/projects/{id}",headers=headers)
    assert res2.status_code == 200

def test_create_project_negative():
    body= {
    "title": "First project",
    "users": {
        "a24edb03-ae2b-4d91-9710-10a3dc16eb4": "admin"}
    }
    res= requests.post("https://ru.yougile.com/api-v2/projects",headers=headers, json=body)
    assert res.status_code == 400

def test_change_project_negative():
    body= {
    "title": "First project",
    "users": {
        "a24edb03-ae2b-4d91-9710-10a3dc16eb40": "admin"
    }
    }
    res= requests.post("https://ru.yougile.com/api-v2/projects",headers=headers, json=body)
    assert res.status_code == 201
    id = res.json()["id"]
    body = {"title": ""}
    res2 = requests.put(f"https://ru.yougile.com/api-v2/projects/{id}",headers=headers, json=body)
    assert res2.status_code == 400

def test_get_project_negative():
    id = 1
    res2 = requests.get(f"https://ru.yougile.com/api-v2/projects/{id}",headers=headers)
    assert res2.status_code == 404