# sssshh. these aren't "real" tests

from character import Character

# Characters can be instantiated with name and avatar

arya = Character("Arya Stark", "arya.png")
jon = Character("Jon Snow", "jon.png")

print(arya.name, arya.avatar)
print(jon.name, jon.avatar)

# After adding 2 items to inventory
# length of inventory should == 2

arya.inventory.append('needle')
arya.inventory.append('mask')

print(len(arya.inventory))


# arya should have a `greet` method
# and when I call with `arya.greet(jon)`, it should return
# "Hello, Jon Snow, I am Ayra Stark. I am awesome."
print(arya.greet(jon))

# arya should have a `greet` method
# and when I call with `arya.greet()`, it should return
# "Hello, I am Ayra Stark. I am awesome."
print(arya.greet())