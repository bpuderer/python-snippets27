import base64


orig_str = "here is a test string"
encoded = base64.b64encode(orig_str)
decoded = base64.b64decode(encoded)

print "Original:", orig_str
print "Encoded: ", encoded
print "Decoded: ", decoded
