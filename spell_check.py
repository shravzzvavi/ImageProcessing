from sys import argv
 
from enchant import request_dict
 
if len(argv) <= 1:
    print "USAGE: python basic_testing.py <sentence>"
    exit()
else:
    sentence = argv[1:]
 
gb_dict = request_dict('en_gb')
us_dict = request_dict('en_us')
 
for word in sentence:
    if gb_dict.check(word) or us_dict.check(word):
        print word, " "
    else:
        print  " %s " % \
            (gb_dict.suggest(word)[0])
        # print word, "| %s first GB suggestion | %s  first US suggestion" % \
         #   (gb_dict.suggest(word)[1], us_dict.suggest(word)[1])

