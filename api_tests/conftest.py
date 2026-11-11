import os
import pytest

from dotenv import load_dotenv

from api_tests.clients.auth_client import AuthClientTokens
from api_tests.clients.base_client import BaseClient

load_dotenv()



@pytest.fixture(scope="session")
def api_client():
    # Базовый URL  API для тестов
    base_url = os.getenv("ALPIRA_2_URL")
    client = BaseClient(base_url)
    yield client
    client.session.close()


@pytest.fixture(scope="session")
def auth_client():
    client = AuthClientTokens(base_url=os.getenv("ALPIRA_2_URL"))
    yield client
    client.session.close()
