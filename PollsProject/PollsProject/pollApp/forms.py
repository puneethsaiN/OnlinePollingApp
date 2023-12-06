from django.forms import ModelForm
from .models import poll

class CreatePollForm(ModelForm):
    class Meta:
        model = poll
        fields = ("question","opt1", "opt2", "opt3",)
    