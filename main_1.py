import chardet

filepath = "SAMPLE.csv"
with open(filepath, 'rb') as f:
  c = f.read()
  result = chardet.detect(c)
