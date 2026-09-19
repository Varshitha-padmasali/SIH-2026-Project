CONTENT_MAP = {
    "plants": {
        "topic": "Plants",
        "visual": "plant",
        "description": "Plants are living things that grow."
    },

    "water": {
        "topic": "Water",
        "visual": "water",
        "description": "Water is needed by people, animals, and plants."
    },

    "sunlight": {
        "topic": "Sunlight",
        "visual": "sun",
        "description": "Sunlight helps plants grow."
    },

    "growth": {
        "topic": "Growth",
        "visual": "plant_growth",
        "description": "Growth means becoming bigger or developing."
    },

    "animals": {
        "topic": "Animals",
        "visual": "animal",
        "description": "Animals are living things that need food, water, and air."
    },

    "food": {
        "topic": "Food",
        "visual": "food",
        "description": "Food gives living things energy."
    },

    "air": {
        "topic": "Air",
        "visual": "air",
        "description": "Living things need air to live."
    },

    "trees": {
        "topic": "Trees",
        "visual": "tree",
        "description": "Trees are large plants that grow tall."
    },

    "oxygen": {
        "topic": "Oxygen",
        "visual": "oxygen",
        "description": "Oxygen is a gas that living things need to breathe."
    },
    
    "living_things": {
    "topic": "Living Things",
    "visual": "living_things",
    "description": "Living things need water, air, and food to live."
    }
}


def map_concepts_to_content(concepts: list[str]) -> list[dict]:
    """
    Map extracted concepts to educational content.
    """

    content = []

    for concept in concepts:
        if concept in CONTENT_MAP:
            content.append({
                "concept": concept,
                **CONTENT_MAP[concept]
            })

    return content