import datetime
import json
import pprint

import yaml


def serializer(o):
    if isinstance(o, datetime.datetime):
        return o.isoformat()
    elif isinstance(o, datetime.date):
        return str(o)
    else:
        raise TypeError("Unknown type")


#http://yaml.org/spec/1.1/#id857168
parsed_yaml = yaml.load("""
invoice: 100
date   : 2015-12-29T08:09:10.011Z
bill-to: &id001
    name   : Billing Name
    address:
        lines: |
            123 Main Street
            Suite #100
        city    : Anytown
        state   : LA
        postal  : 70056
ship-to: *id001
items  :
    - model-no    : CX2600
      quantity    : 1
      description : Atari VCS
      unit-price  : 199.00
      price       : 199.00
    - model-no    : CX30
      quantity    : 2
      description : Paddle Controllers
      unit-price  : 25.00
      price       : 50.00
    - model-no    : CX2610
      quantity    : 1
      description : Warlords
      unit-price  : 19.95
      price       : 19.95
    - model-no    : CX2638
      quantity    : 1
      description : Missile Command
      unit-price  : 29.95
      price       : 29.95
subtotal      : 298.90
tax           : 20.92
shipping      : 19.95
rewards-member: false
total         : 339.77
email         : ~
comments      : >
    Thank you for your order!
    Be sure to stop by The Video Store on Terry Pkwy!
""")

pprint.pprint(parsed_yaml)

print("********")

# print json.dumps(parsed_yaml, indent=4, separators=(',', ': '), sort_keys=True)
# print json.dumps(parsed_yaml, indent=4, separators=(',', ': '), sort_keys=True, default=str)
print(json.dumps(parsed_yaml, indent=4, separators=(',', ': '), sort_keys=True, default=serializer))

print("********")

print yaml.dump(parsed_yaml)
