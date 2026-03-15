import introduction_module
import intrest_question_module
import Recommendation_module
import logic

introduction_module.introduction()

scores = intrest_question_module.ask_questions()

Recommendation_module.recommend_career(scores)

logic.show_description(scores)