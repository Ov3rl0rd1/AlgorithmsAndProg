import os
import hashlib

def group_duplicate_files(directory):
    file_hashes = {}
    duplicates = {}

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'rb') as f:
                file_content = f.read()
                file_hash = hashlib.md5(file_content).hexdigest()

                if file_hash in file_hashes:
                    if file_hash not in duplicates:
                        duplicates[file_hash] = [file_hashes[file_hash]]
                    duplicates[file_hash].append(file_path)
                else:
                    file_hashes[file_hash] = file_path

    return duplicates

print(group_duplicate_files("C:\\Users\\nrbud\\Desktop\\AlgorithmsAndProg\\7\\Директория_1"))