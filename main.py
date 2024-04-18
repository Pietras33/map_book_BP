from utils.crud import read
from models.data import users


if __name__ == '__main__':


    print(f"witaj {users[0]['name']}!")
    while True:
        print("menu:")
        print("0.zakoncz program")
        print("1.pokaz co u znajomych")
        menu_option:str=input("wybierz dostepna funkcje z menu:")
        if menu_option == "0":
            break
        if menu_option == "1":
          read(users)