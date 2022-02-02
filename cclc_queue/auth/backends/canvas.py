from social_core.backends.oauth import BaseOAuth2


class CanvasOAuth2(BaseOAuth2):
    """
    Python Social Auth backend for Canvas LMS

    See:
    * https://canvas.instructure.com/doc/api/file.oauth.html
    * https://canvas.instructure.com/doc/api/file.oauth_endpoints.html
    """

    name = "canvas-oauth2"
    AUTHORIZATION_URL = "https://{base_url}/login/oauth2/auth"
    ACCESS_TOKEN_URL = "https://{base_url}/login/oauth2/token"
    ACCESS_TOKEN_METHOD = "POST"
    REFRESH_TOKEN_URL = "https://{base_url}/login/oauth2/token"
    REFRESH_TOKEN_METHOD = "POST"
    SCOPE_SEPARATOR = " "

    @property
    def base_url(self):
        return self.setting("BASE_URL", "canvas.instructure.com")

    def authorization_url(self):
        return self.AUTHORIZATION_URL.format(base_url=self.base_url)

    def access_token_url(self):
        return self.ACCESS_TOKEN_URL.format(base_url=self.base_url)

    def refresh_token_url(self):
        return self.REFRESH_TOKEN_URL.format(base_url=self.base_url)

    def get_user_details(self, response):
        """
        Return user details from Canvas LMS account

        See https://canvas.instructure.com/doc/api/users.html#User
        """
        return {
            "username": str(response.get("login_id")),
            "email": response.get("email"),
            "fullname": response.get("name"),
            "first_name": response.get("first_name"),
            "last_name": response.get("last_name"),
        }

    def user_data(self, access_token, *args, **kwargs):
        """
        Loads user data from service

        See https://canvas.instructure.com/doc/api/users.html#method.users.api_show
        """
        return self.get_json(
            f"https://{self.base_url}/api/v1/users/self",
            headers={"Authorization": f"Bearer {access_token}"},
            method="GET",
        )
