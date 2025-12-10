from pydantic import BaseModel, field_validator


class RegisterUserResponse(BaseModel):
    id: str

    @field_validator("id")
    def validate_age(cls, v):
        if len(v) != 24:
            raise ValueError(f"id must be string with 24 characters, but got {v}")
        return v
