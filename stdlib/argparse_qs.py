import argparse

#python argparse_qs.py posstrval --optstr optstrval -n1 n1val --reqstr regstrval --destspecified 1 --storetrue --storefalse --constant --port 8080 --pi 3.14157 --loglevel DEBUG --twovals 2 3 --zerotomanyvals 4 5 6 --onetomanyvals 7 --zerooroneval --metavarex 7
#python argparse_qs.py posstrval --optstr optstrval -name1 n1val --reqstr regstrval --destspecified 1 --storetrue --port 8080 --pi 3.14157 --twovals 2 3 --zerotomanyvals 4 --onetomanyvals 7 8 --metavarex 7


parser = argparse.ArgumentParser(description='argparse module demo', formatter_class=argparse.ArgumentDefaultsHelpFormatter)


#required=False, action=store and type=str are defaults
#optional arguments begin with '-'
parser.add_argument("--optstr", default="foo", help="optional string")

#positional arguments do not begin with '-'
parser.add_argument("posstr")

#multiple option strings
parser.add_argument("-name1", "-n1")

#required with help text
parser.add_argument("--reqstr", required=True, help="help text for --reqstr")

#destination specified
parser.add_argument("--destspecified", dest="ds")

#boolean with default values
parser.add_argument("--storetrue", action="store_true", default=False)
parser.add_argument("--storefalse", action="store_false", default=True)

#constant
parser.add_argument("--constant", action="store_const", const="store this value")

#int
parser.add_argument("--port", type=int)

#float
parser.add_argument("--pi", type=float)

#choices
parser.add_argument("--loglevel", choices=["TRACE", "DEBUG", "WARN", "INFO", "ERROR"], default="INFO")

#specify number of values for argument and store as list
parser.add_argument("--twovals", nargs=2)
parser.add_argument("--zerotomanyvals", nargs='*')
parser.add_argument("--onetomanyvals", nargs='+')

#zero or one value and produced as a single item
# --zerooroneval abc   --> "abc"
# --zerooroneval  --> "a const"
# --zerooroneval not in argument list --> "the default"
parser.add_argument("--zerooroneval", nargs='?', default="the default", const="a const")

#specify argument name in usage message instead of dest
parser.add_argument("--metavarex", metavar="different")

#print version info
parser.add_argument("--version", action="version", version="%(prog)s 2.0")


args = parser.parse_args()


print "args.optstr:", args.optstr
print "args.posstr:", args.posstr
print "args.name1:", args.name1
print "args.reqstr:", args.reqstr
print "args.ds:", args.ds
print "args.storetrue:", args.storetrue
print "args.storefalse:", args.storefalse
print "args.constant:", args.constant
print "args.port:", args.port, type(args.port)
print "args.pi:", args.pi, type(args.pi)
print "args.loglevel:", args.loglevel
print "args.twovals:", args.twovals
print "args.zerotomanyvals:", args.zerotomanyvals
print "args.onetomanyvals:", args.onetomanyvals
print "args.zerooroneval:", args.zerooroneval
