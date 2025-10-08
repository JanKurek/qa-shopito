import pytest

@pytest.mark.api
def test_get_users_list(api, api_base_url):
    r = api.get(f"{api_base_url}/users?limit=10")
    assert r.status_code == 200
    body = r.json()
    assert "users" in body and isinstance(body["users"], list)
    assert len(body["users"]) > 0


@pytest.mark.api
@pytest.mark.parametrize("user_id,expected_code", [(1, 200), (99999, 404)])
def test_get_single_user(api, api_base_url, user_id, expected_code):
    r = api.get(f"{api_base_url}/users/{user_id}")
    assert r.status_code == expected_code


@pytest.mark.api
def test_create_user(api, api_base_url):
    payload = {"firstName": "Jan", "lastName": "QA", "age": 28}
    r = api.post(f"{api_base_url}/users/add", json=payload)
    assert r.status_code in (200, 201)  # ✅ upravené
    body = r.json()
    assert body.get("firstName") == "Jan"
    assert "id" in body


@pytest.mark.api
def test_update_user(api, api_base_url):
    payload = {"lastName": "Senior"}
    r = api.put(f"{api_base_url}/users/1", json=payload)
    assert r.status_code == 200
    assert r.json().get("lastName") == "Senior"


@pytest.mark.api
def test_delete_user(api, api_base_url):
    r = api.delete(f"{api_base_url}/users/1")
    assert r.status_code == 200
    body = r.json()
    # niekedy vracia mocknutú štruktúru; stačí, že je JSON a OK kód
    assert isinstance(body, dict)
