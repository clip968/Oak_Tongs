import datetime
from collections import deque

class User_History:
    # 위스키 기록
    
    MAX_VIEWED_ITEMS = 20  # 최근 조회 최대 개수
    
    def __init__(self, user_id):
        self.user_id = user_id
        self.viewed_whiskeys = deque(maxlen=self.MAX_VIEWED_ITEMS)
        self.added_whiskeys = []
    
    def add_viewed_whiskey(self, whiskey_id):
        # 조회한 위스키 ID 추가
        pass
    
    def add_to_collection(self, whiskey_id):
        # 컬렉션에 위스키 id 추가
        pass
    
    def remove_from_collection(self, whiskey_id):
        # 컬렉션에서 제거
        pass
    
    def get_recently_viewed(self, count=None):
        # 최근 조회한 위스키 목록 반환
        pass
    
    def get_collection(self):
        # 컬렉션 목록 반환
        pass
    
    def is_in_collection(self, whiskey_id):
        # 컬렉션에 있는지 확인
        pass