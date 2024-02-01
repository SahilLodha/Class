from django.contrib.auth.mixins import LoginRequiredMixin


class SuperUserMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if not request.user.is_superuser:
                return self.handle_no_permission()
        else:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)