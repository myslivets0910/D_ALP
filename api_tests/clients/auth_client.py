from api_tests.clients.base_client import BaseClient


class AuthClientTokens(BaseClient):


    # AUTH_EMAIL_TOKENS = 'auth/tokens'

    def login(self, email: str, password: str):

        payload = {
            "email": email,
            "password": password,
        }

        return self._post("auth/tokens", json=payload)
