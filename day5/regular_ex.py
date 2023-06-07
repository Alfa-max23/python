"""
Regular expression for extracting email ids

"""

import re

text = """
This alert service notifies r.269.kaushal@gmail.com and roopalkaushal09@web.com 
and anikiet31121993@yahoo.com

"""

#print(dir(re))
#print(re.findall.__doc__)

list_of_emails = re.findall("[a-z0-9\.\-+_]+@+[a-z0-9\.\-+_]+\.[a-z]+",text)
print(list_of_emails)

