import chardet

def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
    return result['encoding']

def search_bots(file_path):
    encoding = detect_encoding(file_path)
    with open(file_path, encoding=encoding) as csvfile:
        reader = csv.reader(csvfile)
        rows = [row for row in reader]
    return rows
