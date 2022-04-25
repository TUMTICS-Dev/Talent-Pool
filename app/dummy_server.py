from db import DB

def dummy_response():
    return 'Hello'

def main():
    db = DB()
    print(db.get_table())

if __name__ == '__main__':
    main()