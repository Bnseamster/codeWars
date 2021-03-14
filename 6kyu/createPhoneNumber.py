def create_phone_number(n):
    for i,num in enumerate(n):
        n[i] = str(num)
    return f'({"".join(n[0:3])}) {"".join(n[3:6])}-{"".join(n[6:])}'