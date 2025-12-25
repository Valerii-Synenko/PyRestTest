from __future__ import annotations

from typing import Annotated

from pydantic import BaseModel, Field


class RegisterUserRequestsModel(BaseModel):
    """
    Representation of payload model for API request to user registration.

    Mandatory Fields:
      - username,
      - password,
      - email,

    Optional Fields:
      - firstName,
      - lastName,
    """

    username: Annotated[str, Field(min_length=1)]
    password: Annotated[str, Field(min_length=1)]
    email: Annotated[str, Field(min_length=1)]
    firstName: Annotated[str | None, Field(min_length=1)] = None
    lastName: Annotated[str | None, Field(min_length=1)] = None
