userId = input('아이디를 입력하세요 : ')
if userId == 'lovePython!':
    usrPwd = input('비밀번호를 입력하세요 : ')
    if usrPwd == 'p12345':
        print('{}님환영합니다~!!'.format(userId)) 
    else:  
        print('비밀번호가틀립니다.') 
else:  
    print('아이디를찾을수없습니다.')