'''adding a main command as a placeholder'''
from app_functions import file_handling


# def main():
#     pass

def main():
    resp = file_handling()
    return print(len(resp.data))


if __name__ == '__main__':
    main()
