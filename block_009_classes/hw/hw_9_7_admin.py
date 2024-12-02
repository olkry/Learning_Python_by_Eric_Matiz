from block_009_classes.hw.hw_9_8_privileges import Privileges
from hw_9_5_acces_try import User

class Administrator(User):

    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age, type_user='Administrator')
        self.privileges = Privileges()





if __name__ == '__main__':
    admin_1 = Administrator("Marazm", "Ezzov", 60)
    admin_1.describe_user()
    admin_1.privileges.show_privileges()

    admin_2 = Administrator("Gasty", "Mareno", 35)
    admin_2.describe_user()
    admin_2.privileges.add_duties("Контроль маразма", "Хостинг")
    admin_2.privileges.show_privileges()

