from taste_profile import TasteProfile
from whiskey_type import WhiskeyType

class Whiskey:
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
        pass
    
    def get_basic_info(self):
        pass
    
    def get_full_details(self):
        pass
    
    def add_review_id(self, review_id):
        pass
    
    def __str__(self):
        pass