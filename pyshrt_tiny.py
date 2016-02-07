#!/usr/bin/python

# Licence

#           DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE 
#                  Version 2, December 2004 

# Everyone is permitted to copy and distribute verbatim or modified 
# copies of this license document, and changing it is allowed as long 
# as the name is changed. 
#
#           DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE 
# TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION 

#  0. You just DO WHAT THE FUCK YOU WANT TO.

import contextlib
import sys

try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

def main():
    for pendekin in map(pendek, sys.argv[1:]):
	print"URL Pendek = ",(pendekin)

def pendek(url):
    short_engine = ('http://tinyurl.com/api-create.php?' + 
    urlencode({'url':url}))
    with contextlib.closing(urlopen(short_engine)) as response:
        return response.read().decode('utf-8')

if __name__ == '__main__':
	main()