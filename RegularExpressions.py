import re

str = "Furkan Akyel İnönü elma elalma elelma ellema deneme deme 22.07.2003"

result = re.findall("el..ma",str)

print(result)