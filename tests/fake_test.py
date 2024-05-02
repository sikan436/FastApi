room_guest_pairs = {339: 'Sue', 238: 'Eli'}

room_no = int(input('What is your name?\n'))
print(room_guest_pairs[room_no])
room_guest_pairs.pop(room_no)
print('Remaining pairs:')
print(room_guest_pairs)