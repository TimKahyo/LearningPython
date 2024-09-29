import re


# Regex reserved characters examples
def regex_reserved_characters_examples():
    text = "This is a test text. Price: $5.00. Call me at (123) 456-7890 or email test@test.com."

    # 1. Dot (.) - Matches any character except a newline
    pattern_dot = r"t.st"
    match_dot = re.findall(pattern_dot, text)
    print("Example of . :", match_dot)  # Output: ['test', 'test']

    # 2. Caret (^) - Matches the start of the string
    pattern_caret = r"^This"
    match_caret = re.findall(pattern_caret, text)
    print("Example of ^ :", match_caret)  # Output: ['This']

    # 3. Dollar Sign ($) - Matches the end of the string
    pattern_dollar = r"com\.$"
    match_dollar = re.findall(pattern_dollar, text)
    print("Example of $ :", match_dollar)  # Output: ['com.']

    # 4. Asterisk (*) - Matches 0 or more repetitions of the preceding element
    pattern_asterisk = r"t.*t"
    match_asterisk = re.findall(pattern_asterisk, text)
    print("Example of * :", match_asterisk)  # Output: ['test text']

    # 5. Plus Sign (+) - Matches 1 or more repetitions of the preceding element
    pattern_plus = r"\d+"
    match_plus = re.findall(pattern_plus, text)
    print("Example of + :", match_plus)  # Output: ['5', '123', '456', '7890']

    # 6. Question Mark (?) - Matches 0 or 1 of the preceding element
    pattern_question = r"Price:? \$(\d+\.\d+)"
    match_question = re.findall(pattern_question, text)
    print("Example of ? :", match_question)  # Output: ['5.00']

    # 7. Curly Braces ({}) - Matches a specific number of repetitions
    pattern_braces = r"\d{3}"
    match_braces = re.findall(pattern_braces, text)
    print("Example of {} :", match_braces)  # Output: ['123', '456', '789']

    # 8. Square Brackets ([]) - Matches any one of the enclosed characters
    pattern_brackets = r"[aeiou]"
    match_brackets = re.findall(pattern_brackets, text)
    print("Example of [] :", match_brackets)  # Output: List of vowels found in the text

    # 9. Backslash (\) - Escapes special characters
    pattern_backslash = r"\$5\.00"
    match_backslash = re.findall(pattern_backslash, text)
    print("Example of \\ :", match_backslash)  # Output: ['$5.00']

    # 10. Pipe (|) - Acts as an OR operator
    pattern_pipe = r"Price|Call"
    match_pipe = re.findall(pattern_pipe, text)
    print("Example of | :", match_pipe)  # Output: ['Price', 'Call']

    # 11. Parentheses (()) - Used for grouping or capturing
    pattern_parentheses = r"\((\d{3})\)"
    match_parentheses = re.findall(pattern_parentheses, text)
    print("Example of () :", match_parentheses)  # Output: ['123']


def main():
    # Run the examples
    regex_reserved_characters_examples()


if __name__ == "__main__":
    main()
