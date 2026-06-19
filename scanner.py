# Your functions
def read_file(filepath):
    with open(filepath, 'r') as f:
        return f.readlines()

def count_lines(lines):
    total = len(lines)
    blank = sum(1 for line in lines if line.strip() == "")
    code = sum(1 for line in lines if line.strip() != "" and not line.strip().startswith("#"))
    return {"total_lines": total, "blank_lines": blank, "code_lines": code}

# === CONNECT TO target_file.py ===
filepath = "target_file.py"

# Read and analyze
lines = read_file(filepath)
stats = count_lines(lines)

# Display results
print(f"📁 Analyzing: {filepath}")
print(f"📊 Total lines:  {stats['total_lines']}")
print(f"📄 Blank lines:  {stats['blank_lines']}")
print(f"💻 Code lines:   {stats['code_lines']}")
print(f"💬 Comments:     {stats['total_lines'] - stats['blank_lines'] - stats['code_lines']}")


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



import re


def read_file(filepath):
    with open(filepath, "r") as f:
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


def count_comments(lines):
    comment_count = 0
    in_docstring = False

    for line in lines:
        stripped = line.strip()

        if in_docstring:
            comment_count += 1
            if stripped.endswith('"""') or stripped.endswith("'''"):
                in_docstring = False
            continue

        if stripped.startswith('"""') or stripped.startswith("'''"):
            comment_count += 1
            # Check if it opens and closes on the same line.
            if not (stripped.count('"""') == 2 or stripped.count("'''") == 2):
                in_docstring = True
            continue

        if stripped.startswith("#"):
            comment_count += 1

    return comment_count


if __name__ == "__main__":
    filepath = "target_file.py"
    lines = read_file(filepath)

    print("Complexity counts:", check_complexity(lines))
<<<<<<< HEAD
    print("Number of comments:", count_comments(lines))
=======
    print("Number of comments:", count_comments(lines))
>>>>>>> 49cffca40108613a8c3c9da3f0bf35ddabc91a45
