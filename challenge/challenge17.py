import re

# text = "The ghost that says boo haunts the loo"
text = "Arizona 479,  501, 870. California 209, 213, 650."

m = re.findall("\d", text, flags=re.ASCII)
print(m)