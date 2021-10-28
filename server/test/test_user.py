from fastapi import status
from fastapi.testclient import TestClient

from server.main import app

import pytest, secrets

client = TestClient(app)

TOKEN = ''

mkuser = lambda : secrets.token_urlsafe(4).lower()

header = {
    'Content-Type': 'application/json',
}

user_id = mkuser()
test_user = {
    'id': 'czgp8a',
    'name': 'hongczgp8a', 
    'email': f'czgp8a@gmail.com',
    'paasword': 'gildong123',
    'is_active': True
}

user_id = mkuser()
test_create_uesr_data = {
    'id': user_id,
    'name': f'hong{user_id}', 
    'email': f'{user_id}@gmail.com',
    'password': 'gildong123',
    'is_active': True
}

update_user_id = mkuser()
test_update_user_data = {
    'id': user_id,
    'name': f'hong{update_user_id}', 
    'email': f'{update_user_id}@gmail.com',
    'email': f'{update_user_id}@naver.com',
    'password': 'changedgildong123',
    'is_active': False
}

before = None
after = None

@pytest.mark.parametrize('endpoint,status_code', [('/token', status.HTTP_200_OK)])
def test_create_token(endpoint: str, status_code: int):
    res = client.post(endpoint, json=test_user, headers=header)
    contents = res.json()
    
    assert res.status_code == status_code
    assert type(contents['result']['token']) == str
    TOKEN = contents['result']['token']
    header.update({'Authorization': f'token {TOKEN}'})

@pytest.mark.parametrize('endpoint,status_code', [('/users', status.HTTP_200_OK)])
def test_create_user(endpoint: str, status_code: int):
    global before
    res = client.post(endpoint, headers=header, json=test_create_uesr_data)
    contents = res.json()
    
    before = contents['result']
    assert res.status_code == status_code
    
@pytest.mark.parametrize('endpoint,status_code', [(f'/users/{test_user["id"]}', status.HTTP_200_OK)])
def test_read_user(endpoint: str, status_code: int):
    res = client.get(endpoint, headers=header)
    contents = res.json()
    
    assert res.status_code == status_code
    
@pytest.mark.parametrize('endpoint,status_code', [(f'/users/{test_user["id"]}', status.HTTP_200_OK)])
def test_update_user(endpoint: str, status_code: int):
    global before
    import time
    time.sleep(1)
    res= client.put(endpoint, headers=header, json=test_update_user_data)
    contents = res.json()
    
    assert res.status_code == status_code
    assert contents['result']['id'] == test_create_uesr_data['id']
    
    for k in contents['result'].keys():
        if k == 'id' or k == 'created_at':
            assert contents['result'][k] == before[k]
        else:
            assert contents['result'][k] != before[k]
            
@pytest.mark.parametrize('endpoint,status_code', [(f'/users/{test_user["id"]}', status.HTTP_200_OK)])
def test_delete_user(endpoint: str, status_code: int):
    res = client.delete(endpoint, headers=header)
    contents = res.json()
    
    assert res.status_code == status_code
    assert contents['result']['success'] == False
    
    res = client.get(endpoint, headers=header, json=test_user)
    contents = res.json()
    
    assert contents['result'] == {}