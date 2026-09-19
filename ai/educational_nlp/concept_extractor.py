import re


# Basic educational concepts for our MVP
EDUCATIONAL_CONCEPTS = {
    "plants": ["plant", "plants"],
    "water": ["water"],
    "sunlight": ["sunlight", "sun"],
    "air": ["air"],
    "animals": ["animal", "animals"],
    "trees": ["tree", "trees"],
    "food": ["food"],
    "growth": ["grow", "grows", "growth"],
    "oxygen": ["oxygen"],
    "living_things": ["living", "living things"],
}


def extract_concepts(text: str) -> list[str]:
    """
    Extract educational concepts from text.

    This is a baseline implementation.
    A proper NLP model can replace it later.
    """

    text = text.lower()

    # Remove punctuation
    text = re.sub(r"[^\w\s]", "", text)

    concepts = []

    for concept, keywords in EDUCATIONAL_CONCEPTS.items():
        for keyword in keywords:
            if keyword in text.split():
                concepts.append(concept)
                break

    return concepts