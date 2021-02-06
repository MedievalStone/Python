import re 

pattern = re.compile(r"(^[A-Za-z$#%@])")

string = 'asdsada@13124%#'
a=pattern.search(string)
print(a);