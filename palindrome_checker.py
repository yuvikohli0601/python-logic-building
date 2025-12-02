def is_palindrome_string(s: str) -> bool:
    s = s.lower()
    return s == s[::-1]

def is_palindrome_number(n: int) -> bool:
    return str(n) == str(n)[::-1]

def is_sentence_palindrome(s: str) -> bool:
    cleaned = "".join(ch.lower() for ch in s if not ch.isspace())
    return cleaned == cleaned[::-1]

if __name__ == "__main__":
    text = input("Enter text: ")
    if text.isdigit():
        print(is_palindrome_number(int(text)))
    else:
        print(is_palindrome_string(text))
