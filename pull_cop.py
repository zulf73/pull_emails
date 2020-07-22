
import re
f = open('mail.copenhagen.txt')
for line in f:
	m = re.findall( r'\'lto:\' \+ \'(.+?)\' \+ \'@\' \+ \'(.+?)\' ;', line, re.MULTILINE)
	for g in m:
		print g[0] + '@' + g[1]




