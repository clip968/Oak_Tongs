import math
from recommendation import Recommendation

class RecommendationSimilar(Recommendation):
    def __init__(self, user_reference, whiskeys_reference):
        super().__init__(user_reference, whiskeys_reference)
        self.similarity_threshold = 0.5  
    
    def get_recommendations(self, count, base_whiskey_id=None):
        pass
    
    def find_similar_whiskeys(self, base_whiskey_id, count):
        pass
    
    def calculate_taste_similarity(self, whiskey1, whiskey2):
        pass