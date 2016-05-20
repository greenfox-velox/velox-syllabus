ab = 123
credits = 100
is_bonus = False

# 1
if not is_bonus:
    if credits > 50:
        ab -= 2
    else:
        ab -= 1


# 2
if is_bonus:
    pass
elif credits > 50:
    ab -= 2
else:
    ab -= 1


