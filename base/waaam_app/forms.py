from .models import VolunteerRecord, Profile, ActivityChoice

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django_select2 import forms as s2forms


class DateInput(forms.DateInput):
    input_type = 'date'


class NumberInput(forms.NumberInput):
    input_type = 'number'


class SignUpForm(UserCreationForm):
    TRUE_FALSE_CHOICES = (
        (True, 'Yes'),
        (False, 'No')
    )

    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    # Profile Fields
    phone = forms.CharField(max_length=30, required=True, help_text='Required.')
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD',
                                 widget=DateInput(attrs={'id': 'dateTimePicker'}))
    medical_conditions = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 20}))
    areas_of_interest = forms.ModelMultipleChoiceField(queryset=ActivityChoice.objects.all(), required=False,
                                                       widget=forms.CheckboxSelectMultiple)
    photo_permission = forms.ChoiceField(choices=TRUE_FALSE_CHOICES, label="Permission to photograph/video",
                                         initial='', widget=forms.Select())
    emergency_contact = forms.CharField(label="Emergency Contact Name", required=True)
    emergency_contact_phone_number = forms.CharField(label="Emergency Contact Phone Number", required=True)
    volunteer_waiver_and_release = forms.CharField(max_length=50, required=True, help_text='Required.',
                                                   label="Volunteer Waiver and Release Signature")
    esignature_date = birth_date
    group = forms.CharField(max_length=256, required=False, label="Group Name",
                            help_text="Please indicate the group you are working with.")

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',
                  'group', 'phone', 'birth_date', 'medical_conditions', 'areas_of_interest', 'photo_permission',
                  'emergency_contact', 'emergency_contact_phone_number',
                  'volunteer_waiver_and_release', 'esignature_date')


class ProfileForm(forms.ModelForm):
    TRUE_FALSE_CHOICES = (
        (True, 'Yes'),
        (False, 'No')
    )

    phone = forms.CharField(max_length=30, required=True, help_text='Required.')
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD',
                                 widget=DateInput(attrs={'id': 'dateTimePicker'}))
    medical_conditions = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 20}))
    areas_of_interest = forms.ModelMultipleChoiceField(queryset=ActivityChoice.objects.all(), required=False,
                                                       widget=forms.CheckboxSelectMultiple)
    photo_permission = forms.ChoiceField(choices=TRUE_FALSE_CHOICES, label="Permission to photograph/video",
                                         initial='', widget=forms.Select())
    emergency_contact = forms.CharField(label="Emergency Contact Name", required=True)
    emergency_contact_phone_number = forms.CharField(label="Emergency Contact Phone Number", required=True)
    volunteer_waiver_and_release = forms.CharField(max_length=50, required=True, help_text='Required.',
                                                   label="Volunteer Waiver and Release Signature")
    esignature_date = birth_date
    group = forms.CharField(max_length=256, required=False, label="Group Name",
                            help_text="Please indicate the group you are working with.")

    class Meta:
        model = Profile
        fields = (
            'phone', 'birth_date', 'medical_conditions', 'areas_of_interest', 'photo_permission', 'emergency_contact',
            'emergency_contact_phone_number',
            'volunteer_waiver_and_release', 'esignature_date', 'group')
        widgets = {
            'medical_conditions': forms.Textarea(attrs={'rows': 4, 'cols': 20}),
        }


class UsersWidget(s2forms.ModelSelect2Widget):
    search_fields = [
        "first_name__icontains",
        "last_name__icontains",
    ]


class VolunteerRecordForm(forms.ModelForm):
    class Meta:
        model = VolunteerRecord
        fields = ('owner', 'activity', 'hours', 'description')
        # widgets = {
        #     "owner": UsersWidget,
        # }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-volunteerRecordForm'
        self.helper.form_class = ''
        self.helper.form_method = 'post'
        self.helper.form_action = ''

        self.fields['hours'].widget = forms.NumberInput(attrs={
            'required': True,
            'id': 'form_hours',
            'step': "0.25",
            'value': '4'
        })

        self.fields['description'].widget = forms.Textarea(attrs={
        })

        print(self.fields['owner'])

        self.helper.add_input(Submit('submit', 'Submit'))

    # hours = NumberInput(attrs={'id': 'form_hours', 'step': "0.25"})
    # description = forms.Textarea(attrs={'id': 'form_desc', 'rows': 4, 'cols': 20})


class FilterForm(forms.Form):
    start_date = forms.DateField(widget=DateInput)
    end_date = forms.DateField(widget=DateInput)

    def is_valid(self):

        valid = super(FilterForm, self).is_valid()
        if not valid:
            return valid

        start_year = self.cleaned_data['start_date'].year
        start_month = self.cleaned_data['start_date'].month
        start_day = self.cleaned_data['start_date'].day

        end_year = self.cleaned_data['end_date'].year
        end_month = self.cleaned_data['end_date'].month
        end_day = self.cleaned_data['end_date'].day

        if (start_year < end_year):
            return True
        elif (start_year > end_year):
            return False

        if (start_month < end_month):
            return True
        elif (start_month > end_month):
            return False

        if (start_day <= end_day):
            return True

        return False


class AddVolunteerForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.')

    class Meta:
        model = User
        fields = ('first_name', 'last_name')
