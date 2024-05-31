import chardet

file_path = "SAMPLE.csv"
with open(file_path, 'rb') as f:
  c = f.read()
  result = chardet.detect(c)
