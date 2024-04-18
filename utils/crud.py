import main
def read(users: list[dict]) -> None:
    for user in users[1:]:
        print(f'Twoj znajomy {user["name"]} opublikował: {user["posts"]}')

