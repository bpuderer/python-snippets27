import json

py_obj = {'_id':0, 'things':[{'a_bool':True, 'a_float': 3.14, 'none_val': None}], 'a_tuple': (1, 2)}
json_str = json.dumps(py_obj)
print "python object:", py_obj
print "converted to json:", json_str
print "with keys sorted:", json.dumps(py_obj, sort_keys=True)
print "converted back to python:", json.loads(json_str)
