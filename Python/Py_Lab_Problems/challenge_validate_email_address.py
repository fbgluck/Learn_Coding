# challenge_validate_email_address
'''
For this exercise, we are going to assume that the rules for a valid email are:
* A string of 1 to n alphanumeric characters, 
* followed by one and only one  @, 
* followed by a string of 1 to n alphanumeric characters, 
* followed by one or more domains each of which begin with a . and are in a list of valid domains
'''
continue_program_flag = True  # Used to continue program based on user input
check_was_valid = True   # flag to determine if a check on the address has failed
# these are a list of the valid domains
accepted_suffix = ["com", "org", "edu", "gov"]

# global dot_position # Position of the dot in the address
# global at_sign_position # Position of the @ in the address
# global email_recipient # recipient portion of the address
# global email_domain_recipient # domain of the recipient


def split_address():  # Inputs from the user and picks the necessary pieces used in validation from the input
    print(f"Validate An Email Address")
    print(40*'-')
    global email_address
    email_address = input(
        "What is the email address you would like to validate >>> ")

    global dot_position
    dot_position = email_address.find(".")  # get the position of the first dot

    global at_sign_position
    # get the position of the first  @ sign which is needed to find the email recipent
    at_sign_position = email_address.find("@")

    global at_sign_count
    at_sign_count = email_address.count("@")

    global email_recipient
    # Get the substring that is the email recipient
    email_recipient = email_address[0:at_sign_position]

    global email_domain_recipient
    # get the string after the first .  which is the full domain name
    email_domain_recipient = email_address[dot_position:]


# First time through
print("Program starting...")
split_address()

while continue_program_flag:
    check_was_valid = True

    # Check #1: validate that there is one and only one @ in the email address
    if at_sign_count != 1:
        if at_sign_count == 0:
            print(f"Validation Failed: No @ sign was included in the email ")
            check_was_valid = False
        if at_sign_count > 1:
            print(
                f"Validation failed: An email address must not more than one '@'. The email address you entered has {at_sign_count}.")
            check_was_valid = False
    else:  # there is only one @ so we can split the list
        # returns a list with the recipient name as the first entry and the rest of the string as the rest
        split_list = email_address.split('@')
        # DEBUG: print(f"Split list is: {split_list}")

    # Check #2: check to see that there is at least one . in the email address
    if dot_position == 0 and check_was_valid:
        print(f"Validation failed. No  '.' was found in the address")
        check_was_valid = False
    # Check #3: check that the suffix (last 4 characters) are in the accepted suffix list)
    else:
        if check_was_valid:
            # we found at least one dot so we can split the domains into a list
            domain_list = split_list[1].split('.')
            '''  ## DEBUG
            print(f"Domain list is: {domain_list}")
            for i in range (1,len(domain_list)):
                if domain_list[i] not in accepted_suffix:
                    print(f"Validation failed. Domain {domain_list[i]} was not found in the list of accepted domains")
                    check_was_valid=False
            
            ### DEBUG END 
            '''

    # Check #4: check to see that the items before @ are alphanumeric
    if not (email_recipient.lower().isalnum()) and check_was_valid:
        print(
            f"Validation failed. Email recipient must be alphanumeric. Your recipient was {email_recipient}")
        check_was_valid = False

    # Check #5: check to see that the characters between @ and . are alphanumeric
    if not ((email_domain_recipient.lower()[1:]).isalnum()) and check_was_valid:
        print(
            f"Validation failed. Email domain must be alphanumeric. Your domain was {email_domain_recipient}")
        check_was_valid = False

    if check_was_valid:
        print(f">> The Email address {email_address} is a valid address")
        print(f">> The recipient's name is: {email_recipient}")
        print(
            f">> A single '@' was correctly included at character position {at_sign_position+1}")
        print(f">> You are sending email to an address at: {domain_list[0]}")
        print(
            f">> A '.' was correctly included at character position {dot_position+1} as the first character of the domain suffix")
        print(
            f">> The complete domain suffix you entered was: {email_address[dot_position:]}")

    else:
        print(
            f"The Email address {email_address} is not a valid email address")

    print(40*'-')  # output seperator

    if (input("Would you line to enter another email address to check? (y or n) ").lower()) != "y":
        continue_program_flag = False
    else:
        print(40*'-')  # finish up the previous results
        split_address()  # Get another address then check

# End program procedures
print(30*'-')  # finish up the previous results
print(f"Thanks for using the validator")
