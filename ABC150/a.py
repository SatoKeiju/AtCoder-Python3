def main():
    k, x = map(int, input().split())

    print('Yes' if k * 500 >= x else 'No')


if __name__ == '__main__':
    main()
