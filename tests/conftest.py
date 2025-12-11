import pytest
from faker import Faker


@pytest.fixture
def faker() -> Faker:
    """
    The fixture provides client for Faker.
    By default, it is using Croatian locale.

    Returns:
        Faker: Faker object

    """
    return Faker(locale="hr_HR")
