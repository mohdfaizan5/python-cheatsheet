# Example of a custom module to be imported

import re

def validate_email(email):
    if len(email) > 7:
        return bool(re.match("^.+@(\[?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", email))



if validate_email("mdfajzan.zprb2@gmail.com"):#mdfajzan.zprb2@gmail.com")
    print("Tr")
else:
    print("False")