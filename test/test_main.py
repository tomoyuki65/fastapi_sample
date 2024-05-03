from .test_settings import *
import config

@pytest.mark.asyncio
async def test_main(async_client):
    response = await async_client.get("/")
    assert response.status_code == starlette.status.HTTP_200_OK
    assert response.text == "Hello World !!"

@pytest.mark.asyncio
async def test_env(async_client):
    response = await async_client.get("/env")
    assert response.status_code == starlette.status.HTTP_200_OK

    data = {
        "ENV": config.settings.env,
        "TZ": config.settings.tz,
        "MYSQL_DATABASE": config.settings.mysql_database,
        "MYSQL_USER": config.settings.mysql_user,
        "MYSQL_PASSWORD": config.settings.mysql_password,
        "MYSQL_ROOT_PASSWORD": config.settings.mysql_root_password,
    }
    assert response.json() == data