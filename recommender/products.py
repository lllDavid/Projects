class Products:
    products = {
        "Electronics": {
            "Smartphones": [
                {"key": "product_001", "name": "Smartphone X", "brand": "TechCorp", "price": 699.99},
                {"key": "product_002", "name": "Smartphone Y", "brand": "NextGen", "price": 799.99},
                {"key": "product_003", "name": "Smartphone Z", "brand": "MobiTek", "price": 599.99},
                {"key": "product_040", "name": "Smartphone A1", "brand": "NovaTech", "price": 549.99},
                {"key": "product_041", "name": "Smartphone B2", "brand": "Zenith", "price": 649.99}
            ],
            "Laptops": [
                {"key": "product_004", "name": "Laptop Pro", "brand": "XtremeGear", "price": 1299.99},
                {"key": "product_005", "name": "Laptop Air", "brand": "LightTech", "price": 999.99},
                {"key": "product_006", "name": "Laptop Go", "brand": "SpeedComp", "price": 899.99},
                {"key": "product_042", "name": "Laptop Ultra", "brand": "MegaComp", "price": 1399.99},
                {"key": "product_043", "name": "Laptop Mini", "brand": "SlimTech", "price": 749.99}
            ],
            "Smartwatches": [
                {"key": "product_007", "name": "Smartwatch Alpha", "brand": "TimeTech", "price": 199.99},
                {"key": "product_008", "name": "Smartwatch Beta", "brand": "WristIQ", "price": 179.99},
                {"key": "product_009", "name": "Smartwatch Gamma", "brand": "PulseGear", "price": 149.99},
                {"key": "product_044", "name": "Smartwatch Delta", "brand": "ChronoPro", "price": 159.99},
                {"key": "product_045", "name": "Smartwatch Epsilon", "brand": "WearIt", "price": 189.99}
            ]
        },
        "Health": {
            "Supplements": [
                {"key": "product_010", "name": "Vitamins Pack", "brand": "HealthPlus", "price": 29.99},
                {"key": "product_011", "name": "Omega-3 Capsules", "brand": "HeartCare", "price": 25.99},
                {"key": "product_012", "name": "Protein Powder", "brand": "FitFuel", "price": 39.99},
                {"key": "product_046", "name": "Multivitamins", "brand": "WellLife", "price": 34.99},
                {"key": "product_047", "name": "Energy Booster", "brand": "ActiveCore", "price": 22.99}
            ],
            "Fitness Gear": [
                {"key": "product_013", "name": "Yoga Mat", "brand": "ZenFlex", "price": 45.00},
                {"key": "product_014", "name": "Foam Roller", "brand": "RecoveryPro", "price": 34.50},
                {"key": "product_015", "name": "Resistance Bands", "brand": "StretchPro", "price": 21.99},
                {"key": "product_048", "name": "Kettlebell Set", "brand": "PowerFit", "price": 59.99},
                {"key": "product_049", "name": "Jump Rope", "brand": "CardioMax", "price": 15.99}
            ]
        },
        "Food": {
            "Cookware": [
                {"key": "product_016", "name": "Non-stick Frying Pan", "brand": "ChefLine", "price": 24.99},
                {"key": "product_017", "name": "Knife Set", "brand": "SharpEdge", "price": 59.99},
                {"key": "product_018", "name": "Cutting Board", "brand": "BoardMate", "price": 19.99},
                {"key": "product_050", "name": "Saucepan Set", "brand": "CookMaster", "price": 79.99},
                {"key": "product_051", "name": "Baking Tray", "brand": "BakePro", "price": 22.99}
            ],
            "Storage": [
                {"key": "product_019", "name": "Glass Containers", "brand": "FreshKeep", "price": 27.99},
                {"key": "product_020", "name": "Lunch Box", "brand": "MealMate", "price": 14.99},
                {"key": "product_021", "name": "Spice Jars", "brand": "FlavorTidy", "price": 18.75},
                {"key": "product_052", "name": "Freezer Bags", "brand": "CoolPack", "price": 9.99},
                {"key": "product_053", "name": "Vacuum Sealer", "brand": "SealTech", "price": 59.99}
            ]
        },
        "Clothing": {
            "Tops": [
                {"key": "product_022", "name": "T-Shirt", "brand": "StyleWear", "price": 14.99},
                {"key": "product_023", "name": "Sweatshirt", "brand": "CozyClub", "price": 39.99},
                {"key": "product_024", "name": "Tank Top", "brand": "FitFlex", "price": 12.50},
                {"key": "product_054", "name": "Hoodie", "brand": "UrbanStyle", "price": 49.99},
                {"key": "product_055", "name": "Polo Shirt", "brand": "ClassicWear", "price": 34.99}
            ],
            "Bottoms": [
                {"key": "product_025", "name": "Jeans", "brand": "DenimPro", "price": 49.99},
                {"key": "product_026", "name": "Shorts", "brand": "CoolGear", "price": 29.99},
                {"key": "product_027", "name": "Joggers", "brand": "UrbanMotion", "price": 44.99},
                {"key": "product_056", "name": "Chinos", "brand": "SmartFit", "price": 39.99},
                {"key": "product_057", "name": "Cargo Pants", "brand": "TrailWear", "price": 54.99}
            ],
            "Footwear": [
                {"key": "product_028", "name": "Sneakers", "brand": "RunFast", "price": 89.99},
                {"key": "product_029", "name": "Sandals", "brand": "BeachSteps", "price": 24.99},
                {"key": "product_030", "name": "Boots", "brand": "TrailMaster", "price": 99.99},
                {"key": "product_058", "name": "Loafers", "brand": "CityWalk", "price": 69.99},
                {"key": "product_059", "name": "Flip Flops", "brand": "SunnyDay", "price": 19.99}
            ]
        },
        "Books": {
            "Fiction": [
                {"key": "product_031", "name": "Sci-Fi Novel", "brand": "FutureReads", "price": 12.99},
                {"key": "product_032", "name": "Mystery Thriller", "brand": "PageTurner", "price": 13.99},
                {"key": "product_033", "name": "Fantasy Saga", "brand": "EpicTales", "price": 15.99},
                {"key": "product_060", "name": "Historical Drama", "brand": "StoryHouse", "price": 14.50},
                {"key": "product_061", "name": "Romance Novel", "brand": "LoveBooks", "price": 11.99}
            ],
            "Cooking": [
                {"key": "product_034", "name": "Cooking Guide", "brand": "ChefMaster", "price": 22.50},
                {"key": "product_035", "name": "Vegan Recipes", "brand": "GreenTable", "price": 18.25},
                {"key": "product_036", "name": "Grilling Manual", "brand": "BBQBoss", "price": 20.00},
                {"key": "product_062", "name": "Baking Basics", "brand": "BakeCraft", "price": 19.99},
                {"key": "product_063", "name": "Slow Cooker Meals", "brand": "EasyCook", "price": 21.50}
            ],
            "Self-Help": [
                {"key": "product_037", "name": "Mindfulness Manual", "brand": "CalmCore", "price": 16.50},
                {"key": "product_038", "name": "Success Habits", "brand": "MindfulPath", "price": 18.75},
                {"key": "product_039", "name": "Productivity Hacks", "brand": "FocusFuel", "price": 17.95},
                {"key": "product_064", "name": "Stress Relief Guide", "brand": "PeaceWorks", "price": 15.75},
                {"key": "product_065", "name": "Goal Setting 101", "brand": "AchieveMore", "price": 19.99}
            ]
        }
    }
