guests = ["john","akmal", "said", "lenur"]
invitation = ",\n happy to invite you to my dinner party at our house.\n"

print(guests[0].title() + invitation)
print(guests[1].title() + invitation)
print(guests[2].title() + invitation)
print(guests[3].title() + invitation)

# Add a print statement at the
# end of your program stating the name of the guest who can’t make it.
guests_couldnot_come = []
guests_couldnot_come.append(guests.pop(0))

guests.insert(0, "Mark")

print("Some people can not come.\n\tPeople can not come for dinner: " + guests_couldnot_come[0])

print(guests[0].title() + invitation)
print(guests[1].title() + invitation)
print(guests[2].title() + invitation)
print(guests[3].title() + invitation)

for guest in guests:
    print(guest.title() + invitation)


number_of_guests = len(guests)
print(f"We will be {number_of_guests} people tonight")
print(f"We will be {len(guests)} people tonight")