"""User API client for user-related operations."""

import requests

from src.api_clients.base_client import BaseClient
from src.models.requests.register_user_requests import RegisterUserRequestsModel


class UserClient(BaseClient):
    """
    Client for user management API endpoints.

    Handles user registration, authentication, and profile operations.
    """

    def __init__(self):
        """Initialize UserClient with 'register' endpoint."""
        super().__init__("register")

    def user_register(self, user_model: RegisterUserRequestsModel) -> requests.Response:
        """
        Register a new user.

        Args:
            user_model: User registration Pydantic model.

        Returns:
            Response object containing registration result and user data.
        """
        response = self.session.post(
            url=self.endpoint,
            json=user_model.model_dump(exclude_none=True),
        )
        return response
