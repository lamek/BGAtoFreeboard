import urllib2
import re


f = open('ReplayCodeRaw.txt', 'r')
myfile = f.read()
##response = urllib2.urlopen('http://en.boardgamearena.com/archive/replay/151214-1316/?table=17964997&player=84035275&comments=')
##html = response.read()

##print html


pattern = '"quoridorstrats_notation":"([a-z][0-9])"'
 
list_of_moves = re.findall(pattern, myfile)

print list_of_moves
