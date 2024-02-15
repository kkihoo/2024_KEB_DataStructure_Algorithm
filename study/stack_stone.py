stack = ["우리집"]
top = 0

top += 1
stack.append("주황")
top += 1
stack.append("초록")
top += 1
stack.append("파랑")
top += 1
stack.append("보라")
top += 1
stack.append("빨강")
top += 1
stack.append("노랑")
top += 1
stack.append("과자집")


print("과자집에 가는길 : ", end="")
for i in range(1, len(stack)):
    if i == len(stack) - 1:
        print(f"{stack[i]}")
    else:
        print(f"{stack[i]}-->", end=" ")


print("우리집에 오는길 : ", end="")
while top >= 0:
    stone_pop = stack.pop()
    if stone_pop == "과자집":
        pass
    elif top == 0:
        print(f"{stone_pop}")
    else:
        print(f"{stone_pop}-->", end=" ")
    top -= 1
