import re


# Advanced Regex Examples
def advanced_regex_examples():
    text = "Price: $5.00. The product code is A123BC, contact (123) 456-7890."

    # 1. Non-Capturing Groups (?:) - Groups without capturing the result
    pattern_non_capturing = r"(?:A|B)\d{3}"
    match_non_capturing = re.findall(pattern_non_capturing, text)
    print(
        "Example of Non-Capturing Group (?:) :", match_non_capturing
    )  # Output: ['A123']

    # 2. Positive Lookahead (?=) - Asserts that what follows the pattern must match
    pattern_positive_lookahead = r"\d+(?= BC)"
    match_positive_lookahead = re.findall(pattern_positive_lookahead, text)
    print(
        "Example of Positive Lookahead (?=) :", match_positive_lookahead
    )  # Output: []

    # 3. Negative Lookahead (?!): Asserts that what follows the pattern must not match
    pattern_negative_lookahead = r"A\d{3}(?! BC)"
    match_negative_lookahead = re.findall(pattern_negative_lookahead, text)
    print(
        "Example of Negative Lookahead (?!):", match_negative_lookahead
    )  # Output: ['A123']

    # 4. Positive Lookbehind (?<=): Asserts that what precedes the pattern must match
    pattern_positive_lookbehind = r"(?<=\$)\d+\.\d{2}"
    match_positive_lookbehind = re.findall(pattern_positive_lookbehind, text)
    print(
        "Example of Positive Lookbehind (?<=):", match_positive_lookbehind
    )  # Output: ['5.00']

    # 5. Negative Lookbehind (?<!): Asserts that what precedes the pattern must not match
    pattern_negative_lookbehind = r"(?<!\()\d{3}"
    match_negative_lookbehind = re.findall(pattern_negative_lookbehind, text)
    print(
        "Example of Negative Lookbehind (?<!):", match_negative_lookbehind
    )  # Output: ['456', '789']

    # 6. Inline Modifiers (?i): Case-insensitive matching
    pattern_inline_modifier = r"(?i)price"
    match_inline_modifier = re.findall(pattern_inline_modifier, text)
    print(
        "Example of Inline Modifier (?i):", match_inline_modifier
    )  # Output: ['Price']

    # 7. Named Groups (?P<name>): Captures a group and assigns it a name
    pattern_named_group = r"(?P<area_code>\d{3})\D*(?P<number>\d{3}-\d{4})"
    match_named_group = re.search(pattern_named_group, text)
    if match_named_group:
        print("Example of Named Groups (?P<name>):")
        print("Area Code:", match_named_group.group("area_code"))  # Output: 123
        print("Number:", match_named_group.group("number"))  # Output: 456-7890

    # 8. Conditional Matching (?(id/name)) - Matches based on a condition
    pattern_conditional = r"(\d{3})(?(1)-\d{3}-\d{4})"
    match_conditional = re.findall(pattern_conditional, text)
    print(
        "Example of Conditional Matching (?(id/name)):", match_conditional
    )  # Output: [('123', '456-7890')]

    # 9. Find and Replace with re.sub using functions
    def replace_function(match):
        return match.group(0).upper()

    pattern_replace_function = r"[a-z]+"
    new_text = re.sub(
        pattern_replace_function, replace_function, "this is a lowercase text"
    )
    print(
        "Example of re.sub with function:", new_text
    )  # Output: THIS IS A LOWERCASE TEXT


# Additional Useful Functions in Regex


# re.match - Matches a pattern only at the beginning of the string
def match_function_example():
    text = "Python is awesome."
    pattern = r"^Python"
    match = re.match(pattern, text)
    if match:
        print("re.match found:", match.group())  # Output: Python


# re.split - Splits a string by the occurrences of a pattern
def split_function_example():
    text = "One,Two,Three;Four.Five"
    pattern = r"[,;.]"  # Split by commas, semicolons, or periods
    result = re.split(pattern, text)
    print("re.split result:", result)  # Output: ['One', 'Two', 'Three', 'Four', 'Five']


# re.finditer - Returns an iterator yielding match objects
def finditer_function_example():
    text = "10 apples, 20 oranges, 30 bananas"
    pattern = r"\d+"
    for match in re.finditer(pattern, text):
        print(f"Found {match.group()} at position {match.start()}-{match.end()}")


# re.compile - Compiles a regex pattern into a regex object for reuse
def compile_function_example():
    text = "Hello World"
    pattern = re.compile(r"world", re.IGNORECASE)
    match = pattern.search(text)
    if match:
        print("re.compile found:", match.group())  # Output: World


# Main function to call everything
def main():
    print("Advanced Regex Examples:")
    advanced_regex_examples()

    print("\nUsing re.match:")
    match_function_example()

    print("\nUsing re.split:")
    split_function_example()

    print("\nUsing re.finditer:")
    finditer_function_example()

    print("\nUsing re.compile:")
    compile_function_example()

if __name__ == "__main__":
    main()
