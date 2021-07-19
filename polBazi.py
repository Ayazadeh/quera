""" 87184 """


class Account:
    # username = 'mohammad'

    def __init__(self, username):

        try:
            name, family = username.split('_')
            if self.is_english(name, family):
                self.username = name + '_' + family
        except ValueError:
            print('invalid username')

    def is_english(self, name, family):
        lower = 'abcdefghijklmnopqrstuvwxyz'
        upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        if name and family in lower:
            return True
        return False

    def show_welcome(self):
        username = self.username.replace('_', ' ').title()
        if len(username) > 15:
            return username.replace(username[15:], '...')
        return username

    def verify_change_password(self):
        pass


a = Account('mohammad_Ayazad')
print(a.username)


class Site:
    pass
