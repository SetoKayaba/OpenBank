import bank_ops as bank


class UserOptions:
    response = None

    def __init__(self):
        self.status = None

    def register(self, process_count=0):
        if process_count == 5:
            exit()
        try:
            number = int(input('Mobile Number:   '))
        except Exception as Error:
            print(Error)
            input("Please Re-Enter you're number and try again.")
            process_count = process_count + 1
            self.register(process_count)
        password = input('Enter Password')
        re_password = input('Enter Password')
        while password != re_password and process_count < 5:
            print("Please Re-Enter you're passwords and try again")
            process_count = process_count + 1
            self.register(process_count)
        if bank.register(number, password):
            print("Registration Successful")

    def login(self, user_id, psw):
        return bank.verify(user_id, psw)

    def recover(self, user_id=None):
        pass

    def getkey(self):
        pass

