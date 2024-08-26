import os
import chardet
from chardet.universaldetector import UniversalDetector

YELLOW = '\033[93m'
RED = '\033[91m'
RESET = '\033[0m'
BG_DARK_BLUE = '\033[44m'

try:
    while True:
        try:
            # ファイルパスの入力
            file_path = input(f"{YELLOW}File path?{RESET} ").strip('\'\"')

            file_size = os.path.getsize(file_path)

            if file_size < 500 * 1024:
                with open(file_path, 'rb') as f:
                    result = chardet.detect(f.read())
                method_used = "chardet.detect()"
            else:
                with open(file_path, 'rb') as f:
                    detector = UniversalDetector()
                    for line in f:
                        detector.feed(line)
                        if detector.done:
                            break
                    detector.close()
                    result = detector.result
                method_used = "UniversalDetector()"

            # エンコーディング検出結果のチェック
            encoding = result.get('encoding')
            if encoding is None:
                encoding = f"{BG_DARK_BLUE}{RED}None{RESET}{BG_DARK_BLUE}"
            confidence = result.get('confidence')
            language = result['language'] if result['language'] else 'N/A'

            formatted_result = (
                f"{{Encoding: {encoding}, "
                f"Confidence: {confidence}, "
                f"Language: {language}}}"
            )

            print("\n" + BG_DARK_BLUE + f"Using {method_used} for file size: {file_size} bytes" + RESET)
            print(BG_DARK_BLUE + formatted_result + RESET)
            break  # 正しく処理できたらループを抜ける

        except Exception as e:
            print(f"{RED}Error: Invalid file path or access issue. Please try again.{RESET}")

except KeyboardInterrupt:
    print(f"\n{RED}Process interrupted by user. Exiting...{RESET}")
