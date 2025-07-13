class User:
    def __init__(self, role):
        self.role = role


def create_user(role):
    return User(role)


u = create_user("admin")
print(u.role)
