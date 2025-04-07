from user_preference import UserPreference
from user_history import UserHistory

class User:
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
        pass
    
    def set_history(self, history):
        pass
    
    def get_user_default_information(self):
        pass
    
    def get_preference(self):
        pass
    
    def get_history(self):
        pass
    
    def add_review_id(self, review_id):
        pass
    
    def get_review_ids(self):
        pass