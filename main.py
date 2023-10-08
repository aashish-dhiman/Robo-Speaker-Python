import os

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1. Created by Aashish")

    while True:
        command = input("What you want me to speak: ")
        if command == "q":
            os.system('espeak -s 150 -v en "bye bye friend"')
            break

        os.system(f'espeak -s 150 -v en "{command}"')
