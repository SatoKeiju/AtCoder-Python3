def main():
    a, b = map(int, input().split())
    print('Yes' if a % 2 != 0 and b % 2 != 0 else 'No')


if __name__ == '__main__':
    main()
