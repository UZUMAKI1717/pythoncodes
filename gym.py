import time

import random

class user:

    def __init__(self, name, age, weight):

        self.name = name
        self.age = age
        self.weight = weight

        self.workout_history = []

    def add_workout(self, workout):

        self.workout = history.append(workout)

    def show_workout(self):

        if not self.workout_history:
            print("No workout recorded yet.")

        else:
            print("workout history:")

            for workout in self.workout_history:
                print(workout)


class workout:

    def __init__(self, name, duration, difficulty):

        self.name = name
        self.duration = duration
        self.difficulty = difficulty

    def __str__(self):
        return f "{self.name} ({self.duration} minutes) - Difficulty: {self.difficulty}"

class workoutplan:

    def __inti__(self, user):

        self.user = user

        self.exercies = []

    def add_exercis(self, name, duration, difficulty):

        self.exercises.append(worktout(name, duration, difficulty))

    def show_plan(self):

        if not self.exercise:

            print("No exercises in your plan.")

        else:

            print("Your workout plan:")

            for exercise in self.exercises:

                print(exercise)

class gymApp:

    def __init__(self):

        self.user = None

    def register_user(self):

        name = input("Enter your name:")

        age = int(input("Enter your age:"))

        weight = float(input("Enter your weight(kg):"))

        self.user = user (name, age, weight)

        print(f"welcome, {self.user.name}! your gym journey begins now!\n")

    def generate_workout(self):

        exercise = [

            ("Push-ups", 10, "Medium"),

            ("Squats", 12, "Easy"),

            ("Burpees", 15, "Hard"),

            ("PLank", 60, "Medium"),

            ("Lunges", 12, "Easy"),

            ("Jumping Jacks", 7, "Easy")
        ]

        chosen = random.choice(exercise)

    print(f"AI suggest:{Chosen[0]}({chosen[1]} minutes) - Difficulty: {chosen[27]}")

    self.user.add_workout(chose[0])

    def rest_timer(self, seconds):

        print(f"Resting for {second} seconds...")

        for i in range(seconds, 0, -1):

            print(i, end="", flush=True)

            time.sleep(1)

        print("\n Rest over! Get back to your workout!")


    def menu(self):
        
        while True:

            print("\n Gym workout App")

            print("1. Register user")

            print("2. Generate workout")

            print("3. Get AI workout suggestion")

            print("4. Start rest timer")

            print("5. Exit")

            choice = input("Enter your choice:")

            if choice == "1":

                self.register_user()

            elif choice == "2":

                if self.user:

                    self.user.show_history()

                else:

                    print("No use found please register first.")

            elif choice =="3":

                if self.user:

                    self.generat_workout()

                else:

                    print("No user found please register first.")

            elif choice == "4":

                second = int(input("Enter rest time in seconnds:"))

                self.rest_timer(second)

            elif choice == "5":

                print("Exiting Gym workout App stay fit!")

                break:

            else:

                print("Invalid choice! please try again.")

        if __name__ == "__main__":

            app = gymApp()

            app.register_user()

            app.menu()


