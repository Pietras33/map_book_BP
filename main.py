from utils.crud import read, create_user
from models.data import users


if __name__ == '__main__':


    print(f"witaj {users[0]['name']}!")
    while True:
        print("menu:")
        print("0.zakoncz program")
        print("1.pokaz co u znajomych")
        print("2.dodaj znajomego")
        menu_option:str=input("wybierz dostepna funkcje z menu:")
        if menu_option == "0":
            break
        if menu_option == "1":
          read(users)
        if menu_option == "2":
            create_user(users)
