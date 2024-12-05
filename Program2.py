def write_and_read_file(filename, content):
    with open(filename, "w") as file:
        file.write(content)
        
    with open(filename, "r") as file:
        return file.read()

filename = "example.txt"
content = input("Введите текст: ")

print(write_and_read_file(filename, content))