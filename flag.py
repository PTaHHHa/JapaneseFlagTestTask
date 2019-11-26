import argparse


def flag(N):
    if N % 2 == 0:

        for i in range(2, N, 2):
            x = i // 2 - 1
            y = x + 1

        border = '#' * (3 * N + 2)
        blank = "#" + (' ' * (3 * N)) + '#'
        if N == 2:
            asterisk_line = "#" + (' ' * int(N)) + ('*' * 2) + (' ' * int(N)) + "#"
        else:
            asterisk_line = "#" + (' ' * int(N + y)) + ('*' * 2) + (' ' * int(N + y)) + "#"
        ascii_line = "#" + (' ' * N) + "*" + ('o' * int(N - 2)) + "*" + (' ' * N) + "#"
        print('{}{}{}{}{}{}{}'.format(border + '\n',
                                      (blank + '\n') * int(N / 2),
                                      (asterisk_line + '\n'),
                                      (ascii_line + '\n') * int(N - 2),
                                      (asterisk_line + '\n'),
                                      (blank + '\n') * int(N / 2),
                                      border))
    else:
        raise argparse.ArgumentError(None, "The N you've entered is not even")


i = input("Input N: ")
flag(int(i))
