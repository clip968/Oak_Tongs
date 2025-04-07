class User_Preference:
    # 사용자의 위스키 취향
    
    def __init__(self, user_id):
        self.user_id = user_id
        self.body_preference = 3
        self.richness_preference = 3
        self.smoke_preference = 3
        self.sweetness_preference = 3
        self.preferred_price_range = (None, None)
    
    def update_preference(self, preference_type, value):
        # 맛 선호도 업데이트
        pass
    
    def update_price_range(self, min_price, max_price):
        # 가격 범위 업데이트
        pass
    
    def get_price_range(self):
        # 선호 가격 범위 반환
        pass
    
    def get_preference_vector(self):
        # 선호 벡터 반환
        pass