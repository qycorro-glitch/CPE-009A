from FileReaderWriter import FileReaderWriter
from CSVFileReaderWriter import CSVFileReaderWriter
from JSONFileReaderWriter import JSONFileReaderWriter

# Test default class
df = FileReaderWriter()
df.read()
df.write()

print("\n--- CSV TEST ---")
c = CSVFileReaderWriter()
c.read("sample.csv")
c.write(filepath="sample2.csv", data=["Hello", "World"])

print("\n--- JSON TEST ---")
j = JSONFileReaderWriter()
j.read("sample.json")
j.write(filepath="sample2.json", data={"foo": {"bar": ["baz", None, 1.0, 2]}})

