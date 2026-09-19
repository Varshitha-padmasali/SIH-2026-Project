from ai.simplification.simplifier import simplify_text
from ai.educational_nlp.concept_extractor import extract_concepts
from ai.educational_nlp.content_mapper import map_concepts_to_content
from ai.educational_nlp.lesson_mapper import create_lesson


def process_lesson(text: str, grade: int) -> dict:
    """
    Main AI pipeline.

    Input:
        text  -> educational text
        grade -> target student grade (1 to 3)

    Output:
        structured educational result
    """

    # Validate text
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    if not text.strip():
        raise ValueError("text cannot be empty")

    # Validate grade
    if not isinstance(grade, int):
        raise TypeError("grade must be an integer")

    if grade < 1 or grade > 3:
        raise ValueError("grade must be between 1 and 3")

    # Step 1: Simplify
    simplified_text = simplify_text(text, grade)

    # Step 2: Extract concepts
    concepts = extract_concepts(simplified_text)

    # Step 3: Map concepts to educational content
    content = map_concepts_to_content(concepts)

    # Step 4: Create lesson structure
    lesson = create_lesson(
        concepts,
        simplified_text,
        grade
    )

    # Final structured output
    result = {
        "original_text": text,
        "simplified_text": simplified_text,
        "grade": grade,
        "concepts": concepts,
        "content": content,
        "lesson": lesson
    }

    return result