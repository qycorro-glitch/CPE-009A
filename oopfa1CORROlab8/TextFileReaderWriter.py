from FileReaderWriter import FileReaderWriter

class TextFileReaderWriter(FileReaderWriter):

    def read(self, filepath):
        with open(filepath, "r") as file:
            data = file.read()
            print(data)
        return data

    def write(self, filepath, data):
        with open(filepath, "w") as file:
            file.write(data)
            
 
    print("\n--- TEXT FILE TEST ---")
t = TextFileReaderWriter()

# read file
t.read("sample.txt")

# write (this will overwrite file)
t.write("sample2.txt", "This is overwritten text file content.")