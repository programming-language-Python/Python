nomer=input('Введите номер телефона: ')
# Вариант 1
'''
if nomer.isdigit() and (nomer.startswith('8') or nomer.startswith('7')) and (nomer[1]=='9' or nomer[1]=='4') and len(nomer)==11:
    nomer='+7('+nomer[1:]
    nomer=nomer.replace(nomer[3:6],nomer[3:6]+')')
    nomer=nomer.replace(nomer[-4:-2],'-'+nomer[-4:-2]+'-')
    print(nomer)
else:
    print('Вы ввели не номер телефона или ввели с недопустимыми символами')
'''
# Вариант 2
if nomer.isdigit()==False:
    newnomer=''
    for j in nomer:
        if j.isdigit()==True:
            newnomer+=j
if (newnomer.startswith('8') or newnomer.startswith('7')) and (newnomer[1]=='9' or newnomer[1]=='4') and len(newnomer)==11:
    newnomer='+7('+newnomer[1:]
    newnomer=newnomer.replace(newnomer[3:6],newnomer[3:6]+')')
    newnomer=newnomer.replace(newnomer[-4:-2],'-'+newnomer[-4:-2]+'-')
    print(newnomer)
else:
    print('Вы ввели некорректный номер телефона')