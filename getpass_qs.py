import getpass

# prompt user without echoing output

print getpass.getpass()

print getpass.getpass(prompt="Custom Prompt:")

print "user login name:", getpass.getuser()
