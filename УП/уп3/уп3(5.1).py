current_health = 500
attack = 80
second = 0
while current_health > 0:
    current_health -= attack
    second += 1
print(second)