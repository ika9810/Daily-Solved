import sys
input = sys.stdin.readline
def is_winning_ticket(serial):
    for i in range(len(serial) - 3):
        if serial[i] != '2':
            continue
        for j in range(i + 1, len(serial) - 2):
            if serial[j] != '0':
                continue
            for k in range(j + 1, len(serial) - 1):
                if serial[k] != '2':
                    continue
                for l in range(k + 1, len(serial)):
                    if serial[l] != '3':
                        continue
                    return True
    return False

n = int(input())
count = 0
for i in range(1, n + 1):
    if is_winning_ticket(str(i)):
        count += 1
print(count)