import re

with open ("GeekBrains - образовательный портал.html","r") as f:
    text=f.read()

peoples = re.findall("total-users\">(Нас уже .*?)</span>",text)

print(peoples)