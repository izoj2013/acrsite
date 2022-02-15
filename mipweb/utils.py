from datetime import datetime
from logging import raiseExceptions
from dateutil.relativedelta import relativedelta
from django import forms


def full_name(first_name, last_name, middle_name=""):
        "Returns the person's full name."
        if(middle_name):
            return '%s %s %s' % (first_name, middle_name, last_name)
        else:
            return '%s %s' % (first_name, last_name)

def get_date():
    return datetime.now().strftime("%d-%m-%Y")

def add_time(duration_add: int):
    future_date = datetime.now() + relativedelta(months=+duration_add)
    return future_date

def get_cleaned_attribute(form, attrName):
    cleaned_variable = form.cleaned_data.get(attrName)
    return cleaned_variable

def is_valid_string(str_2_validate):
    if len(str_2_validate) == 0:
        raise forms.ValidationError(str_2_validate + " " + "must not be blank")
    return True

def is_valid_email(email_addr: str):
    if is_valid_string(email_addr):
        with open("acrsite/disposable_email_providers.txt", 'r') as f:
                blacklist = f.read().splitlines()

        for disposable_email in blacklist:
            if disposable_email in email_addr:
                raise forms.ValidationError("Your email address %s may not be legit" %disposable_email)

    return True