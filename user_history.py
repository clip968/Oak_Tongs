import datetime
from collections import deque

class UserHistory:
    MAX_VIEWED_ITEMS = 20
    
    def __init__(self, user_id):
        self.user_id = user_id
        self.viewed_whiskeys = deque(maxlen=self.MAX_VIEWED_ITEMS)  # (위스키ID, 조회시각)
        self.added_whiskeys = []  # 컬렉션에 추가한 위스키 ID
    
    def add_viewed_whiskey(self, whiskey_id):
        pass
    
    def add_to_collection(self, whiskey_id):
        pass
    
    def remove_from_collection(self, whiskey_id):
        pass
    
    def get_recently_viewed(self, count=None):
        pass
    
    def get_collection(self):
        pass
    
    def is_in_collection(self, whiskey_id):
        pass