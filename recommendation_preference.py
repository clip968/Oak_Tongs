from recommendation import Recommendation

class RecommendationPreference(Recommendation):
    def __init__(self, user_reference, whiskeys_reference):
        super().__init__(user_reference, whiskeys_reference)
    
    def get_recommendations(self, count):
        pass
    
    def calculate_preference_match(self, user_preference, whiskey):
        pass