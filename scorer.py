def calculate_score(data):

    score = 0

    # -----------------------------------
    # UNIQUE SKILLS
    # -----------------------------------

    score += data["skills_count"] * 6

    # -----------------------------------
    # PROJECT QUALITY
    # -----------------------------------

    score += min(data["projects"] * 5, 25)

    # -----------------------------------
    # CERTIFICATIONS
    # -----------------------------------

    score += min(data["certifications"] * 4, 15)

    # -----------------------------------
    # EDUCATION
    # -----------------------------------

    score += data["education_score"]

    # -----------------------------------
    # RESUME LENGTH
    # -----------------------------------

    if data["length"] >= 500:
        score += 10

    elif data["length"] >= 300:
        score += 5

    else:
        score -= 10

    # -----------------------------------
    # GRAMMAR PENALTY
    # -----------------------------------

    score -= data["grammar_errors"] * 2

    # -----------------------------------
    # KEYWORD STUFFING PENALTY
    # -----------------------------------

    score -= data["stuffing_penalty"]

    # -----------------------------------
    # FINAL LIMIT
    # -----------------------------------

    if score > 100:
        score = 100

    if score < 0:
        score = 0

    return score