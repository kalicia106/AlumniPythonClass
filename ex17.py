from sys import argv

script, summer.txt, winter.txt = argv

print("f Copying from {summer.txt} to {winter.txt}")

#we could do these two on one line, how?
in_file = open(summer.txt)
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists (winter)}")
print("Ready, hit RETURN to continue, CTRL -C to abort.")
input()

out_file = open(winter.txt, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()
