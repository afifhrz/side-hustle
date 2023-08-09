def is_palindrom(text_input):
    for i in range(len(text_input)):
        if text_input[i] != text_input[-1*(i+1)]:
            return False
    return True
        
input_text = input("Check Palindrom: ")
print(is_palindrom(input_text))