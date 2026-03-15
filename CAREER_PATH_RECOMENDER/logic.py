from career_description import career_description 

def show_description(career_scores):
    sorted_careers = sorted(career_scores.items(), key=lambda x: x[1], reverse=True)
    best_career = sorted_careers[0][0]

    print("\nRecommended Career:", best_career)
    print("Description:", career_description[best_career])