import random
from products import Products
from data import Data
from user import User

def load_products(data, products_dict):
    for cat, subcats in products_dict.items():
        for subcat, prods in subcats.items():
            for p in prods:
                data.add(p["key"], {**p, "category": cat, "subcategory": subcat})

def simulate_user_views(data, user):
    for k in user.seen:
        data.increase_score(k)

def get_recommendations(data, user):
    seen = set(user.seen)
    items_sorted = data.get_sorted_by_score()
    top_cats = data.get_top_categories(1)
    if not top_cats:
        return []
    top_cat = top_cats[0][0]
    return [i for i in items_sorted if i.get("category") == top_cat and i["key"] not in seen]

def main():
    all_keys = None
    users = []
    for _ in range(3):
        data = Data()
        load_products(data, Products.products)
        if all_keys is None:
            all_keys = list(data.data.keys())
        seen_items = random.sample(all_keys, random.randint(8, 15))
        user = User(*seen_items)
        users.append((user, data))
        simulate_user_views(data, user)

    for idx, (user, data) in enumerate(users, 1):
        print(f"\nUser {idx} Viewed Items Ranked by Score\nCategory Scores")
        for c, s in sorted(data.category_scores.items(), key=lambda x: x[1], reverse=True):
            print(f"{c}: {s}")

        print("\nSubcategory Scores")
        for (c, sc), s in sorted(data.subcategory_scores.items(), key=lambda x: x[1], reverse=True):
            print(f"{sc} ({c}): {s}")

        print("\nTop Recommendations")
        for r in get_recommendations(data, user)[:5]:
            print(f" - {r['name']} ({r['category']} > {r['subcategory']}) | Score: {r['score']}")

if __name__ == "__main__":
    main()
