def full_name(first_name, last_name, middle_name=""):
        "Returns the person's full name."
        if(middle_name):
            return '%s %s %s' % (first_name, middle_name, last_name)
        else:
            return '%s %s' % (first_name, last_name)