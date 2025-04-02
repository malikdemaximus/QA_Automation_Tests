import requests

def test_google_status(api_client):
    response = requests.get(f"{api_client}/get")
    assert response.status_code == 200, f"Ошибка: {response.status_code}"
def test_json_response(api_client):
    response = requests.get(f"{api_client}/get")
    json_data = response.json()
    assert "url" in json_data, "Ошибка: поле 'url' отсутствует в JSON"
def test_post_request(api_client):
    data = {"name": "Malik", "job": "QA Engineer"}
    response = requests.post(f"{api_client}/post", json=data)
    json_data = response.json()
    
    assert response.status_code == 200, "Ошибка: статус не 200"
    assert json_data["json"] == data, "Ошибка: Данные не совпадают"

def test_404_not_found(api_client):
    response = requests.get(f"{api_client}/status/404")
    assert response.status_code == 404, "Ошибка: ожидали 404"

def test_invalid_post_request(api_client):
    response = requests.post(f"{api_client}/post", data="invalid_data")
    assert response.status_code == 200  # API принимает данные, но вернет ошибку в JSON
    json_data = response.json()
    assert json_data["json"] is None, "Ошибка: JSON не должен обрабатываться"
