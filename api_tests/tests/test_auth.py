import pytest



class TestAuthClientIncorrectTokens:

    def test_auth_post_not_token(self,auth_client):
        """Авторизация без токена"""
        response = auth_client.login("eve.holt@reqres.in", "cityslicka")

        data = response.json()
        assert response.status_code == 401, "Ошибка! Авторизаия прошла"
        print(data)
        assert "Invalid credentials" in data["message"]

    def test_auth_post_random_token(self,auth_client):
        """Авторизация с рандомным токеном"""

        response = auth_client.login("auth11@m.ru", "7tRuweP3")
        assert response.status_code == 200

        data = response.json()["two_factor_session_token"]
        print(data)
