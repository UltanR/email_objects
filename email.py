#An Email Simulation

class Email():

    has_been_read = False
    is_spam = False

    def __init__(self, email_contents, from_address):

        self.email_contents = email_contents
        self.from_address = from_address
    

    def mark_as_read(self):

        self.has_been_read = True
    

    def mark_as_spam(self):

        self.is_spam = True


inbox = []

def add_email(email_contents, from_address):    # creates instance of Email class and adds to inbox

    email = Email(email_contents, from_address)
    inbox.append(email)


def operate_email():    # allows user to select email as long as there are more than 0 emails

    while num_emails != 0:

        print()

        try:
            choice = int(input("What number corresponds with the email you would like to read: "))
            get_email(choice-1) # calls email selected by user
            break

        except ValueError:
            print("That was not a number corresponding with one of the emails. Try again.")


def delete(email):

    inbox.pop(email)    # removes email from inbox


def get_count():

    return len(inbox)


def get_email(i):

    inbox[i].mark_as_read()

    print(f"From address: {inbox[i].from_address}") # displays email contents and address
    print(f"Email contents: {inbox[i].email_contents}")

    if inbox[i].is_spam == True:    # displays that email is spam
        print("Email is marked spam")

    remove_yn = input("Delete email (y/n): ")   # user can delete email
    if remove_yn == "y":
        delete(i)
    
    elif inbox[i].is_spam == False:   # email can be marked spam
        spam_yn = input("Mark as spam (y/n): ")
        if spam_yn == "y":
            inbox[i].mark_as_spam()


def display_emails():   # displays an numbered list of emails

    count = 0

    for email in inbox:

        count += 1

        print(f"{count}. From: {email.from_address}")
    
    operate_email()


def get_unread_emails():    # displays a numbered list of unread emails

    count = 0
    count_unread = 0

    for email in inbox:

        count += 1

        if email.has_been_read == False:

            count_unread += 1

            print(f"{count}. From: {email.from_address}")
    
    if count_unread != 0:

        operate_email()
            


def get_spam_emails():  # displays a numbered list of spam emails

    count = 0
    count_spam = 0

    for email in inbox:

        count += 1

        if email.is_spam == True:

            count_spam += 1

            print(f"{count}. {email.from_address}")
    
    if count_spam != 0:

        operate_email()


user_choice = ""

while user_choice != "quit":    # program ends when user types quit

    user_choice = input("What would you like to do - read/send/quit? ")
    print()

    if user_choice == "read":
        
        num_emails = get_count()
        print(f"Number of emails: {num_emails}")    # shows how many emails in inbox
        print()
        
        while (num_emails != 0) and (user_choice != "all") and (user_choice != "spam") and (user_choice != "unread"):

            user_choice = input("Read all or read spam (all/unread/spam): ")

            if user_choice == "all":
                
                display_emails()

            elif user_choice == "unread":

                get_unread_emails()
        
            elif user_choice == "spam":

                get_spam_emails()
            
            else:

                print("Oops - incorrect input")
            
            print()

    elif user_choice == "send": # adds email to inbox using user values to create email object
        
        email_contents = input("Enter the contents of the email: ")
        from_address = input("Enter the email address: ")
        add_email(email_contents, from_address)
        print("Email confirmed")
        print()

    elif user_choice == "quit":
        print("Goodbye")

    else:
        print("Oops - incorrect input")

    print()