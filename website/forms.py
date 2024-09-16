from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser  # Make sure to import your custom user model


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=15, required=False)
    name = forms.CharField(max_length=100, required=False)
    date_of_birth = forms.DateField(required=False)
    gender = forms.ChoiceField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], required=False)
    terms = forms.BooleanField(required=True, label="I agree to the Terms and Conditions")

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone_number', 'name', 'date_of_birth', 'gender', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.phone_number = self.cleaned_data.get('phone_number')
        user.name = self.cleaned_data.get('name')
        user.date_of_birth = self.cleaned_data.get('date_of_birth')
        user.gender = self.cleaned_data.get('gender')
        
        if commit:
            user.save()
        return user
    
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['email', 'name', 'phone_no', 'type', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4, 'cols': 15}),
        }


