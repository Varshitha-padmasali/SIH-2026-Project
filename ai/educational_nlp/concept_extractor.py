def extract_concepts(text: str) -> list[str]:
    """
    Extract basic educational concepts.

    This is a baseline implementation.
    It can later be replaced with an NLP model.
    """

    concepts = []

    keywords = {
        "plant",
        "plants",
        "water",
        "sun",
        "sunlight",
        "air",
        "animal",
        "animals",
        "tree",
        "trees",
        "food"
    }

    words = text.lower().split()

    for word in words:
        word = word.strip(".,!?;:")

        if word in keywords and word not in concepts:
            concepts.append(word)

    return concepts