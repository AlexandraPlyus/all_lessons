import pytest
import requests
import json
from for_lesson_08 import KEY

url = "https://yougile.com"

def test_create_project():
    my_headers = {
        "Authorization": f"Bearer {KEY}"
    }
    body = {
        "title": "ГосУслуги"
    }
    respone = requests.post(url+"/api-v2/projects", json=body, headers=my_headers)

    assert respone.status_code == 201

def test_create_project_no_title():
    my_headers = {
        "Authorization": f"Bearer {KEY}"
    }
    body = {
        "title": ""
    }
    respone = requests.post(url+"/api-v2/projects", json=body, headers=my_headers)
    body_respone = respone.json()
    assert respone.status_code == 400
    assert body_respone["message"] == ['title should not be empty']


def test_rename_project():

    # Создать проект
    my_headers = {
        "Authorization": f"Bearer {KEY}"
    }
    body = {
        "title": "ГосУслуги"
    }
    respone = requests.post(url+"/api-v2/projects", json=body, headers=my_headers)

    body_respone = respone.json()
    id = body_respone["id"]

    assert len(body_respone) > 0
    assert respone.status_code == 201

    # Рeдактировать название проекта
    body = {
        "title": "Гос"
    }
    respone = requests.put(f"{url}/api-v2/projects/{id}", json=body, headers=my_headers)
    assert respone.status_code == 200

def test_rename_project_empty_name():

    # Создать проект
    my_headers = {
        "Authorization": f"Bearer {KEY}"
    }
    body = {
        "title": "ГосУслуги"
    }
    respone = requests.post(url+"/api-v2/projects", json=body, headers=my_headers)

    body_respone = respone.json()
    id = body_respone["id"]

    assert len(body_respone) > 0
    assert respone.status_code == 201

    # Рeдактировать название проекта
    body = {
        "title": ""
    }
    
    respone = requests.put(f"{url}/api-v2/projects/{id}", json=body, headers=my_headers)
    body_respone = respone.json()
    
    assert respone.status_code == 400
    assert body_respone["message"] == ["title should not be empty"]

def test_get_by_id():
    
    title_project = "ГсУслуги"

    # Создать проект
    my_headers = {
        "Authorization": f"Bearer {KEY}"
    }
    body = {
        "title": title_project
    }
    respone = requests.post(url+"/api-v2/projects", json=body, headers=my_headers)
    body_respone = respone.json()

    id_project = body_respone["id"]

    assert respone.status_code == 201

    # Получение по id
    respone = requests.get(f"{url}/api-v2/projects/{id_project}", headers=my_headers)
    assert respone.status_code == 200

def test_get_by_empty_id():
    id_project = ""
    respone = requests.get(f"{url}/api-v2/projects/{id_project}")
    assert respone.status_code == 401

def test_get_projects():
    my_headers = {
        "Authorization": f"Bearer {KEY}"
    }
    respone = requests.get(f"{url}/api-v2/projects", headers=my_headers)
    assert respone.status_code == 200


def test_delete_project():
    id = "10e06011-5fe0-4dde-9040-189f9e624b35"
    my_headers = {
        "Authorization": f"Bearer {KEY}"
    }
    
    body = {
        "deleted": True
    }

    respone = requests.put(f"{url}/api-v2/projects/{id}", json=body, headers=my_headers)
    assert respone.status_code == 200

  

