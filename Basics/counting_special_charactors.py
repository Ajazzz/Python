


st = ''
lio = '!-:,."'
special_char = ''
special_char_count = 0
count = 0

for i in string:
    if i == 'a':
        st += i
        count += 1
    elif i in lio:
        special_char += i
        special_char_count += 1
    else:
        pass
print(st)
print(count)
print(special_char)
print(special_char_count)
