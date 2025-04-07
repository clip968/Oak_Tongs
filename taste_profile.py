class TasteProfile:
    def __init__(self, body=3, richness=3, smoke=3, sweetness=3):
        self.body = body          # 바디감 (0-5)
        self.richness = richness  # 깊이 (0-5)
        self.smoke = smoke        # 스모키 (0-5)
        self.sweetness = sweetness # 단맛 (0-5)
    
    def get_vector(self):
        pass
    
    def __str__(self):
        pass