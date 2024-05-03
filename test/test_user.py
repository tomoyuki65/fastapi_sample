from .test_settings import *
import warnings

@pytest.mark.asyncio
async def test_create_user(async_client):
    response = await async_client.post("/user", json={
                   "uid": "ABC10001",
                   "name": "田中 太郎",
                   "email": "taro-1@example.com"
               })
    assert response.status_code == starlette.status.HTTP_201_CREATED
    assert response.json() == { "message": "OK" }

@pytest.mark.asyncio
async def test_get_user(async_client):
    await async_client.post("/user", json={
        "uid": "ABC10001",
        "name": "田中 太郎",
        "email": "taro-1@example.com"
    })

    # 日付項目のフォーマット変換部分で警告が出るので無視する
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", UserWarning)
        response = await async_client.get("/user/ABC10001")
    
    assert response.status_code == starlette.status.HTTP_200_OK
    data = response.json()
    assert data['uid'] == "ABC10001"
    assert data['name'] == "田中 太郎"
    assert data['email'] == "taro-1@example.com"
    assert data['created_at'] != None
    assert data['updated_at'] != None
    assert data['deleted_at'] == None

@pytest.mark.asyncio
async def test_update_user(async_client):
    await async_client.post("/user", json={
        "uid": "ABC10001",
        "name": "田中 太郎",
        "email": "taro-1@example.com"
    })

    # ユーザー更新
    response = await async_client.put("/user/ABC10001", json={
                   "name": "佐々木 二郎",
                   "email": "sasaki-1@example.com"
               })

    assert response.status_code == starlette.status.HTTP_200_OK
    assert response.json() == { "message": "OK" }

    # DBのデータ確認
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", UserWarning)
        response2 = await async_client.get("/user/ABC10001")
    
    assert response2.status_code == starlette.status.HTTP_200_OK
    data = response2.json()
    assert data['uid'] == "ABC10001"
    assert data['name'] == "佐々木 二郎"
    assert data['email'] == "sasaki-1@example.com"
    assert data['created_at'] != None
    assert data['updated_at'] != None
    assert data['deleted_at'] == None

@pytest.mark.asyncio
async def test_delete_user(async_client):
    await async_client.post("/user", json={
        "uid": "ABC10001",
        "name": "田中 太郎",
        "email": "taro-1@example.com"
    })

    # ユーザー削除
    response = await async_client.delete("/user/ABC10001")
    assert response.status_code == starlette.status.HTTP_200_OK

    # DBのデータ確認
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", UserWarning)
        response2 = await async_client.get("/user/ABC10001")
    
    assert response2.status_code == starlette.status.HTTP_200_OK
    assert response2.json() == None

    # 削除済みデータ確認
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", UserWarning)
        response3 = await async_client.get("/users")
    
    assert response3.status_code == starlette.status.HTTP_200_OK
    data = response3.json()[0]
    assert data['uid'] == "ABC10001"
    assert data['name'] == "田中 太郎"
    assert data['email'] == "taro-1@example.com"
    assert data['created_at'] != None
    assert data['updated_at'] != None
    assert data['deleted_at'] != None

@pytest.mark.asyncio
async def test_get_users(async_client):
    await async_client.post("/user", json={
        "uid": "ABC10001",
        "name": "田中 太郎",
        "email": "taro-1@example.com"
    })
    await async_client.post("/user", json={
        "uid": "ABC10002",
        "name": "佐藤 三郎",
        "email": "sato-3@example.com"
    })

    # DBのデータ確認
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", UserWarning)
        response = await async_client.get("/users")
    
    data1 = response.json()[0]
    data2 = response.json()[1]

    assert data1['uid'] == "ABC10001"
    assert data1['name'] == "田中 太郎"
    assert data1['email'] == "taro-1@example.com"
    assert data1['created_at'] != None
    assert data1['updated_at'] != None
    assert data1['deleted_at'] == None

    assert data2['uid'] == "ABC10002"
    assert data2['name'] == "佐藤 三郎"
    assert data2['email'] == "sato-3@example.com"
    assert data2['created_at'] != None
    assert data2['updated_at'] != None
    assert data2['deleted_at'] == None
