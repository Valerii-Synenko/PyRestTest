import os

import pytest
from dotenv import load_dotenv
from faker import Faker

from src.api_clients.user_client import UserClient

load_dotenv()


@pytest.fixture
def faker() -> Faker:
    """
    The fixture provides client for Faker.
    The client has customizable locale.

    Returns:
        Faker: Faker object

    """
    locale: str | None = os.getenv("FAKER_LOCALE")

    return Faker(locale=locale)


@pytest.fixture
def user_client():
    """Crete UserClient object. And after test close the session."""
    client = UserClient()
    yield client
    client.close_session()
