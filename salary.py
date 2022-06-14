number_of_tabs = int(input())
salary = float(input())

facebook_fine = 150
instagram_fine = 100
reddit_fine = 50


for _ in range(1, number_of_tabs + 1):
    name_of_tab = input()
    if name_of_tab == "Facebook":
        salary -= facebook_fine
    elif name_of_tab == "Instagram":
        salary -= instagram_fine
    elif name_of_tab == "Reddit":
        salary -= reddit_fine

if salary <= 0:
    print("You have lost your salary.")

else:
    print(int(salary))



