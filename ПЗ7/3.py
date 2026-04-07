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

def check_duplicate_file(file_path, directory):
    with open(file_path, 'rb') as f:
        file_content = f.read()
        file_hash = hashlib.md5(file_content).hexdigest()

    duplicates = group_duplicate_files(directory)

    return file_hash in duplicates

print(check_duplicate_file("C:\\Users\\nrbud\\Desktop\\AlgorithmsAndProg\\ПЗ7\\Директория_1\\ПЗ №9.docx", "C:\\Users\\nrbud\\Desktop\\AlgorithmsAndProg\\ПЗ7\\Директория_1"))