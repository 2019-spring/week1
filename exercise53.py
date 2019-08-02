print("Game started ...")
alien_color = input("Enter your Alien color: ")
points = 0

if alien_color.lower() == 'green':
    points = points + 5
    print(f"Congratualtions! You just earned 5 points.\n\t Your Total points = {points}")
else:
    print(f"Sorry, no points were rewarded.\n\t Your Total points = {points}")