from ai.educational_nlp.topic_map import TOPIC_MAP


def create_lesson(concepts: list[str], simplified_text: str, grade: int) -> dict:
    """
    Create a structured educational lesson from extracted concepts.
    """

    topic = "General Science"

    for topic_id, topic_data in TOPIC_MAP.items():
        required_concepts = topic_data["required_concepts"]

        if all(concept in concepts for concept in required_concepts):
            topic = topic_data["name"]
            break

    return {
    "topic": topic,
    "grade": grade,
    "explanation": simplified_text,
    "concepts": concepts,
    "resources": {
        "visuals": concepts,
        "audio": ["lesson_explanation"],
        "activities": [f"{topic.lower().replace(' ', '_')}_activity"]
        }
    }