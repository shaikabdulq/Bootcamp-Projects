# 6. Hard Criteria

# ASCII of 1st - 0th letter != ASCII of 2nd - 1st letter and so on
def check_consistency(password):
    for i in range(len(password) - 2):
        if ord(password[i]) - ord(password[i + 1]) == ord(password[i + 1]) - ord(password[i + 2]):
            if abs(ord(password[i]) - ord(password[i + 1])) < 2:
                return False
    return True
