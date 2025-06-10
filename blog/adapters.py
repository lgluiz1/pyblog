from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

class MySocialAccountAdapter(DefaultSocialAccountAdapter):
    def get_connect_view(self, request, *args, **kwargs):
        # Pula a confirmação e redireciona imediatamente
        from allauth.socialaccount.providers.oauth2.views import OAuth2LoginView
        return OAuth2LoginView.adapter_view(self.get_provider().get_adapter())(request, *args, **kwargs)
