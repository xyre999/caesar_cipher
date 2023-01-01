
upper_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_alpha = "abcdefghijklmnopqrstuvwxyz"

def main(user_msg):
    
    
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

user_input = input("enter a message:\n > ")

print(main(user_input))