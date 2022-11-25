N = int(input('Enter a triangle width: '))  # Triangle width
for i in range(0, N):
    print(' ' * i + '*' * (N - i))
