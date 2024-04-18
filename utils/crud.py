
def read(users: list[dict]) -> None:
    for user in users[1:]:
        print(f'Twoj znajomy {user["name"]} opublikował: {user["posts"]}')

def create_user(user:list[dict])->None:
    name: str = input("podaj imie uzytkownika:")
    surname: str = input("podaj nazwisko uzytkownika:")
    posts: int = int(input("podaj liczbe postow:"))
    user: dict = {"name": name, "surname": surname, "posts": posts}
    users.append(user)
def search(users: list[dict]) -> None:
    user_name: str = input("kogo szukasz?:")
    for user in users[1:]:
        if user["name"] == user_name:
            print(f'Twoj znajomy {user["name"]} opublikował: {user["posts"]}')
def remove(users: list[dict]) -> None:
    user_name: str = input("kogo szukasz?:")
    for user in users[1:]:
        if user["name"] == user_name:
            users.remove(user)


