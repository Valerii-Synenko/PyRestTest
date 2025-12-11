from __future__ import annotations

from typing import Optional, Any

from pydantic import BaseModel


class RegisterUserRequestsModel(BaseModel):
    """
    Representation of payload model for API request to user registration.
    Fields use `Any` so that you can generate any malformed data needed for negative testing as well
    as valid data for positive testing.

    Mandatory Fields:
      - username,
      - password,
      - email
    """

    username: Any
    password: Any
    email: Any
    firstName: Optional[Any] = None
    lastName: Optional[Any] = None
