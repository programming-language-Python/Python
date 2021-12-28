volume = 1000
delivery = 0
col = 0
while volume >= 0:
    delivery += 5
    volume -= delivery
    col += 1
print(col)