from recommendation import Recommendation

class Recommendation_Preference(Recommendation):
    # 사용자 선호도 기반 추천
    
    def __init__(self, user_reference, whiskeys_reference):
        super().__init__(user_reference, whiskeys_reference)
    
    def get_recommendations(self, count):
        # 사용자 기반 추천 목록 반환
        pass
    
    def calculate_preference_match(self, user_preference, whiskey):
        # 내 선호도와 위스키 맛 프로필 비교해서 추천 점수 계산
        pass