import logging

logging.basicConfig(filename='day-8.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(name)s - %(message)s'
) #formating ready for cloudwatch

class Dishes:
    def __init__(self, breakfast, lunch, dinner):
        self.breakfast = breakfast
        self.lunch = lunch
        self.dinner = dinner
        logging.info("Dishes instance created with breakfast: %s, lunch: %s, dinner: %s", breakfast, lunch, dinner)

    def total_calories(self):
        total = self.breakfast + self.lunch + self.dinner
        logging.info("Total calories calculated: %d", total)
        return total
    
day_1_dishes = Dishes(500, 700, 800)
day_2_dishes = Dishes(600, 600, 900)
day_3_dishes = Dishes(400, 800, 700)

print("Day 1 Total Calories:", day_1_dishes.total_calories())
print("Day 2 Total Calories:", day_2_dishes.total_calories())
print("Day 3 Total Calories:", day_3_dishes.total_calories())
        
