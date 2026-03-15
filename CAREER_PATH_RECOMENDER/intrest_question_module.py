def ask_questions():
    
    career_scores = {
        "Software Developer": 0,
        "AI Engineer": 0,
        "Data Scientist": 0,
        "Web Developer": 0,
        "Cyber Security Analyst": 0,
        "Graphic Designer": 0,
        "Digital Marketer": 0,
        "Teacher": 0,
        "Actor": 0,
        "Entrepreneur": 0
    }

    
    q1 = input("1. Do you enjoy coding or programming? (yes/no): ").lower()
    if q1 == "yes":
        career_scores["Software Developer"] += 3
        career_scores["AI Engineer"] += 2

    q2 = input("2. Do you enjoy working with numbers or data? (yes/no): ").lower()
    if q2 == "yes":
        career_scores["Data Scientist"] += 3

    q3 = input("3. Are you interested in Artificial Intelligence? (yes/no): ").lower()
    if q3 == "yes":
        career_scores["AI Engineer"] += 3

    q4 = input("4. Do you enjoy designing websites? (yes/no): ").lower()
    if q4 == "yes":
        career_scores["Web Developer"] += 3

    q5 = input("5. Do you like solving logical problems? (yes/no): ").lower()
    if q5 == "yes":
        career_scores["Software Developer"] += 2
        career_scores["Data Scientist"] += 1

    q6 = input("6. Are you interested in computer security or ethical hacking? (yes/no): ").lower()
    if q6 == "yes":
        career_scores["Cyber Security Analyst"] += 3

    q7 = input("7. Do you enjoy creative designing or drawing? (yes/no): ").lower()
    if q7 == "yes":
        career_scores["Graphic Designer"] += 3

    q8 = input("8. Do you enjoy using social media platforms? (yes/no): ").lower()
    if q8 == "yes":
        career_scores["Digital Marketer"] += 2

    q9 = input("9. Do you like explaining concepts to others? (yes/no): ").lower()
    if q9 == "yes":
        career_scores["Teacher"] += 3

    q10 = input("10. Do you enjoy performing in front of people? (yes/no): ").lower()
    if q10 == "yes":
        career_scores["Actor"] += 3

    q11 = input("11. Do you enjoy creating videos or content? (yes/no): ").lower()
    if q11 == "yes":
        career_scores["Digital Marketer"] += 2
        career_scores["Actor"] += 1

    q12 = input("12. Do you enjoy solving mathematical problems? (yes/no): ").lower()
    if q12 == "yes":
        career_scores["Data Scientist"] += 2
        career_scores["AI Engineer"] += 2

    q13 = input("13. Do you like working on computers for long hours? (yes/no): ").lower()
    if q13 == "yes":
        career_scores["Software Developer"] += 1
        career_scores["Web Developer"] += 1

    q14 = input("14. Are you interested in business or startups? (yes/no): ").lower()
    if q14 == "yes":
        career_scores["Entrepreneur"] += 3

    q15 = input("15. Do you enjoy solving real-world problems? (yes/no): ").lower()
    if q15 == "yes":
        career_scores["Entrepreneur"] += 2
        career_scores["Software Developer"] += 1

    q16 = input("16. Do you enjoy learning new technologies? (yes/no): ").lower()
    if q16 == "yes":
        career_scores["AI Engineer"] += 1
        career_scores["Software Developer"] += 1

    q17 = input("17. Do you enjoy photography or visual creativity? (yes/no): ").lower()
    if q17 == "yes":
        career_scores["Graphic Designer"] += 2

    q18 = input("18. Do you enjoy analysing trends and patterns? (yes/no): ").lower()
    if q18 == "yes":
        career_scores["Data Scientist"] += 2

    q19 = input("19. Do you enjoy interacting with many people? (yes/no): ").lower()
    if q19 == "yes":
        career_scores["Teacher"] += 1
        career_scores["Digital Marketer"] += 1
        career_scores["Actor"] += 1

    q20 = input("20. Do you like creating something new or innovative? (yes/no): ").lower()
    if q20 == "yes":
        career_scores["Entrepreneur"] += 2

    # 3. CRITICAL: Return the scores so main.py can use them
    return career_scores