import os
import chardet
from chardet.universaldetector import UniversalDetector

def detect_encoding(file_path):
    file_size = os.path.getsize(file_path)
    threshold_size = 500 * 1024  # 500KBを閾値とする

    if file_size <= threshold_size:
        print(f"Using chardet.detect() for file size: {file_size} bytes")
        with open(file_path, 'rb') as f:
            c = f.read()
            result = chardet.detect(c)
    else:
        print(f"Using UniversalDetector for file size: {file_size} bytes")
        with open(file_path, 'rb') as f:
            detector = UniversalDetector()
            for line in f:
                detector.feed(line)
                if detector.done:
                    break
            detector.close()
            result = detector.result

    return result

file_path = r"YOUR_FILE_PATH"
encoding_info = detect_encoding(file_path)
print(encoding_info)
