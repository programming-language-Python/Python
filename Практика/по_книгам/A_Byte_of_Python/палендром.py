'''
def reverse(text):
    return text[::-1]
def is_palindrome(text):
    return text == reverse(text)
something = input('Введите текст: ')
if (is_palindrome(something)):
     print("Да, это палиндром") 
else:
    print("Нет, это не палиндром")
'''
# улучшенная
def reverse(text):
    return text[::-1]
def is_palindrome(text):
    text.lower()
    text=text.replace(',','')
    text=text.replace(' ','')
    text=text.replace('!','')
    text=text.replace('.','')
    text=text.replace('?','')
    text=text.replace(':','')
    text=text.replace(';','')
    text=text.replace('...','')
    text=text.replace('/','')
    return text == reverse(text)
something = input('Введите текст: ')
if (is_palindrome(something)):
     print("Да, это палиндром") 
else:
    print("Нет, это не палиндром")