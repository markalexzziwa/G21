import sys
import os
import re
import json

# Read Function
def read_file(filepath):
    with open(filepath, 'r') as f:
        return f.readlines()

def count_lines(lines):
    total = len(lines)
    blank = sum(1 for line in lines if line.strip() == "")
    code = sum(1 for line in lines if line.strip() != "" and not line.strip().startswith("#"))
    return {"total_lines": total, "blank_lines": blank, "code_lines": code}

#complexity check
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

class VariableValidator:
    @staticmethod
    def check_variables(raw_lines):
        """Finds items assigned with = and ensures they use snake_case formatting."""
        warnings = []
        snake_case_pattern = r"^[a-z0-9_]+$"
        
        for line_num, line in enumerate(raw_lines, 1):
            if "=" in line and "==" not in line and "!=" not in line and "<=" not in line and ">=" not in line:
                left_side = line.split("=")[0].strip()
                
                # Extract words/variables to the left of the assignment operator
                vars_found = re.findall(r"\b[a-zA-Z0-9_]+\b", left_side)
                
                for var in vars_found:
                    # Filter out purely numeric entries or core structural words
                    if var.isdigit() or var in ["self", "if", "for", "while", "return"]:
                        continue
                        
                    # Check snake_case compliance rule
                    if not re.match(snake_case_pattern, var):
                        warnings.append(f"Line {line_num}: Variable '{var}' is not snake_case.")
                        
        return warnings


if __name__ == "__main__":

    if len(sys.argv) >= 2:
        filepath = sys.argv[1]
    else:
        filepath = "target_file.py"

    lines = read_file(filepath)
    stats = count_lines(lines)

    # 2. Display initial analysis log layout
    print(f"Analyzing: {filepath}")
    print(f"Total lines:  {stats['total_lines']}")
    print(f"Blank lines:  {stats['blank_lines']}")
    print(f"Code lines:   {stats['code_lines']}")
    print(f"Comments:     {stats['total_lines'] - stats['blank_lines'] - stats['code_lines']}\n")

    complexity_counts = check_complexity(lines)
    total_comments = count_comments(lines)
    naming_warnings = VariableValidator.check_variables(lines)

    comment_ratio = round((total_comments / stats['total_lines']) * 100, 2) if stats['total_lines'] > 0 else 0.0
    
    score = 100 - (len(naming_warnings) * 2)
    if sum(complexity_counts.values()) > 15:
        score -= 10
    health_score = max(0, min(score, 100))

    output_dictionary = {
        "total_lines": stats['total_lines'],
        "blank_lines": stats['blank_lines'],
        "lines_of_code": stats['code_lines'],
        "comment_lines": total_comments,
        "comment_ratio_pct": comment_ratio,
        "complexity": complexity_counts,
        "naming_warnings": naming_warnings,
        "health_score": health_score
    }

    print(json.dumps(output_dictionary, indent=4))
