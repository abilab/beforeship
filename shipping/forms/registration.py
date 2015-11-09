from django.contrib.auth.forms import UserCreationForm


class EnchancedUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ("username", "email")
