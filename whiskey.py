class Whiskey:
    # 위스키 기본 정보
    def __init__(self, whiskey_id, name, taste_profile, origin, price, 
                 alcohol_percentage, whiskey_type, image_path=None, age_years=None):
        self.id = whiskey_id
        self.name = name
        self.taste_profile = taste_profile
        self.origin = origin
        self.price = price
        self.alcohol_percentage = alcohol_percentage
        self.type = whiskey_type
        self.image_path = image_path
        self.age_years = age_years
        self.user_review_ids = []
    
    def get_taste_vector(self):
        # 맛 프로필 벡터로 변환
        pass
    
    def get_basic_info(self):
        # 기본 정보 호출
        pass
    
    def get_full_details(self):
        # 모든 상세 정보 반환
        pass
    
    def add_review_id(self, review_id):
        # 리뷰 id 추가
        pass
    
    def __str__(self):
        return f"{self.name} ({str(self.type)})"