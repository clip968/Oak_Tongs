from recommendation import Recommendation
import math

class Recommendation_Similar(Recommendation):
    # 유사한 위스키 추천
    
    def __init__(self, user_reference, whiskeys_reference):
        super().__init__(user_reference, whiskeys_reference)
        self.similarity_threshold = 0.5  # 유사도 임계값
    
    def get_recommendations(self, count, base_whiskey_id=None):
        # 유사 위스키 추천 목록 반환
        pass
    
    def find_similar_whiskeys(self, base_whiskey_id, count):
        # 유사 위스키 찾아줌
        pass
    
    def calculate_taste_similarity(self, whiskey1, whiskey2):
        # 코사인 유사도로 맛 프로필 간 유사도 계산
        pass