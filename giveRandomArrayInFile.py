import difflib
import random
import glob
import os

text_files = glob.glob("*.txt")


def getRandomLinesOfFile(file_path, amount=1):
    all_lines = open(file_path).read().splitlines()
    random_file_lines = []
    for i in range(amount):
        random_file_line = random.choice(all_lines)
        while random_file_line in random_file_lines:
            random_file_line = random.choice(all_lines)
        random_file_lines.append(random_file_line)
    return random_file_lines


while True:
    print(" ")
    print(" ")
    print("Existing Files: ")
    for file in text_files:
        print(file)
    print(" ")
    print("_____________________________________________________________")

    print(" ")
    file_name = input("Which file do you want to load? (closest match) : ")
    return_amount = int(input("How many values do you want to get back? : "))

    if file_name not in text_files:
        file_name = difflib.get_close_matches(file_name, text_files, n=1, cutoff=0)[0]

    print("_____________________________________________________________")
    print(" ")
    print(" ")
    random_lines = ""
    for random_line in getRandomLinesOfFile(file_name, return_amount):
        random_lines += random_line + " "
    os.system('echo ' + random_lines + '| clip')
    print("File: " + file_name)
    print("Result: " + random_lines)
    print("[Result was loaded into the clipboard]")
    print(" ")
    print(" ")
    print("#############################################################")
    print("#############################################################")
