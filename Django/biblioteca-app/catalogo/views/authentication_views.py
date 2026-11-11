from django.contrib.auth.views import LoginView, LogoutView


class BibliotecaloginView(LoginView):
    template_name = 'catalogo/cuentas/login.html'
    redirect_authenticated_user = True


class Bibliotecalogout_view(LogoutView):
    pass
