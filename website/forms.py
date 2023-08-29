from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Customer, Address


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label='',
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    first_name = forms.CharField(label='', max_length=100,
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First name'}))
    last_name = forms.CharField(label='', max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last name'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '''<span class="form-text text-muted">
                                               <small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small>
                                               </span>'''

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '''<ul class="form-text text-muted small">
                                                <li>Your password can\'t be too similar to your other personal information.</li>
                                                <li>Your password must contain at least 8 characters.</li>
                                                <li>Your password can\'t be a commonly used password.</li>
                                                <li>Your password can\'t be entirely numeric.</li>
                                                </ul>'''

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '''<span class="form-text text-muted">
                                                <small>Enter the same password as before, for verification.</small>
                                                </span>'''

# Create Form to add customer
class AddCustomerForm(forms.ModelForm):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    first_name = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={"placeholder": "First Name", "class": "form-control"}),
        label=""
    )
    last_name = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={"placeholder": "Last Name", "class": "form-control"}),
        label=""
    )
    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"}),
        label="Gender"
    )
    email = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={"placeholder": "Email", "class": "form-control"}),
        label=""
    )
    phone = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={"placeholder": "Phone", "class": "form-control"}),
        label=""
    )

    class Meta:
        model = Customer
        exclude = ('membership',)

# create form to add customer address
class AddAddressFrom(forms.ModelForm):
    country = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={"placeholder": "Country", "class": "form-control"}),
        label=""
    )
    city = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={"placeholder": "City", "class": "form-control"}),
        label=""
    )
    state = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={"placeholder": "State", "class": "form-control"}),
        label=""
    )
    zipcode = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={"placeholder": "Zipcode", "class": "form-control"}),
        label=""
    )
    street = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={"placeholder": "Street", "class": "form-control"}),
        label=""
    )
    class Meta:
        model = Address
        exclude = ('customer_id',)
