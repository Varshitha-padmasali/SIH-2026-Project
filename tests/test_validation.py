from ai.pipeline.processor import process_lesson


# Test 1: Empty text
try:
    process_lesson("", 2)
    print("❌ Empty text validation failed")
except ValueError as e:
    print("✅ Empty text validation passed:", e)


# Test 2: Invalid grade
try:
    process_lesson("Plants need water.", 5)
    print("❌ Grade validation failed")
except ValueError as e:
    print("✅ Grade validation passed:", e)


# Test 3: Invalid text type
try:
    process_lesson(123, 2)
    print("❌ Text type validation failed")
except TypeError as e:
    print("✅ Text type validation passed:", e)


# Test 4: Invalid grade type
try:
    process_lesson("Plants need water.", "2")
    print("❌ Grade type validation failed")
except TypeError as e:
    print("✅ Grade type validation passed:", e)