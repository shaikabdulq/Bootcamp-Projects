import random

def word_list():
    word_list = [
        "agneepath", "baahubali", "badlapur", "barfi", "bharat", "bhuj", "brahmastra", "cocktail", "dabangg", "dhoom",
        "dilwale", "don", "dostana", "fashion", "ghajini", "golmaal", "guru", "haider", "housefull", "judwaa", "kalank",
        "kaminey", "kesari", "krrish", "laxmii", "ludo", "mimi", "mom", "neerja", "october", "omkara", "padmaavat", "panipat",
        "pathan", "piku", "pink", "pk", "queen", "raajneeti", "raazi", "race", "radhe", "raees", "raid", "rangoon",
        "rockstar", "roohi", "rrr", "sanju", "shershaah", "simmba", "sooryavanshi", "stree", "sultan", "tanhaji", "wanted", "war"
    ]
    word = random.choice(word_list)
    return word
