def recommend_career(career_scores):

   
    sorted_careers = sorted(career_scores.items(), key=lambda x: x[1], reverse=True)

    print("\n==============================")
    print("   Career Recommendation")
    print("==============================")

    print("\nTop 3 Career Suggestions:\n")

    for career, score in sorted_careers[:3]:
        print(career, "-> Score:", score)