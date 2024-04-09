class House:
    '''
    This is a stub for a class representing a house that can be used to create objects and evaluate different metrics that we may require in constructing it.
    '''
    num_rooms = 5
    bathrooms = 2

    def cost_evaluation(self, rate):
        # print(house.num_rooms)
        # print(house.bathrooms)
        # pass 
        # Functionality to calculate the costs from the area of the house
        cost =  self * rate
        return cost

house = House()
print(house.num_rooms) # instance referencing class attribute
print(House.num_rooms) # class referrencing class attribute
print(House.cost_evaluation(house.num_rooms, 10)) 
print(House.cost_evaluation(house.bathrooms, 10))


# house.num_rooms = 7
# print(house.num_rooms)
# print(House.num_rooms)

# House.num_rooms = 7
# print(house.num_rooms)
# print(House.num_rooms)
