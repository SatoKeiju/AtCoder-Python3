def main() -> None:
    d, n = map(int, input().split())

    if n == 100:
        print(100**d * (n+1))
    else:
        print(100**d * n)


if __name__ == '__main__':
    main()
