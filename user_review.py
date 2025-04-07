import datetime

class UserReview:
    def __init__(self, review_id, user_id, whiskey_id, rating, review_text=""):
        self.review_id = review_id
        self.user_id = user_id
        self.whiskey_id = whiskey_id
        self.rating = rating  # 평점 (1-5)
        self.review_text = review_text
        self.review_date = datetime.datetime.now()
    
    def update_review(self, new_rating=None, new_text=None):
        pass
    
    def get_review_details(self):
        pass
    
    def __str__(self):
        pass