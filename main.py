
upper_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_alpha = "abcdefghijklmnopqrstuvwxyz"

def encrypte(user_msg):
    
    while True:
        try:
            key = int(input('enter a key (0 to 26):\n > '))
            if key >= 0 and key <= 26:
                break
            else:
                print("unvalid key!")
                continue
        except:
            print("unvalid key!")
        
    msg_len = len(user_msg)
    encrypted_msg = ""
    ascii_calc = 0
    i = 0
    while i < msg_len and user_msg[i] != '\0':
        
        if user_msg[i] >= 'A' and user_msg[i] <= 'Z':
            
            ascii_calc = upper_alpha.index(user_msg[i]) + key
            
            if ascii_calc >= 26:
                ascii_calc -= 26
            encrypted_msg += upper_alpha[ascii_calc]
               
        elif user_msg[i] >= 'a' and user_msg[i] <= 'z':
            
            ascii_calc = lower_alpha.index(user_msg[i]) + key
            
            if ascii_calc >= 26:
                ascii_calc -= 26
            encrypted_msg += lower_alpha[ascii_calc]
           
        else:
            encrypted_msg += user_msg[i]
        
        i += 1
    
    return(encrypted_msg)

def decrypte(encrypted_msg):

    while True:
        try:
            key = int(input('enter a key (0 to 26):\n > '))
            if key >= 0 and key <= 26:
                break
            else:
                print("unvalid key!")
                continue
        except:
            print("unvalid key!")
            
    msg_len = len(encrypted_msg)
    decrypted_msg = ""
    ascii_calc = 0
    i = 0 
    
    while i < msg_len and encrypted_msg[i] != '\0':
        
        if encrypted_msg[i] >= 'A' and encrypted_msg[i] <= 'Z':
            
            ascii_calc = upper_alpha.index(encrypted_msg[i]) - key
            
            if ascii_calc < 0:
                ascii_calc += 26
            decrypted_msg += upper_alpha[ascii_calc]

        elif encrypted_msg[i] >= 'a' and encrypted_msg[i] <= 'z':
            
            ascii_calc = lower_alpha.index(encrypted_msg[i]) - key
            
            if ascii_calc < 0:
                ascii_calc += 26
            decrypted_msg += lower_alpha[ascii_calc]
           
        else:
            decrypted_msg += encrypted_msg[i]
            
        i += 1
    
    return (decrypted_msg)


def user_input():
    user_deci = input('Do you want to (e)ncrypt or (d)ecrypt?\n > ')

    if user_deci.lower() == 'e':
        user_input = input("enter the message to encrypte:\n > ")
        print(encrypte(user_input))
    elif user_deci.lower() == 'd':
        user_input = input("enter the message to decrypte:\n > ")
        print(decrypte(user_input))
        
user_input()