from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Assessment

# No need to redefine UserCreationForm or AuthenticationForm,
# as we're using Django's built-in versions.

# Custom form for vehicle assessment submissions
class AssessmentForm(forms.ModelForm):
    class Meta:
        model = Assessment
        fields = ['image', 'description']  # assuming your Assessment model has an 'image' and 'description' field
        # Customize the labels or help_texts here, if needed.

    def __init__(self, *args, **kwargs):
        super(AssessmentForm, self).__init__(*args, **kwargs)
        # Here, you can further customize the form, like setting placeholders, classes, or other attributes
        self.fields['image'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})