# initialize both rooms with 0 indication both rooms contain dirt
# 1 is for clean
room_A = 0
room_B = 0

room = raw_input("Enter the room: ")

# use for loop to simultaneously switch between rooms A and B
for i in xrange(0,2):
    if room == 'a':
        room = 'b'
        if room_A == 0:
            print("\n --Room A is Dirty-- \n")
            print("Cleaning Room A \n")
            room_A = 1
        if room_A == 1:
            print("Room A is Clean \n")
            print("Move to Room B \n")
    if room == 'b':
        room = 'a'
        if room_B == 0:
            print("\n --Room B is Dirty-- \n")
            print("Cleaning Room B \n")
            room_B = 1
        if room_B == 1:
            print("Room B is Clean \n")
            print("Move to Room A \n")


