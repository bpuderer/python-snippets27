import json

py_obj = {'_id': 0, 'things': [{'a_bool': True, 'a_float': 3.14, 'none_val': None}], 'a_tuple': (1, 2), 'a_string': 'some string val'}
json_str = json.dumps(py_obj)

print "python object:", py_obj
print "\nconverted to json:", json_str
print "\nwith keys sorted and minimal spacing:", json.dumps(py_obj, separators=(',', ':'), sort_keys=True)
print "\npretty printed:\n", json.dumps(py_obj, indent=4, separators=(',', ': '), sort_keys=True)
print "\nconverted back to python (notice tuple):", json.loads(json_str)
