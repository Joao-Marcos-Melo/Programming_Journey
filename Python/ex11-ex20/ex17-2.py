from sys import argv

script, from_file, to_file = argv

print("Copying from %s to %s" % (from_file, to_file))

# we could do these two on one line too, how?
open(to_file, 'w').write(open(from_file).read())

print("Alright, all done.")

