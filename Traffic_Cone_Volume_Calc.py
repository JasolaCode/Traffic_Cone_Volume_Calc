# Grab inputs for the room size
room_length = int(input('Enter the length of your room in cm:'))
room_width = int(input('Enter the width of your room in cm:'))
room_height = int(input('Enter the height of your room in cm:'))

# declare cone size (might add variable sizing later for small, medium, large cones)
cone_length = float(36.0)
cone_width = float(36.0)
cone_height = float(70.0)
cone_stack_gap = float(7.6)

def calc_volume(length, width, height): # Calculates Room Volume
    return length * width * height

def calc_stack_attr(height, gap, room_height): #Calculates the stack heaight of cones if higher than ceiling
    stack_height = float(0.0) # Declare for cone stack height
    num_cones = int(0) # use to calculate number of cones in one stack
    while stack_height <= room_height: # While the cone stack hasn't hit the ceiling yet
        if (num_cones == 0): # Calculations for the first cone are different
            if ((height + gap) > room_height):
                return [num_cones, stack_height, room_height]
            else:
                stack_height += height # the first cone creates a stack height of cone_height
        else:
            if ((stack_height + gap) <= room_height): # if the next cone is below the ceiling
                stack_height += gap
            else:
                return [num_cones, stack_height, room_height] # if the next cone will be higher than the ceiling
        num_cones += 1 # when all else checks out... add a cone

    return 'bleh, error'

def stacks_in_room(room_volume, stack_volume): # Calculate the amount of stacks in a room
    return room_volume / stack_volume


room_volume = calc_volume(room_length, room_width, room_height) # Set room volume as variable

print(f'The volume of your room is {room_volume}') # currently using for testing purposes

cone_stack_attr = calc_stack_attr(cone_height, cone_stack_gap, room_height) # Set stack attributes as variable

print(f'The number of cones that can fit in one stack is {cone_stack_attr[0]}. This has a stack height of {cone_stack_attr[1]}, with {round(cone_stack_attr[2] - cone_stack_attr[1], 2)}cm remaining until hitting the ceiling.') # currently using for testing purposescurrently using for testing purposes

result = stacks_in_room(room_volume, calc_volume(cone_length, cone_width, cone_stack_attr[2]))
print (f'the amount of stacks you can fit in the room is {round(result)}')

print(f'total number of cones is {cone_stack_attr[0] * round(result)}')