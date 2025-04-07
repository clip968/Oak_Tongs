class User:
    # 사용자 기본 정보
    
    def __init__(self, user_id, user_name, user_age=None, user_sex=None):
        self.user_id = user_id
        self.user_name = user_name
        self.user_age = user_age
        self.user_sex = user_sex
        
        # 관련 객체들
        self.user_preference = None
        self.user_history = None
        self.user_review_ids = []
    
    def set_preference(self, preference):
        # 선호도 객체 설정
        pass
    
    def set_history(self, history):
        # 활동 기록 객체 설정
        pass
    
    def get_user_default_information(self):
        # 기본 정보 반환
        pass
    
    def get_preference(self):
        # 선호도 객체 반환
        pass
    
    def get_history(self):
        # 활동 기록 객체 반환
        pass
    
    def add_review_id(self, review_id):
        # 리뷰 id 추가
        pass
    
    def get_review_ids(self):
        # 리뷰 목록 반환
        pass