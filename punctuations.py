import re
file = ';Hello?World!'

#change = ':'
file = re.sub('[ ;%!$?%*:]',' ',file)
print(file)