from __future__ import annotations

from typing import Optional, Any

from pydantic import BaseModel


class Model(BaseModel):
    """
    Representation of payload model for API request to user registration.
    This model is intentionally NOT validated.
    You can use any values you want in your payload model.

    Fields use `Any` so that we can generate:
      - invalid types,
      - invalid formats,
      - missing fields,
      - empty strings,
      - or any malformed data needed for negative testing.
    """

    username: Any
    password: Any
    email: Any
    firstName: Optional[Any] = None
    lastName: Optional[Any] = None
