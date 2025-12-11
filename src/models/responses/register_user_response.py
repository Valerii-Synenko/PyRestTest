from pydantic import BaseModel, field_validator


class RegisterUserResponseModel(BaseModel):
    """
    The model for register user response.
    The response has only one field - id.
    """

    id: str

    @field_validator("id")
    def validate_age(cls, v):
        if len(v) != 24:
            raise ValueError(f"id must be string with 24 characters, but got {v}")
        return v
