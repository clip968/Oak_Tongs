import os
import json
import datetime

from user import User
from user_preference import User_Preference
from user_history import User_History
from user_review import User_Review
from whiskys import Whiskys
from whiskey import Whiskey
from taste_profile import TasteProfile
from whiskey_type import WhiskeyType
from recommendation_preference import Recommendation_Preference
from recommendation_similar import Recommendation_Similar

# 데이터 경로
DATA_DIR = "data"
USER_FILE = os.path.join(DATA_DIR, "user_data.json")
WHISKEY_FILE = os.path.join(DATA_DIR, "whiskey_catalog.json")
REVIEWS_FILE = os.path.join(DATA_DIR, "reviews.json")

class System:
    # 앱 총괄 관리 서비스
    
    def __init__(self):
        # 시스템 초기화
        self.current_user = None
        self.whiskey_catalog = Whiskys()
        self.all_reviews = {}
        self.recommendation_engine = None
        self.ui_reference = None
    
    def initialize(self, ui_reference=None):
        # 초기화
        pass
    
    def manage_user(self, action, user_info=None):
        # 사용자 관리 (등록, 수정, 삭제)
        pass
    
    def manage_data(self, action):
        # 데이터 관리 (불러오기, 저장)
        pass
    
    def manage_whiskey(self, action, whiskey_id=None, review_data=None):
        # 위스키 관리 (등록, 수정, 삭제)
        pass
    
    def get_recommendations(self, count, method_type=None, base_whiskey_id=None):
        # 추천 위스키 목록 반환
        pass
    
    def run(self):
        # 실행
        pass
    
# 프로그램 실행 진입점
if __name__ == '__main__':
    system = System()
    system.run()