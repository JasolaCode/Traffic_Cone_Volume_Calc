# Grab inputs for the area size
area_size = float(input("Enter the metres squared of your area you'd like covered:"))
area_height = float(input('Enter the height of your area in metres:'))


class Cone:  # declare cone object with size (for small, medium, large cones)

    def __init__(self, name, length, width, height, stack_gap):  # assign values for the object
        self.name = name  # friendly name
        self.length = length  # length of base
        self.width = width  # width of base
        self.height = height  # height of cone
        self.volume = volume(self.length, self.width, self.height)  # volume of cone L x W x H
        self.stack_gap = stack_gap  # when stacked, how much space is between the cones
        self.stack_height = 0  # the height of stacked cones in space
        self.stack_amount = 0  # the amount of stacked cones in space
        self.stack_numofcones = 0  # the number of cones in a stack
        self.stack_volume = 0  # the stack volume

    def __str__(self):  # will run when using print(<cone-object>)
        return f'\n--- {self.name} Dimensions --- \nLength: {self.length*100}cm \nWidth: {self.width*100}cm \nHeight: {self.height*100}cm \nVolume: {round(self.volume, 2)}m^3 \nStack Gap: {self.stack_gap*100}cm \n\n--- {self.name} Stack Dimensions --- \nStack Height: {round(self.stack_height, 2)}m \nNumber of Cones per Stack: {self.stack_numofcones} \nNumber of Stacks: {round(self.stack_amount)} \nStack Volume: {round(self.stack_volume, 2)}m^3 \nTotal Number of {self.name}/s: {round(self.stack_numofcones * self.stack_amount)}\n '
        
    def stack_formula(self, count):  # the formula to calculate stack height of cones
        return (self.stack_gap * count) + (self.height - self.stack_gap)
        
    def stack_add_cone(self, amount):  # add a cone to the stack
        self.stack_numofcones += 1
        
    def stacks_in_area(self, area):  # calculates how many stacks can be in the space
        return (min([(area.length * area.width), (area.size * area.height)]) / (self.length * self.width))//1
        
    def create_stack(self, area):  # all the steps and variable to create a stack of cones
        while self.stack_height <= max([area.width, area.length, area.height]):  # while stack is shorter than the biggest length of the area
                
            if self.volume > area.volume:  # if cone is bigger than area volume
                print(f'1 {self.name} is too big!')
                break
            elif self.stack_formula(self.stack_numofcones + 1) >= max([area.length, area.width, area.height]):  # else if adding a cone is shorter than the greatest length of the area
                self.stack_height = self.stack_formula(self.stack_numofcones)  # set stack height with formula
                self.stack_volume = volume(self.length, self.width, self.stack_height)  # set stack volume
                self.stack_amount = self.stacks_in_area(area)  # use base of cone to calculate
                area.remainder = area.calc_remainder(self)  # calc remaining area not filled by cone
                break
            else:
                self.stack_add_cone(1)  # add a cone
        

class Area:  # declare area object with measurements

    def __init__(self, area_size, area_height):  # assign values for the object
        self.size = area_size  # size from input
        self.width = 7  # width assumed to be 7 metres
        self.length = round((self.size / self.width), 2)  # length calculated from assumed width using size
        self.height = area_height  # size from input
        self.volume = volume(self.length, self.width, self.height)  # using input, calc volume
        self.remainder = 0

    def __str__(self):  # will run when using print(area-object>)
        return f'--- Area Dimensions ---  \nSize: {self.size}m^2 \nLength: {self.length}m^2 \nWidth: {self.width}m^2 \nHeight: {self.height}m^2 \nVolume: {self.volume}m^3 \nRemaining Volume: {round(self.remainder, 2)}m^3'

    def calc_remainder(self, cone):  # used to calculate remaining space in area
        return (cone.volume * cone.stack_amount) / self.volume


volume = lambda length, width, height: length * width * height  # Lambda function, set volume as variable

# stacks_in_area = lambda cone_base_size, area_size: (area_size / cone_base_size)//1

largecone = Cone("Large Cone (STC900R)", 0.36, 0.36, 0.90, 0.076)  # creating cone object LARGE
mediumcone = Cone("Medium Cone (STC700R)", 0.36, 0.36, 0.70, 0.076)  # creating cone object MEDIUM
smallcone = Cone("Small Cone (STC450R)", 0.25, 0.25, 0.45, 0.046)  # creating cone object SMALL
area = Area(area_size, area_height)

largecone.create_stack(area)  # performs all logic for the cone
mediumcone.create_stack(area)  # performs all logic for the cone
smallcone.create_stack(area)  # performs all logic for the cone

print(largecone)  # print all info of LARGE cone and stack
print(mediumcone)  # print all info of MEDIUM cone and stack
print(smallcone)  # print all info of SMALL cone and stack
print(area)  # print all info of area
