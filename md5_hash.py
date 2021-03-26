import hashlib


def my_generator(file_name):
    with open(file_name, "r") as f:
        lines = f.readlines()
        for line in lines:
            yield hashlib.md5(line.encode()).hexdigest()


for i in my_generator("country_names.txt"):
    print(i)
