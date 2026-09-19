from ai.simplification.simplifier import simplify_text
from ai.educational_nlp.concept_extractor import extract_concepts
from ai.educational_nlp.content_mapper import map_concepts_to_content 
from ai.educational_nlp.lesson_mapper import create_lesson  

def process_lesson(text: str, grade: int) -> dict:
    """
    Main AI pipeline.

    Input:
        text  -> educational text
        grade -> target student grade

    Output:
        structured educational result
    """

    # Step 1: Simplify the educational text
    simplified_text = simplify_text(text, grade)

    # Step 2: Extract important educational concepts
    concepts = extract_concepts(simplified_text)

    # Step 3: Combine the results
    content = map_concepts_to_content(concepts)

    lesson = create_lesson(
    concepts,
    simplified_text,
    grade)

    result = {
    "original_text": text,
    "simplified_text": simplified_text,
    "grade": grade,
    "concepts": concepts,
    "content": content,
    "lesson": lesson
    }

    return result