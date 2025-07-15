class Post:

    def __init__(self, post_info):
        self.id = post_info["id"]
        self.title = post_info["title"]
        self.subtitle = post_info["subtitle"]
        self.body = post_info["body"]
