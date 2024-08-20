def is_palindrome_recursive(phrase):
    s = ''.join(c.lower() for c in phrase if c.isalnum())
    
    if len(s) <= 1:
        return True
    
    if s[0] == s[-1]:
        return is_palindrome_recursive(s[1:-1])
    else:
        return False
    
phrases = ["A man, a plan, a canal: Panama", "race a car", "hello"]
for string in phrases:
    print(is_palindrome_recursive(string))