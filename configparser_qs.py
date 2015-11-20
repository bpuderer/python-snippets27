"""demo of basic read capabilities of ConfigParser"""

import ConfigParser


config = ConfigParser.SafeConfigParser(allow_no_value=True)
config.read('settings.cfg')

print "\ndefaults:", config.defaults()

#DEFAULTS not included (if present)
print "\nsections:", config.sections()

print "\nis there a section named Section 2?", config.has_section('Section 2')

#options in DEFAULTS (if present) are included
print "\noptions for Section 1:", config.options('Section 1')

#items in DEFAULTS (if present) are included
print "\nitems for Section 1:", config.items('Section 1')

print "\nvalue of name1 in Section1:", config.get('Section 1', 'name1')
#get always returns a string
print "type using get:", type(config.get('Section 1', 'name1'))

print "\nvalue of name7 as a float:", config.getfloat('Section 1', 'name7')
print "type using getfloat:", type(config.getfloat('Section 1', 'name7'))

# 1,yes,true,on -> True    0,no,false,off -> False    case-insensitive
print "\nvalue of name8 as a Boolean:", config.getboolean('Section 1', 'name8')
print "type using getboolean:", type(config.getboolean('Section 1', 'name8'))

print "\nvalue of name11 as an int:", config.getint('Section 1', 'name11')
print "type using getint:", type(config.getint('Section 1', 'name11'))

print "\nis name99 in Section1?", config.has_option('Section 1', 'name99')

