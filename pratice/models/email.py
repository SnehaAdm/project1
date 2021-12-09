from odoo import models, fields, api

import re

def  ValidateEmail(email):

    if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) != None:
        return True
    else:
        raise osv.except_osv('Invalid Email', 'Please enter a valid email address')
if __name__ == '__main__' : 
    email=fields.Char(srting="Email", required=True)

