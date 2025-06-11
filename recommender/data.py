class Data:
    def __init__(self):
        self.data = {}
        self.category_scores = {}
        self.subcategory_scores = {}

    def add(self, key, value):
        value.setdefault("score", 0)
        if key in self.data:
            self.data[key].update(value)
            self.data[key].setdefault("score", 0)
        else:
            self.data[key] = value

        cat = value.get("category")
        if cat and cat not in self.category_scores:
            self.category_scores[cat] = 0
        subcat = value.get("subcategory")
        if cat and subcat and (cat, subcat) not in self.subcategory_scores:
            self.subcategory_scores[(cat, subcat)] = 0

    def increase_score(self, key, amount=1):
        if key not in self.data:
            print(f"Item {key} not found.")
            return
        self.data[key]['score'] += amount
        cat = self.data[key].get("category")
        if cat:
            self.category_scores[cat] += amount
        subcat = self.data[key].get("subcategory")
        if cat and subcat:
            self.subcategory_scores[(cat, subcat)] += amount

    def get_product(self, key):
        return self.data.get(key)

    def get_sorted_by_score(self):
        return sorted(self.data.values(), key=lambda x: x['score'], reverse=True)

    def get_top_categories(self, n=3):
        return sorted(self.category_scores.items(), key=lambda x: x[1], reverse=True)[:n]

    def get_top_subcategories(self, n=3):
        return sorted(self.subcategory_scores.items(), key=lambda x: x[1], reverse=True)[:n]
