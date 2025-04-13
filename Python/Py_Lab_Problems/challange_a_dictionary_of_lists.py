# challange a dictionary of lists

# This is a dictionary of the rooms. Each entry in the dictionary is keyed by the room number
# Each entry in the dictionary consists of a llist with two items. The subect and the name of the instructor

rooms = {
    103: ["History", "Ms.Jones"],
    201: ["Geology", "Mr. Dilton"],
    107: ["Gym", "Mr. Williams"]
}

room_no = int(input("What room are you standing at? "))
try:
    # infor is assigned to be the list that was retrieved from rooms
    info = rooms[room_no]
    print(
        f"You are at room {room_no}. It's time for {info[0]} taught by {info[1]}.")
except:
    print(f"Check again, are you sure that's the right room?")
