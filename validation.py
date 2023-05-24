from BasicValues import users, admins

def AdminValidation(id, password):
    for i in admins:
        if(i.id == id and i.password == password):
            return 5
    return 8

def UserValidation(id, password):
    for i in users:
        print(i.id)
        print(i.password)
        if(i.id == id and i.password == password):
            return 6
    return 8