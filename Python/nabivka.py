import os
files = []
content_files = []
for x in os.listdir():
    if x.endswith(".txt") and x !="Результат.txt" and x !="res.txt":
        file = open(x, "r")
        content = file.read()
        file.close()
        files.append(x)
        content_files.append(content)

print(files)
print(content_files)

my_file = open("Результат.txt", "w+")
for i in range(len(files)):
    my_file.write(files[i] + "       " + content_files[i] + "\n")
my_file.close()