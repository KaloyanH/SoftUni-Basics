command = input()

total_steps = 0
goal = 10000
goal_is_reached = False
difference = 0

while command != "Going home":
    current_steps = int(command)
    total_steps += current_steps
    if total_steps > goal:
        difference = total_steps - goal
        goal_is_reached = True
        break
    command = input()

if command == "Going home":
    current_steps = int(input())
    total_steps += current_steps
    if total_steps > goal:
        difference = total_steps - goal
        goal_is_reached = True
    else:
        difference = goal - total_steps
        goal_is_reached = False

if goal_is_reached:
    print("Goal reached! Good job!")
    print(f"{difference} steps over the goal!")
else:
    print(f"{difference} more steps to reach goal.")
