from sys import argv
from os.path import exists   # aquele ele diz "do caminho do sistema operacional importe a ferramenta de checagem de existencia"

script, from_file, to_file = argv

print("Copying from %s to %s" % (from_file, to_file))

# we could do these two on one line too, how?

in_file = open(from_file)
indata = in_file.read()

print("The input file is %d bytes long" % len(indata))   # funcao length / comprimento

print("Does the output file exist? %r" % exists(to_file))  # a função exists vai nos dizer se o arquivo existe ou nao 
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w') 
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()
