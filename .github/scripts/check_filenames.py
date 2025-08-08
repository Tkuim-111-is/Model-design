import os
import sys
import unicodedata

def is_ascii(s):
    try:
        s.encode('ascii')
        return True
    except UnicodeEncodeError:
        return False

def main():
    failed = False
    for root, dirs, files in os.walk("."):
        for name in dirs + files:
            path = os.path.join(root, name)
            if not is_ascii(name):
                print(f"❌ Non-ASCII name found: {path}")
                failed = True
    if failed:
        print("🚫 Merge rejected: Please use ASCII-only (English) characters for all file/folder names.")
        sys.exit(1)
    else:
        print("✅ All filenames are ASCII-only.")

if __name__ == "__main__":
    main()
