def main():
    print('\nWelcome to the email slicer!')
    print("To exit the loop you can enter 'e'")
    # global email 
    email = input("Enter you email address here:")
    if email =='e':
        print('The program is ended.')
        exit()
    (user,domain) = email.split('@')
    (domain,extention) = domain.split('.')
    print("username: ",user)
    print("domain: ",domain)
    print("extention: ",extention)
    
    
while True:    
    main()
    # ex = input('Enter "e" for exit, if not enter any character: ') 
    # if email == 'e':
    #     exit()
    
   