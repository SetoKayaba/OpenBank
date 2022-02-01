# OPEN BANK's MAIN SCRIPT. SERVES AS A BACKBONE FOR BACK-END PROCESSING AND FLOW-EXECUTION CONTROL


# Setting up Imports and file system Dependencies
import Authenticator as auth

preferences = open("preferences").read()


class Session:  # Session Class

    session_status = -1  # Current Session status 0 for UnActive, 1 for Active and -1 for new

    def __init__(self):  # function to initialize with the Session Class
        if self.session_status is -1:  # condition to execute connect function
            self.user_options()
        else:  # if user data is not provided execute options function with a param of 1
            self.user_options()

    def connect(self, user_id, password):
        self.authenticate(user_id, password)

    def login(self):
        user_id = input("Username:")
        password = input("\t\t\tpassword:")
        self.connect(user_id, password)

    def user_options(self, choice=None):  # Defining a function which returns a session variable
        print("User Options Menu:\n")
        if choice == -1:
            print("To Login to an existing account: select 1\n"
                  "To Register a New Account: select 2\n"
                  "To Recover an Account: select 3")
            self.login()
        if choice == 1:  # Login
            self.login()
        elif choice == 2:  # Registration
            auth.UserOptions.register()
        elif choice == 3:  # Recovery
            auth.UserOptions.recover()
        else:
            self.user_options(-1)

    # sets _oAuthToken equal to the token
    def authenticate(self, user_id, password):
        oAuthToken = None
        user_data = auth.UserOptions
        user_data.login(user_id, password)
        if user_data.status is True:
            oAuthToken = auth.user_data.getkey()
            self.session_status = 1
            oAuthToken = user_data.getkey()
        elif user_data.status is False:
            self.session_status = 0
            self.user_options()
        else:
            
        # Establish a connection
        auth.dataflow(oAuthToken)


# CLI Implementation for Quick Testing
if __name__ == '__main__':
    print("Welcome to OPEN BANK's Command Line Interface!")
    if len(preferences) <= 5:
        decision = input("Would you like to make a new account? Y/N")
        if decision.upper() == 'Y':
            loginStep = 2
        else:
            loginStep = 1

    else:
        LoginStep = input("To Login to existing account: 1\nTo Register a New Account: 2\To nRecover an Account: 3")
