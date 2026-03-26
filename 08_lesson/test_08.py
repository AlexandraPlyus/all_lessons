import requests
from ClassForLesson08 import GetKey

url = "https://yougile.com"
get_key_exemplar = GetKey(url)

KEY = get_key_exemplar.get_key()


def test_create_project():

    my_headers = {"Authorization": f"Bearer {KEY}"}

    # Создать проект
    body = {"title": "ГосУслуги"}
    respone = requests.post(
        url + "/api-v2/projects", json=body, headers=my_headers
    )
    respone_body = respone.json()
    id = respone_body["id"]
    assert respone.status_code == 201

    # Удалить проект
    body = {"deleted": True}
    respone = requests.put(
        f"{url}/api-v2/projects/{id}", json=body, headers=my_headers
    )
    assert respone.status_code == 200


def test_create_project_no_title():
    my_headers = {"Authorization": f"Bearer {KEY}"}
    body = {"title": ""}
    respone = requests.post(
        url + "/api-v2/projects", json=body, headers=my_headers
    )
    body_respone = respone.json()
    assert respone.status_code == 400
    assert body_respone["message"] == ["title should not be empty"]


def test_rename_project():

    # Создать проект
    my_headers = {"Authorization": f"Bearer {KEY}"}
    body = {"title": "ГосУслуги"}
    respone = requests.post(
        url + "/api-v2/projects", json=body, headers=my_headers
    )

    body_respone = respone.json()
    id = body_respone["id"]

    assert len(body_respone) > 0
    assert respone.status_code == 201

    # Рeдактировать название проекта
    body = {"title": "Гос"}
    respone = requests.put(
        f"{url}/api-v2/projects/{id}", json=body, headers=my_headers
    )
    assert respone.status_code == 200

    # Удалить проект
    body = {"deleted": True}
    respone = requests.put(
        f"{url}/api-v2/projects/{id}", json=body, headers=my_headers
    )
    assert respone.status_code == 200


def test_rename_project_empty_name():

    # Создать проект
    my_headers = {"Authorization": f"Bearer {KEY}"}
    body = {"title": "ГосУслуги"}
    respone = requests.post(
        url + "/api-v2/projects", json=body, headers=my_headers
    )

    body_respone = respone.json()
    id = body_respone["id"]

    assert len(body_respone) > 0
    assert respone.status_code == 201

    # Рeдактировать название проекта
    body = {"title": ""}

    respone = requests.put(
        f"{url}/api-v2/projects/{id}", json=body, headers=my_headers
    )
    body_respone = respone.json()

    assert respone.status_code == 400
    assert body_respone["message"] == ["title should not be empty"]

    # Удалить проект
    body = {"deleted": True}
    respone = requests.put(
        f"{url}/api-v2/projects/{id}", json=body, headers=my_headers
    )
    assert respone.status_code == 200


def test_get_by_id():

    title_project = "ГсУслуги"

    # Создать проект
    my_headers = {"Authorization": f"Bearer {KEY}"}
    body = {"title": title_project}
    respone = requests.post(
        url + "/api-v2/projects", json=body, headers=my_headers
    )
    body_respone = respone.json()

    id = body_respone["id"]

    assert respone.status_code == 201

    # Получение по id
    respone = requests.get(f"{url}/api-v2/projects/{id}", headers=my_headers)
    assert respone.status_code == 200

    # Удалить проект
    body = {"deleted": True}
    respone = requests.put(
        f"{url}/api-v2/projects/{id}", json=body, headers=my_headers
    )
    assert respone.status_code == 200


def test_get_by_empty_id():
    id_project = ""
    respone = requests.get(f"{url}/api-v2/projects/{id_project}")
    assert respone.status_code == 401
