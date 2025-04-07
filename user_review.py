import datetime

class User_Review:
    #사용자 위스키 리뷰
    
    def __init__(self, review_id, user_id, whiskey_id, rating, review_text=""):
        # 리뷰 초기화
        self.review_id = review_id
        self.user_id = user_id
        self.whiskey_id = whiskey_id
        self.rating = rating
        self.review_text = review_text
        self.review_date = datetime.datetime.now()
    
    def update_review(self, new_rating=None, new_text=None):
        #리뷰 내용 업뎃
        pass
    
    def get_review_details(self):
        # 리뷰 상세 정보 반환
        pass
    
    def __str__(self):
        return f"리뷰(ID:{self.review_id}, 평점:{self.rating})"