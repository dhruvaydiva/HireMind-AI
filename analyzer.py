import re

# -----------------------------------
# SKILLS DATABASE
# -----------------------------------

technical_skills = {

    "python",
    "java",
    "c",
    "c++",
    "sql",
    "html",
    "css",
    "javascript",
    "react",
    "nodejs",
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "data science",
    "tensorflow",
    "opencv",
    "mongodb",
    "mysql",
    "flask",
    "django",
    "aws",
    "git",
    "github",
    "nlp",
    "computer vision"
}

# -----------------------------------
# ANALYZE RESUME
# -----------------------------------

def analyze_resume(text):

    result = {}

    text_lower = text.lower()

    # -----------------------------------
    # UNIQUE SKILLS DETECTION
    # -----------------------------------

    found_skills = set()

    for skill in technical_skills:

        if skill in text_lower:
            found_skills.add(skill)

    result["skills"] = list(found_skills)

    result["skills_count"] = len(found_skills)

    # -----------------------------------
    # PROJECT QUALITY
    # -----------------------------------

    strong_project_words = [

        "developed",
        "implemented",
        "built",
        "created",
        "designed",
        "deployed",
        "trained",
        "integrated"
    ]

    project_score = 0

    for word in strong_project_words:

        project_score += text_lower.count(word)

    result["projects"] = project_score

    # -----------------------------------
    # CERTIFICATIONS
    # -----------------------------------

    cert_score = 0

    cert_words = [

        "certification",
        "certificate",
        "certified"
    ]

    for word in cert_words:

        cert_score += text_lower.count(word)

    result["certifications"] = cert_score

    # -----------------------------------
    # EDUCATION
    # -----------------------------------

    education_score = 0

    if "artificial intelligence" in text_lower:
        education_score += 10

    if "machine learning" in text_lower:
        education_score += 10

    if "computer science" in text_lower:
        education_score += 10

    # -----------------------------------
    # CGPA EXTRACTION
    # -----------------------------------

    cgpa = 0

    cgpa_match = re.search(
        r'cgpa[^0-9]*([0-9]\.?[0-9]*)',
        text_lower
    )

    if cgpa_match:

        cgpa = float(cgpa_match.group(1))

        if cgpa >= 8.5:
            education_score += 25

        elif cgpa >= 7:
            education_score += 15

        elif cgpa >= 6:
            education_score += 5

    result["education_score"] = education_score

    # -----------------------------------
    # RESUME LENGTH
    # -----------------------------------

    word_count = len(text.split())

    result["length"] = word_count

    # -----------------------------------
    # KEYWORD STUFFING DETECTION
    # -----------------------------------

    stuffing_penalty = 0

    words = text_lower.split()

    for word in set(words):

        if words.count(word) > 15:
            stuffing_penalty += 10

    result["stuffing_penalty"] = stuffing_penalty

    # -----------------------------------
    # GRAMMAR ESTIMATION
    # -----------------------------------

    grammar_errors = 0

    sentences = text.split(".")

    for sentence in sentences:

        if len(sentence.split()) < 2:
            grammar_errors += 1

    result["grammar_errors"] = grammar_errors

    return result