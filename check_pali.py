def check_pali(word):
    flag=True
    for i in range(len(word)//2):
        back=-(i+1)
        if word[i]!=word[back]:
            flag=False
            break
    if flag:
        return True
    return False

print(check_pali(input('Введите слово: ')))

'''
придумал еще способ. не знаю, какой эффективнее, так что оставлю тут оба:
def check_pali(word):
    if len(word)%2==0:
        if word[:len(word)//2]==word[len(word):len(word)//2-1:-1]:
            return True
        else:
            return False
    else:
        if word[:len(word)//2+1]==word[len(word):len(word)//2-1:-1]:
            return True
        else:
            return False
'''
