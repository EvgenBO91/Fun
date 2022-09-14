def Int(x):
    try:
        int(x)
        return True
    except ValueError:
        return False

print(Int(input()))