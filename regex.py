##import re
##line = "123 hi 34 hello."
##m = re.findall("\d", line, re.IGNORECASE)
##print(m)

import re
l = "The ghost that says boo haunts the loo"
m = re.findall(".oo",l)
print(m)    
    
