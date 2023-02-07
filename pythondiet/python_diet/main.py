import os.path
import time
from sqlmain import *
from datetime import *
from sqlite3 import *




class Person():
    def __init__(self, dietary, weight, height, age, sex, phys_activity):
        self.__Dietary = dietary #3 and 6
        self.__Weight = weight
        self.__Height = height
        self.__Age = age
        self.__Sex = sex # "1" = Male; "2" = Female
        self.__Phys_activity = phys_activity
        self.daynutr = 0
        self.weeknutr = 0

    def sex_calc(self, Sex):
        if self.__Sex == "Male" or self.__Sex == "male":
            self.__Sex = 1
        elif self.__Sex == "Female" or self.__Sex == "female":
            self.__Sex = 2
    def phys_act_calc(self, Psys_activity):
        match Psys_activity:
            case 1:
                self.__Phys_activity = 1.2
            case 2:
                self.__Phys_activity = 1.375
            case 3:
                self.__Phys_activity = 1.55
            case 4:
                self.__Phys_activity = 1.725
            case 5:
                self.__Phys_activity = 1.9

    def calc(self, Dietary, Weight, Height, Age, Sex, Phys_activity):
        if self.__Sex == 1:
            self.__nutritional_intake = (10 * self.__Weight) + (6.25 * self.__Height) - (5 * self.__Age) + 5
            self.water_int = self.__Weight * 35
        else:
            self.__nutritional_intake = (10 * self.__Weight) + (6.25 * self.__Height) - (5 * self.__Age) - 161
            self.water_int = self.__Weight * 21
        self.true_nutr_int = self.__nutritional_intake/self.__Phys_activity

    def write_info(self):
        return (self.__Dietary, self.__Weight, self.__Height, self.__Age, self.__Sex, self.__Phys_activity, self.true_nutr_int, self.water_int, self.daynutr, self.weeknutr)

class Meal():
    def __init__(self, account, id_meal, amount, when_added, time_os):
        self.id_meal = id_meal
        self.amount = amount
        bb = datetime.today()
        if (bb - time_os).days <= 7:
            account.weeknutr += int(self.amount)
        if bb == time_os:
            account.daynutr += int(self.amount)
    def get_info(self):
        return(self.id_meal, self.amount)

def first_step(dietary, weight, height, age, sex, phys_activity):

    account = Person(dietary, weight, height, age, sex, phys_activity)
    account.sex_calc(sex)
    account.phys_act_calc(phys_activity)
    account.calc(dietary, weight, height, age, sex, phys_activity)
    return account

#def End(account):

    #data = open("C:/Users/Варвара/PycharmProjects/pythondiet/pythondiet/info_account.txt", "w+")
    #a = str(account.write_info())
    #data.write(a)
    #data.close()

def AddMeal(account):

    #id
    print("Please enter name of the meal: ")
    name = str(input())
    print("Please enter nutritions value: ")
    nutritions = int(input())
    time = datetime.today()
    Meal1 = Meal(account, name, nutritions, str(time), time)
    #datameal = open("C:/Users/Варвара/PycharmProjects/pythondiet/pythondiet/info_meals.txt", "a")
    #datameal.write(name + ", ")
    #datameal.write(str(nutritions) + ", ")
    #datameal.write(str(time) + "\n")
    #datameal.close()


def ReadMeal(account):

    if os.path.getsize("C:/Users/Варвара/PycharmProjects/pythondiet/pythondiet/info_meals.txt") == 0:
        return 0
    else:
        meals = []
        datameal = open("C:/Users/Варвара/PycharmProjects/pythondiet/pythondiet/info_meals.txt", "r")
        a = datameal.readline()
        name, nutritions, time = a.split(", ")
        time_now = datetime.today()
        meals.append(Meal(account, name, nutritions, time, time_now))
        b = True
        while b:
            a = datameal.readline()
            if not a:
                b = False
            else:
                name, nutritions, time = a.split(", ")
                meals.append(Meal(account, name, nutritions, time, time_now))

        datameal.close()
    return meals


def WeekStatist(account, meals):

    if len(meals) != 0:
        for i in range(len(meals)):
            print(meals[i].get_info())

        print("Taken: ", account.daynutr)
        print("More: ", round(account.true_nutr_int-account.daynutr))
        print("Your nutritional intake: ", account.true_nutr_int)
        print("Taken om this week: ", account.weeknutr)
    else:
        print("Taken: ", account.daynutr)
        print("More: ", round(account.true_nutr_int-account.daynutr))
        print("Your nutritional intake: ", account.true_nutr_int)
        print("Taken on this week: ", account.weeknutr)

#def ShowMeals():
    #pass

def Rewrite_Acc_Info():

    data = open("C:/Users/Варвара/PycharmProjects/pythondiet/pythondiet/info_account.txt", "w+")
    First_Meet()

def First_Meet():

    print("Please, enter how many times per day you usually take a meal (3 or 6): ")
    dietary = int(input())

    print("Please, enter your weight: ")
    weight = int(input())

    print("Please, enter your height: ")
    height = int(input())

    print("Please, enter your age: ")
    age = int(input())

    print("Please, enter your sex (female or male): ")
    sex = input()

    while not (sex == "Female" or sex == "female" or sex == "Male" or sex == "male"):
        print("Error. Try again.")
        sex = str(input())

    print("Please, enter option, which describes your physical activity")
    print("1. No physical activity at all")
    print("2. I do sports 1-3 times a week")
    print("3. I do sports 3-5 times a week")
    print("4. I do sports 6-7 times a week")
    print("5. Sport is my work"
          ": ")
    phys_activity = int(input())

    main_account = first_step(dietary, weight, height, age, sex, phys_activity)

    return main_account

def Menu():
    choice = 0
    while choice != 4:
        print("Menu")
        print("Please enter number of option")
        print("1. Add meal")
        print("2. Print info about this week")
        print("3. Rewrite info")
        print("4. Exit")
        choice = int(input())
        match choice:
            case 1:
                AddMeal(main_account)
                Menu()
                break
            case 2:
                WeekStatist(main_account, meals)
                Menu()
                break
            case 3:
                Rewrite_Acc_Info()
            case 4:
                End(main_account)
                break

Start()
if os.path.getsize("C:/Users/Варвара/PycharmProjects/pythondiet/pythondiet/info_account.txt") == 0:
    main_account = First_Meet()
else:
    data = open("C:/Users/Варвара/PycharmProjects/pythondiet/pythondiet/info_account.txt", "r")
    a = data.readline().replace("'", "").replace("(", "").replace(")", "")
    dietary, weight, height, age, sex, phys_activity, true_nutr_int, water_int = (a.split(","))
    dietary = int(dietary)
    weight = int(weight)
    height = int(height)
    age = int(age)
    sex = int(sex)
    phys_activity = float(phys_activity)
    true_nutr_int = float(true_nutr_int)
    water_int = int(water_int)
    data.close()
    main_account = first_step(dietary, weight, height, age, sex, phys_activity)

meals = ReadMeal(main_account)
Menu()
End(meals, main_account)