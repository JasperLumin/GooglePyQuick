
import sys

def hello(name):
    if name == 'Alice' or name == 'alice':
        name = name + '!!!!!'
        print('Hello' , name)
    else:
        name = name + ' you are a stranger !!!! GET OUT OF MY PROGRAM B**CH'
        print(':|' , name)

def main():
    hello(sys.argv[1])


if __name__ == '__main__':
    main()
