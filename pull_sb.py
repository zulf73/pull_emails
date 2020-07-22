
import re
f = open('sbphysics.html')
for line in f:
	m = re.findall( r'(.+)<img src=\"web/at.gif\" width=20 height=17>(.+)\.', line, re.MULTILINE)
	for g in m:
		print g[0]+'@'+g[1]





