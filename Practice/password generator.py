#modules
from string import ascii_letters, digits, punctuation
from simple_colors import green
from secrets import choice


#textual guide
print("------------------------------------------------------------------")
print("Password Generator".center(66, "-"))
print("------------------------------------------------------------------")
char_count = int(input("Input number of characters (length of password): "))
print("------------------------------------------------------------------")
print("Choose what type of characters you would want in your password.")
print(f'EXAMPLE. {green("a")} = alpha, {green("n")} = number, {green("s")} = symbol.')
print(f'Or you can even make combinations: {green("as")} = alpha+symbol,...etc.')
print("------------------------------------------------------------------")
char_type = input("Your choice: ")
print("------------------------------------------------------------------")


#variables
alpha, numbers, symbols = ascii_letters, digits, punctuation
rating = ['1', '2', '3', '4', '5']
user_experience = ''


#generator
while user_experience == '':
    if char_type == 'a':
        password = ''.join(choice(alpha)for i in range(char_count))
    elif char_type == 'n':
        password = ''.join(choice(numbers)for i in range(char_count))
    elif char_type == 's':
        password = ''.join(choice(symbols)for i in range(char_count))
    elif char_type == ('an' or 'na'):
        password = ''.join(choice(alpha+numbers)for i in range(char_count))
    elif char_type == ('as' or 'sa'):
        password = ''.join(choice(alpha+symbols)for i in range(char_count))
    elif char_type == ('ns' or 'sn'):
        password = ''.join(choice(numbers+symbols)for i in range(char_count))
    elif char_type in 'ansasnsnasan':
        password = ''.join(choice(alpha+numbers+symbols)for i in range(char_count))
    else:
        password = None
        print("Inputed parameters are incorrect. Please try again.")
    #user output
    print("Your password is: ", green(password))
    print(f'If you liked your password press {green("<q>")} to quit.')
    user_experience = input(f'If you would like a different password press {green("<Enter>")}: ')
    if user_experience:
        print("Thank you and goodbye :)")
        exit()
