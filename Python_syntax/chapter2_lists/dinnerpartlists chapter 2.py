friends = ["Luke.","Clare."]
message = f"Hello {friends[0].title()} how are you doing today?\n\tWould you like to know more?"
print(message)
friends.insert(1, "Snickers")
print(friends)
friends.append("Snacks")
print(friends)
del friends[3]
print(friends)
popfriends = friends.pop()
print(popfriends)
nomoresnax = f"I removed {popfriends.title()} from my list. Sorry {popfriends.title()}"
print(nomoresnax)

dinnerparty = ["Nikola tesla", "Snickers", "Clare"]
invite = f"I'm having dinner tomorrow {dinnerparty[0].title()}, {dinnerparty[1].title()}, {dinnerparty[2].title()} \nWould you care to come?"
print(invite)
cancel = f"Oh dear, {dinnerparty[2].title()} cant come!"
print (cancel)
del dinnerparty[2]
dinnerparty.append("Snickers2")
newinvite = f"Okay so, {dinnerparty[0].title()}, {dinnerparty[1].title()}, {dinnerparty[2].title()}, you all still have to come."
print (newinvite)
dinnerparty.insert(0, "Snarks")
dinnerparty.insert(1, "Snorks")
dinnerparty.append("Snarkels")
print(dinnerparty)
removal = dinnerparty.pop()
sorry = f"Hey {dinnerparty.pop()} Sorry you cant come though."
print(sorry)
removal = dinnerparty.pop()
sorry = f"Hey {dinnerparty.pop()} Sorry you cant come though."
print(sorry)
print(dinnerparty)
itsstillon = f"Hey {dinnerparty[0]} the party is still on so!"
print(itsstillon)
itsstillon = f"Hey {dinnerparty[1]} the party is still on so!"
print(itsstillon)
del dinnerparty[0:2]
print(dinnerparty)

test = ["Test1", "Test2"]
print(test)

test3 = f"Hey {test[0:2]}"
print(test3)