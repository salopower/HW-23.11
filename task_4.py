N = int(input('Enter a triangle width: '))  # Triangle width
for i in range(N, 0, -1):
    print(' ' * i + '*' * ((N+1) - i))
