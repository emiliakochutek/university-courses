import os
import sys

def find_files(directory, target):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file == target:
                print(os.path.join(root, file))

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python find.py <directory> <target>")
        sys.exit(1)

    directory = sys.argv[1]
    target = sys.argv[2]

    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory.")
        sys.exit(1)

    find_files(directory, target)
