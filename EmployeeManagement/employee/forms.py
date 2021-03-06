import re
from employee.views import *
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from employee.models import Employee, ProjectDetails


GENDER_CHOICES = [("Male", "Male"),
                  ("Female", "Female"),
                  ("Other", "Other")]
MERITAL_STATUS_CHOICES = [("SINGLE", "SINGLE"),
                          ("MARRIED", "MARRIED")]

emp_designation = [("SOFTWARE ANALYST", "SOFTWARE ANALYST"),
                   ("SOFTWARE CONSULTANT", "SOFTWARE CONSULTANT"),
                   ("SENIOR CONSULTANT", "SENIOR CONSULTANT"),
                   ("MANAGER", "MANAGER")]

COUNTRY_CHOICES = (
    ('Andorra', _(u"Andorra")),
    ('UAE', _(u"United Arab Emirates")),
    ('Afghanistan', _(u"Afghanistan")),
    ('Antigua and Barbuda', _(u"Antigua and Barbuda")),
    ('Anguilla', _(u"Anguilla")),
    ('AL', _(u"Albania")),
    ('AM', _(u"Armenia")),
    ('AN', _(u"Netherlands Antilles")),
    ('AO', _(u"Angola")),
    ('AQ', _(u"Antarctica")),
    ('AR', _(u"Argentina")),
    ('AS', _(u"American Samoa")),
    ('AT', _(u"Austria")),
    ('AU', _(u"Australia")),
    ('AW', _(u"Aruba")),
    ('AX', _(u"Åland Islands")),
    ('AZ', _(u"Azerbaijan")),
    ('BA', _(u"Bosnia and Herzegovina")),
    ('BB', _(u"Barbados")),
    ('BD', _(u"Bangladesh")),
    ('BE', _(u"Belgium")),
    ('BF', _(u"Burkina Faso")),
    ('BG', _(u"Bulgaria")),
    ('BH', _(u"Bahrain")),
    ('BI', _(u"Burundi")),
    ('BJ', _(u"Benin")),
    ('BL', _(u"Saint Barthélemy")),
    ('BM', _(u"Bermuda")),
    ('BN', _(u"Brunei Darussalam")),
    ('BO', _(u"Bolivia, Plurinational State of")),
    ('BR', _(u"Brazil")),
    ('BS', _(u"Bahamas")),
    ('BT', _(u"Bhutan")),
    ('BV', _(u"Bouvet Island")),
    ('BW', _(u"Botswana")),
    ('BY', _(u"Belarus")),
    ('BZ', _(u"Belize")),
    ('CA', _(u"Canada")),
    ('CC', _(u"Cocos (Keeling) Islands")),
    ('CD', _(u"Congo, the Democratic Republic of the")),
    ('CF', _(u"Central African Republic")),
    ('CG', _(u"Congo")),
    ('CH', _(u"Switzerland")),
    ('CI', _(u"Côte d'Ivoire")),
    ('CK', _(u"Cook Islands")),
    ('CL', _(u"Chile")),
    ('CM', _(u"Cameroon")),
    ('CN', _(u"China")),
    ('CO', _(u"Colombia")),
    ('CR', _(u"Costa Rica")),
    ('CU', _(u"Cuba")),
    ('CV', _(u"Cape Verde")),
    ('CX', _(u"Christmas Island")),
    ('CY', _(u"Cyprus")),
    ('CZ', _(u"Czech Republic")),
    ('DE', _(u"Germany")),
    ('DJ', _(u"Djibouti")),
    ('DK', _(u"Denmark")),
    ('DM', _(u"Dominica")),
    ('DO', _(u"Dominican Republic")),
    ('DZ', _(u"Algeria")),
    ('EC', _(u"Ecuador")),
    ('EE', _(u"Estonia")),
    ('EG', _(u"Egypt")),
    ('EH', _(u"Western Sahara")),
    ('ER', _(u"Eritrea")),
    ('ES', _(u"Spain")),
    ('ET', _(u"Ethiopia")),
    ('FI', _(u"Finland")),
    ('FJ', _(u"Fiji")),
    ('FK', _(u"Falkland Islands (Malvinas)")),
    ('FM', _(u"Micronesia, Federated States of")),
    ('FO', _(u"Faroe Islands")),
    ('FR', _(u"France")),
    ('GA', _(u"Gabon")),
    ('GB', _(u"United Kingdom")),
    ('GD', _(u"Grenada")),
    ('GE', _(u"Georgia")),
    ('GF', _(u"French Guiana")),
    ('GG', _(u"Guernsey")),
    ('GH', _(u"Ghana")),
    ('GI', _(u"Gibraltar")),
    ('GL', _(u"Greenland")),
    ('GM', _(u"Gambia")),
    ('GN', _(u"Guinea")),
    ('GP', _(u"Guadeloupe")),
    ('GQ', _(u"Equatorial Guinea")),
    ('GR', _(u"Greece")),
    ('GS', _(u"South Georgia and the South Sandwich Islands")),
    ('GT', _(u"Guatemala")),
    ('GU', _(u"Guam")),
    ('GW', _(u"Guinea-Bissau")),
    ('GY', _(u"Guyana")),
    ('HK', _(u"Hong Kong")),
    ('HM', _(u"Heard Island and McDonald Islands")),
    ('HN', _(u"Honduras")),
    ('HR', _(u"Croatia")),
    ('HT', _(u"Haiti")),
    ('HU', _(u"Hungary")),
    ('ID', _(u"Indonesia")),
    ('IE', _(u"Ireland")),
    ('IL', _(u"Israel")),
    ('IM', _(u"Isle of Man")),
    ('IN', _(u"India")),
    ('IO', _(u"British Indian Ocean Territory")),
    ('IQ', _(u"Iraq")),
    ('IR', _(u"Iran, Islamic Republic of")),
    ('IS', _(u"Iceland")),
    ('IT', _(u"Italy")),
    ('JE', _(u"Jersey")),
    ('JM', _(u"Jamaica")),
    ('JO', _(u"Jordan")),
    ('JP', _(u"Japan")),
    ('KE', _(u"Kenya")),
    ('KG', _(u"Kyrgyzstan")),
    ('KH', _(u"Cambodia")),
    ('KI', _(u"Kiribati")),
    ('KM', _(u"Comoros")),
    ('KN', _(u"Saint Kitts and Nevis")),
    ('KP', _(u"Korea, Democratic People's Republic of")),
    ('KR', _(u"Korea, Republic of")),
    ('KW', _(u"Kuwait")),
    ('KY', _(u"Cayman Islands")),
    ('KZ', _(u"Kazakhstan")),
    ('LA', _(u"Lao People's Democratic Republic")),
    ('LB', _(u"Lebanon")),
    ('LC', _(u"Saint Lucia")),
    ('LI', _(u"Liechtenstein")),
    ('LK', _(u"Sri Lanka")),
    ('LR', _(u"Liberia")),
    ('LS', _(u"Lesotho")),
    ('LT', _(u"Lithuania")),
    ('LU', _(u"Luxembourg")),
    ('LV', _(u"Latvia")),
    ('LY', _(u"Libyan Arab Jamahiriya")),
    ('MA', _(u"Morocco")),
    ('MC', _(u"Monaco")),
    ('MD', _(u"Moldova, Republic of")),
    ('ME', _(u"Montenegro")),
    ('MF', _(u"Saint Martin (French part)")),
    ('MG', _(u"Madagascar")),
    ('MH', _(u"Marshall Islands")),
    ('MK', _(u"Macedonia, the former Yugoslav Republic of")),
    ('ML', _(u"Mali")),
    ('MM', _(u"Myanmar")),
    ('MN', _(u"Mongolia")),
    ('MO', _(u"Macao")),
    ('MP', _(u"Northern Mariana Islands")),
    ('MQ', _(u"Martinique")),
    ('MR', _(u"Mauritania")),
    ('MS', _(u"Montserrat")),
    ('MT', _(u"Malta")),
    ('MU', _(u"Mauritius")),
    ('MV', _(u"Maldives")),
    ('MW', _(u"Malawi")),
    ('MX', _(u"Mexico")),
    ('MY', _(u"Malaysia")),
    ('MZ', _(u"Mozambique")),
    ('NA', _(u"Namibia")),
    ('NC', _(u"New Caledonia")),
    ('NE', _(u"Niger")),
    ('NF', _(u"Norfolk Island")),
    ('NG', _(u"Nigeria")),
    ('NI', _(u"Nicaragua")),
    ('NL', _(u"Netherlands")),
    ('NO', _(u"Norway")),
    ('NP', _(u"Nepal")),
    ('NR', _(u"Nauru")),
    ('NU', _(u"Niue")),
    ('NZ', _(u"New Zealand")),
    ('OM', _(u"Oman")),
    ('PA', _(u"Panama")),
    ('PE', _(u"Peru")),
    ('PF', _(u"French Polynesia")),
    ('PG', _(u"Papua New Guinea")),
    ('PH', _(u"Philippines")),
    ('PK', _(u"Pakistan")),
    ('PL', _(u"Poland")),
    ('PM', _(u"Saint Pierre and Miquelon")),
    ('PN', _(u"Pitcairn")),
    ('PR', _(u"Puerto Rico")),
    ('PS', _(u"Palestinian Territory, Occupied")),
    ('PT', _(u"Portugal")),
    ('PW', _(u"Palau")),
    ('PY', _(u"Paraguay")),
    ('QA', _(u"Qatar")),
    ('RE', _(u"Réunion")),
    ('RO', _(u"Romania")),
    ('RS', _(u"Serbia")),
    ('RU', _(u"Russian Federation")),
    ('RW', _(u"Rwanda")),
    ('SA', _(u"Saudi Arabia")),
    ('SB', _(u"Solomon Islands")),
    ('SC', _(u"Seychelles")),
    ('SD', _(u"Sudan")),
    ('SE', _(u"Sweden")),
    ('SG', _(u"Singapore")),
    ('SH', _(u"Saint Helena")),
    ('SI', _(u"Slovenia")),
    ('SJ', _(u"Svalbard and Jan Mayen")),
    ('SK', _(u"Slovakia")),
    ('SL', _(u"Sierra Leone")),
    ('SM', _(u"San Marino")),
    ('SN', _(u"Senegal")),
    ('SO', _(u"Somalia")),
    ('SR', _(u"Suriname")),
    ('ST', _(u"Sao Tome and Principe")),
    ('SV', _(u"El Salvador")),
    ('SY', _(u"Syrian Arab Republic")),
    ('SZ', _(u"Swaziland")),
    ('TC', _(u"Turks and Caicos Islands")),
    ('TD', _(u"Chad")),
    ('TF', _(u"French Southern Territories")),
    ('TG', _(u"Togo")),
    ('TH', _(u"Thailand")),
    ('TJ', _(u"Tajikistan")),
    ('TK', _(u"Tokelau")),
    ('TL', _(u"Timor-Leste")),
    ('TM', _(u"Turkmenistan")),
    ('TN', _(u"Tunisia")),
    ('TO', _(u"Tonga")),
    ('TR', _(u"Turkey")),
    ('TT', _(u"Trinidad and Tobago")),
    ('TV', _(u"Tuvalu")),
    ('TW', _(u"Taiwan, Province of China")),
    ('TZ', _(u"Tanzania, United Republic of")),
    ('UA', _(u"Ukraine")),
    ('UG', _(u"Uganda")),
    ('UM', _(u"United States Minor Outlying Islands")),
    ('US', _(u"United States")),
    ('UY', _(u"Uruguay")),
    ('UZ', _(u"Uzbekistan")),
    ('VA', _(u"Holy See (Vatican City State)")),
    ('VC', _(u"Saint Vincent and the Grenadines")),
    ('VE', _(u"Venezuela, Bolivarian Republic of")),
    ('VG', _(u"Virgin Islands, British")),
    ('VI', _(u"Virgin Islands, U.S.")),
    ('VN', _(u"Viet Nam")),
    ('VU', _(u"Vanuatu")),
    ('WF', _(u"Wallis and Futuna")),
    ('WS', _(u"Samoa")),
    ('YE', _(u"Yemen")),
    ('YT', _(u"Mayotte")),
    ('ZA', _(u"South Africa")),
    ('ZM', _(u"Zambia")),
    ('ZW', _(u"Zimbabwe")),
)

employee_type = [
    ("Permanent", "Permanent"),
    ("Contract", "Contract")]

PROJECT_CATEGORY_CHOICES = [
    ("Development ", "Development "),
    ("Maintenance ", "Maintenance "),
    ("Enhancement  ", "Enhancement  ")]

PROJECT_STATUS_CHOICES = [
    ("completed ", "completed "),
    ("OnTrack ", "OnTrack "),
    ("Not Started  ", "Not Started  ")]


class CountryDoesNotExistException(Exception):
    pass


def get_country(iso_code, countries=COUNTRY_CHOICES):
    for country in countries:
        if country[0] == iso_code:
            return country
    raise CountryDoesNotExistException


class ProjectForm(forms.ModelForm):
    project_category = forms.CharField(label='What is your project type?',
                                       widget=forms.Select(choices=PROJECT_CATEGORY_CHOICES))
    project_status = forms.CharField(label='What is your project status?',
                                     widget=forms.Select(choices=PROJECT_STATUS_CHOICES))
    project_start_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    project_end_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = ProjectDetails
        fields = "__all__"

    def clean__project_id_data(self):
        pro_id = self.cleaned_data.get('project_id')
        project_available = Employee.objects.filter(project_id=pro_id).exists()
        if project_available:
            raise forms.ValidationError()
        return pro_id


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def clean_username_data(self):
        data = self.cleaned_data.get('username')
        print(data)
        available = Employee.objects.filter(username=data).exists()
        if available:
            raise forms.ValidationError()
        return data

    def clean(self):
        cleaned_data = super(UserRegistrationForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if len(password) < 8:
            self.add_error('password', "The password Must be 8 to 20 characters in length")
        else:
            if re.search('[a-z,A-Z]', password) is None:
                self.add_error('password', "Password should have atleast 1 letter")
            if re.search('[0-9]', password) is None:
                self.add_error('password', "Password should have atleast 1 digit")
            if re.search('[a-z]', password) is None:
                self.add_error('password', "Password should have atleast 1 Lowecase")
            if re.search('[A-Z]', password) is None:
                self.add_error('password', "Password should have atleast 1 Uppercase")
            if re.search('\W', password) is None:
                self.add_error('password', "Password should have atleast 1 Special Character")
        if password != confirm_password:
            self.add_error('confirm_password', "Password and Confirm Password does not match")
        return cleaned_data


class UserForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    fields = ['username', 'password']


class EmployeeForm(forms.ModelForm):
    emp_country = forms.CharField(label='What is your country?', widget=forms.Select(choices=COUNTRY_CHOICES))
    emp_address = forms.CharField(widget=forms.Textarea)
    emp_gender = forms.CharField(label='What is your gender?', widget=forms.Select(choices=GENDER_CHOICES))
    emp_marital_status = forms.CharField(label='What is your status?',
                                         widget=forms.Select(choices=MERITAL_STATUS_CHOICES))
    emp_designation = forms.CharField(label='What is your Designation?', widget=forms.Select(choices=emp_designation))
    emp_type = forms.CharField(label='What is your employment type?', widget=forms.Select(choices=employee_type))
    emp_notes = forms.CharField(widget=forms.Textarea)
    emp_dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    emp_hire_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Employee
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['emp_manager_id'].label_from_instance = self.business_label_manager
        self.fields['emp_project_id'].label_from_instance = self.business_label_project

    @staticmethod
    def business_label_manager(self):
        return str(self.emp_first_name)

    @staticmethod
    def business_label_project(self):
        return str(self.project_name)

    def clean_id_data(self):
        data = self.cleaned_data.get('emp_id')
        print(data)
        available = Employee.objects.filter(emp_id=data).exists()
        if available:
            raise forms.ValidationError()
        return data
