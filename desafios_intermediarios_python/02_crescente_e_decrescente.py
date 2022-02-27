x, y = map(int, input().split())
while (  x != y    ):
    floor = min(x, y)
    top = max(x, y)
    if (  x < y  ):
        print("Crescente")
    elif (  x > y  ):
        print("Decrescente")
    x, y = map(int, input().split())