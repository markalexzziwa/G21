#Complexity Checker



import re

def read_file(filepath):

    with open(filepath, 'r') as f:

        return f.readlines()



def check_complexity(lines):

    keywords = ["if", "elif", "else", "for", "while", "print", "match", "case"]

    counts = {k: 0 for k in keywords}

    for line in lines:

        stripped = line.strip()

        if stripped.startswith("#"):

            continue

        for kw in keywords:

            if re.search(rf"\b{kw}\b", stripped):

                counts[kw] += 1

    return counts

# --- Run it ---

if __name__ == "__main__":

    filepath = "target_file.py"   # replace with the actual file judges give you

    lines = read_file(filepath)

    result = check_complexity(lines)

    print(result)