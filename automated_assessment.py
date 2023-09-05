from docx import Document

# Load the DOCX file
doc = Document("/mnt/data/coding_benchmark.docx")

# Extract the content of the DOCX file
content = [p.text for p in doc.paragraphs if p.text.strip() != ""]

content[:10]  # Display the first 10 lines of content for inspection
# Define a function to extract problems and assessment standards from the content

def extract_problems_and_standards(content):
    sections = {}
    current_section = None
    current_difficulty = None
    problems = []
    is_standard = False
    standard_text = ""

    for line in content:
        if "Problem " in line:
            problems.append(line.split(": ", 1)[1])
            is_standard = False
        elif "Easy" in line or "Medium" in line or "Hard" in line:
            current_difficulty = line
            is_standard = False
        elif any(section in line for section in ["Error/edge case handling", "Task planning", "Optimization", "General testing"]):
            if current_section:
                sections[current_section] = {"difficulty": current_difficulty, "problems": problems, "standard": standard_text}
                problems = []
                standard_text = ""
            current_section = line
            is_standard = False
        elif "Assessment Standard" in line:
            is_standard = True
        elif is_standard:
            standard_text += line + "\n"
    
    # Add the last section
    if current_section:
        sections[current_section] = {"difficulty": current_difficulty, "problems": problems, "standard": standard_text}
    
    return sections

sections = extract_problems_and_standards(content)
list(sections.keys())  # Display the section names for verification
def extract_optimization_problems_and_standards(content):
    optimization_problems = []
    current_problem = None
    is_standard = False
    standard_text = ""
    
    for line in content:
        if "Optimization Question:" in line:
            if current_problem:
                optimization_problems.append({"problem": current_problem, "standard": standard_text})
                standard_text = ""
            current_problem = line.split(": ", 1)[1]
            is_standard = False
        elif "Assessment:" in line:
            is_standard = True
        elif is_standard:
            standard_text += line + "\n"
    
    # Add the last problem
    if current_problem:
        optimization_problems.append({"problem": current_problem, "standard": standard_text})
    
    return optimization_problems

# Extract optimization problems
optimization_problems = extract_optimization_problems_and_standards(content)

# Remove the optimization questions that were mistakenly treated as separate sections
for key in list(sections.keys()):
    if "Optimization Question:" in key:
        del sections[key]

# Update the "Optimization" section with the extracted problems
#sections["Optimization"]["problems"] = [problem["problem"] for problem in optimization_problems]
#sections["Optimization"]["standards"] = [problem["standard"] for problem in optimization_problems]

#list(sections.keys())  # Display the corrected section names for verification
# Re-extract the problems and standards from the content
sections = extract_problems_and_standards(content)

# Extract optimization problems and standards
optimization_problems = extract_optimization_problems_and_standards(content)

# Update the "Optimization" section with the extracted problems and standards
if "Optimization" in sections:
    sections["Optimization"]["problems"] = [problem["problem"] for problem in optimization_problems]
    sections["Optimization"]["standards"] = [problem["standard"] for problem in optimization_problems]

list(sections.keys())  # Display the corrected section names for verification

def refined_extract_problems_and_standards(content):
    sections = {}
    current_section = None
    current_difficulty = None
    problems = []
    standards = []
    is_standard = False
    standard_text = ""

    for line in content:
        if "Problem " in line:
            problems.append(line.split(": ", 1)[1])
            is_standard = False
        elif "Optimization Question:" in line:
            problems.append(line.split(": ", 1)[1])
            is_standard = False
        elif "Assessment:" in line:
            is_standard = True
        elif any(section in line for section in ["Error/edge case handling", "Task planning", "Optimization", "General testing"]):
            if current_section:
                sections[current_section] = {
                    "difficulty": current_difficulty,
                    "problems": problems,
                    "standards": standards
                }
                problems = []
                standards = []
            current_section = line
            is_standard = False
        elif "Easy" in line or "Medium" in line or "Hard" in line:
            current_difficulty = line
        elif is_standard:
            standards.append(standard_text + line + "\n")
            standard_text = ""
        else:
            standard_text += line + "\n"
    
    # Add the last section
    if current_section:
        sections[current_section] = {
            "difficulty": current_difficulty,
            "problems": problems,
            "standards": standards
        }
    
    return sections

# Extract the problems and standards using the refined function
sections = refined_extract_problems_and_standards(content)
list(sections.keys())  # Display the section names for verification
# Generate solutions for a few problems from each section as a demonstration

def generate_solutions(problem_text):
    # For the purpose of this demo, we'll generate simple responses
    # In a real-world scenario, this function would be more elaborate
    if "eligible to vote" in problem_text:
        return """
def can_vote(age_input):
    try:
        age = int(age_input)
        if age >= 18:
            return "You are eligible to vote."
        else:
            return "You are not eligible to vote."
    except ValueError:
        return "Invalid input for age."
"""
    elif "number of lines in the file" in problem_text:
        return """
def count_lines(filename):
    try:
        with open(filename, 'r') as file:
            return len(file.readlines())
    except FileNotFoundError:
        return "File does not exist."
"""
    else:
        return "Solution for this problem is not provided in this demo."

# Sample solutions for a few problems
solutions = {}
for section, data in sections.items():
    for problem in data["problems"][:2]:  # Taking first 2 problems from each section for the demo
        solutions[problem] = generate_solutions(problem)

solutions


def assess_solution(solution, standard):
    feedback = []
    
    # Check if the solution uses certain keywords or methods based on the standard
    if "efficiency" in standard and "loop" in solution and "sum" not in solution:
        feedback.append("Solution might be inefficient due to usage of loops instead of built-in methods.")
    if "FileNotFoundError" in standard and "FileNotFoundError" in solution:
        feedback.append("Good job! Solution correctly handles the case where the file does not exist.")
    if "ValueError" in standard and "ValueError" in solution:
        feedback.append("Good job! Solution correctly handles invalid inputs.")
    
    # If no specific feedback is provided, give a generic response
    if not feedback:
        feedback.append("Solution looks okay based on the given standard. Further testing might be required.")
    
    return "\n".join(feedback)

# Assess the generated solutions
assessment_results = {}
for problem, solution in solutions.items():
    # Find the associated standard for the problem
    for section, data in sections.items():
        if problem in data["problems"]:
            idx = data["problems"].index(problem)
            if data["standards"] and len(data["standards"]) > idx:
                standard = data["standards"][idx]
                assessment_results[problem] = assess_solution(solution, standard)
                break

assessment_results
def grade_solution(solution, standard, difficulty):
    # Assign a raw grade based on the assessment feedback
    feedback = assess_solution(solution, standard)
    
    if "Good job!" in feedback:
        raw_grade = 100
    elif "Solution looks okay" in feedback:
        raw_grade = 80
    else:
        raw_grade = 50
    
    # Adjust the grade based on difficulty
    difficulty_multiplier = {
        "Easy-Beginner": 1,
        "Medium": 2,
        "Hard": 3
    }
    
    return raw_grade * difficulty_multiplier.get(difficulty, 1)

# Grade the solutions, ensuring we only grade sections that have problems
grades = {}
for section, data in sections.items():
    if data["problems"]:
        difficulty = data["difficulty"]
        problem = data["problems"][0]  # Taking the first problem as a representative for the section
        if problem in solutions:
            standard = data["standards"][0] if data["standards"] else ""
            grades[problem] = grade_solution(solutions[problem], standard, difficulty)

grades
