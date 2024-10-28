from getter import Speech  
from sender import give_commands   

def main():
    print("Say 'stop' to end the conversation.")
    
    while True:
         
        text = Speech()
        
         
        if text.lower() == 'stop':
            print("Ending the conversation.")
            break

         
        give_commands(text)

if __name__ == "__main__":
    main()
