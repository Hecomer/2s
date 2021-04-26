def password_level(password):
    if len(password) < 6:
        print('«Недопустимый пароль»')
    elif password.isdigit() == True or ((password.islower() == True or password.isupper() == True) and len(list(filter(lambda sym: sym.isdigit(), password))) == 0):
        print("«Ненадежный пароль»")
    elif (password.islower() == True and password.isupper() == True and len(list(filter(lambda sym: sym.isdigit(), password))) == 0) or ((password.islower() == True or password.isupper() == True) and len(list(filter(lambda sym: sym.isdigit(), password))) > 0):
        print('«Слабый пароль»')
    elif len(list(filter(lambda sym: sym.isdigit(), password))) > 0 and len(list(filter(lambda sym: sym.islower(), password))) > 0 and len(list(filter(lambda sym: sym.isupper(), password))) > 0:
        print("«Надежный пароль»")


password_level('g7R9uYRWeujjj')