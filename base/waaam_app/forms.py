from .models import VolunteerRecord

from django import forms
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django_select2 import forms as s2forms


class DateInput(forms.DateInput):
    input_type = 'date'


class NumberInput(forms.NumberInput):
    input_type = 'number'


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
