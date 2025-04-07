class UserPreference:
    def __init__(self, user_id):
        self.user_id = user_id
        self.body_preference = 3
        self.richness_preference = 3
        self.smoke_preference = 3
        self.sweetness_preference = 3
        self.preferred_price_range = (None, None)  # (최소, 최대)
    
    def update_preference(self, preference_type, value):
        pass
    
    def update_price_range(self, min_price, max_price):
        pass
    
    def get_price_range(self):
        pass
    
    def get_preference_vector(self):
        pass