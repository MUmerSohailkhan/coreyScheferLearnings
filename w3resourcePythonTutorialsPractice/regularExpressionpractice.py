import re



theString1="Original men's T-shirts with barcode scan s.m.l.xl.xxl sizes available made in Bangladesh per peice price 1200 PKR"


lst=re.findall('Original',theString1)

re.search("^Original.PKR$")




seqOfCharacter="^[a-zA-Z0-9]{1}@[a-zA-Z]{1}.{1}com$"

print(lst)