from sys import argv

script, bubble, bath = argv

file_to_read = open(bubble, 'r')

content = file_to_read.read()

print(content)

write_file = open(bath, 'w')

write_file.write(content)

file_to_read.close()

write_file.close()
