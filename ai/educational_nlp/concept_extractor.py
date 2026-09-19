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
    "living_things": ["living things"],
}


def extract_concepts(text: str) -> list[str]:
    """
    Extract educational concepts from text.

    Uses phrase matching so both single-word
    and multi-word concepts can be detected.
    """

    text = text.lower()

    # Remove punctuation but preserve spaces
    text = re.sub(r"[^\w\s]", "", text)

    concepts = []

    for concept, keywords in EDUCATIONAL_CONCEPTS.items():
        for keyword in keywords:
            # Match complete words/phrases
            pattern = r"\b" + re.escape(keyword) + r"\b"

            if re.search(pattern, text):
                concepts.append(concept)
                break

    return concepts