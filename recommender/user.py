class User:
    id = 1  

    def __init__(self, *seen):
        self.id = User.id
        User.id += 1
        self.seen = list(seen)

    def add_seen(self, item_key):
        if item_key not in self.seen:
            self.seen.append(item_key)

    def has_seen(self, item_key):
        return item_key in self.seen
