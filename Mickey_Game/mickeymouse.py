import time
import functools
from enum import Enum
from pydantic import BaseModel, Field

def print_delay(message, delay=2, prefix=""):
    print(f"{prefix}{message}")
    time.sleep(delay)

# A. Define Game State (mickey)
#  Step 1: Define Enum for Mood 
class Mood(Enum):
    HAPPY = 'happy'
    TIRED = 'tired'
    BLOCKED = "blocked"
    
# Step 2: Define Mickey's state (using Pydantic)

class MickeyState(BaseModel):
    energy: int = Field(default=10, ge=0, le=50)
    fun: int = Field(default=0, ge=0, le=100)
    mood: Mood
    with_friends: list[str]
    pete_angry: bool

mickey = MickeyState(
    energy=10,
    fun=0,
    mood=Mood.HAPPY,
    with_friends=['Minnie', 'Donald', 'Goofy'],
    pete_angry=False
)

    # === DECORATORS ===
    
# B. Purpose: Print what Mickey is doing before and after each action.
#  Decorator 1: Show Action (basic logger)
def show_action(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("\n" + "=" * 40)
        print_delay("Mickey is about to perform an action...", prefix="🎬 ACTION: ")
        result = func(*args, **kwargs)
        action_name = func.__name__.replace('_', ' ').title()
        print_delay(f"Mickey completed: {action_name}")
        print("=" * 40 + "\n")
        return result
    return wrapper

# C. Purpose: Deduct energy if Mickey has enough; block if not.
#  Decorator 2: Energy Check
def requires_energy(min_energy):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if mickey.energy>=min_energy:
                mickey.energy -= min_energy
                print_delay(f"Mickey used {min_energy} energy for function {func.__name__}. (Left: {mickey.energy})")
                return func(*args, **kwargs)
            else:
                print_delay(f"Too tired to perform {func.__name__}!", prefix="🚫 BLOCKED: ")
                mickey.mood = Mood.TIRED
                return None
        return wrapper
    return decorator

#  D. Purpose: Boost Mickey’s fun if Minnie, Goofy or Donald is around.
# Decorator 3: Fun Boost if Friends are Present
def fun_boost(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if any(friend in mickey.with_friends for friend in ['Minnie', 'Goofy', 'Donald']):
            mickey.fun +=1
            mickey.mood = Mood.HAPPY
            mickey.energy += 1  # Boost energy as well
            mickey.energy = min(mickey.energy + 1, 10)
            print_delay(f"Fun boosted to {mickey.fun}! Energy +1 (now {mickey.energy})", prefix="🎉 FUN BOOST: ")
        return result
    return wrapper

#  E. Purpose: Repeat an action multiple times
#  Decorator 4: Repeat Action
def repeat_actions(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwagrs):
            result = None
            for i in range(times):
                print_delay(f"Repeating action {i + 1}/{times}...", prefix="🔁 REPEAT: ")
                result = func(*args, **kwagrs)
            return result
        return wrapper
    return decorator

#  F. urpose: Block actions when Pete is angry
#  Decorator 5: Block If Pete is Angry
def block_if_pete_angry(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if mickey.pete_angry:
            print_delay(f"Mickey can't do {func.__name__}, Pete is angry!", prefix="😠 BLOCKED: ")
            mickey.mood = Mood.BLOCKED
            return None
        return func(*args, **kwargs)
    return wrapper
    
# DEFINE TASKS
# Game Task: ride_rollercoaster() ;  Deduct 4 energy, add 2 fun

@show_action
@requires_energy(4)
def ride_rollercoaster():
    print_delay("Mickey is riding the rollercoaster!", prefix="🎢 TASK: ")
    mickey.fun += 2
    print_delay("Whee! That was fun! (+2 fun)", prefix="✅ RESULT: ")


# Game Task: help_donald() ; Adds fun, mickey is helping donald deduct energy by 3
@show_action
@block_if_pete_angry
@requires_energy(3)
@fun_boost
def help_donald():
    print_delay("Helping Donald fix his boat...", prefix="🛠️ TASK: ")
    mickey.fun += 1
    print_delay("Boat fixed! Donald is happy. (+1 fun)", prefix="✅ RESULT: ")
    
# Game Task: dance_with_minnie() ; Adds fun, mickey is dancing with minnie deduct energy by 2 and use repeat_actions by 2
@show_action
@block_if_pete_angry
@requires_energy(2)
@repeat_actions(2)
@fun_boost
def dance_with_minnie():
    print_delay("Dancing with Minnie 💃", prefix="💃 TASK: ")
    mickey.fun += 3
    print_delay("Such a lovely dance! (+3 fun)", prefix="✅ RESULT: ")
    
    
# Game Task: eat_cheese() ; Adds energy, blocked when Pete is angry
@show_action
@block_if_pete_angry
@requires_energy(1)
def eat_cheese():
    print_delay("Mickey is eating cheese!🧀", prefix="🧀 TASK: ")
    mickey.energy = min(mickey.energy+3, 50)  # Max energy is 50
    print_delay("Yum! Energy restored. (+3 energy)", prefix="✅ RESULT: ")

# Game Task:  trouble_with_pete() ; blocked when Pete is angry
@show_action
@block_if_pete_angry
def trouble_with_pete():
    mickey.pete_angry = True
    mickey.mood = Mood.BLOCKED
    print_delay("Pete is angry! Mickey is blocked.", prefix="⚠️ EVENT: ")
    
# Game Task: resolve_conflict_with_pete ; to calm pete and gain energy
@show_action
@requires_energy(1)
def resolve_conflict_with_pete():
    print_delay("Mickey resolved conflict with pete.", prefix="🤝 TASK: ")
    mickey.pete_angry = False
    mickey.mood = Mood.HAPPY
    print_delay("Pete calmed down. Conflict resolved!", prefix="✅ RESULT: ")
    
    # === STATUS DISPLAY ===
def show_status():
    print("\n" + "=" * 40)
    print("MICKEY'S CURRENT STATUS")
    print("=" * 40)
    print(f"Energy     : {mickey.energy}")
    print(f"Fun        : {mickey.fun}")
    print(f"Mood       : {mickey.mood.value.capitalize()}")
    print(f"Friends    : {', '.join(mickey.with_friends)}")
    print(f"Pete Angry : {'Yes' if mickey.pete_angry else 'No'}")
    print("=" * 40)

# === MAIN GAME LOOP ===
def main():
    print("\n" + "=" * 40)
    print("🎉 Welcome to Mickey's Adventure Game 🎉")
    print("=" * 40)
    
    actions = {
        "1": ride_rollercoaster,
        "2": help_donald,
        "3": dance_with_minnie,
        "4": eat_cheese,
        "5": trouble_with_pete,
        "6": resolve_conflict_with_pete,
        "0": exit
    }

    while True:
        show_status()
        print("\nChoose an action:")
        print("1 - 🎢 Ride Rollercoaster")
        print("2 - 🛠️  Help Donald")
        print("3 - 💃 Dance with Minnie")
        print("4 - 🧀 Eat Cheese")
        print("5 - 😠 Trouble with Pete")
        print("6 - 🤝 Resolve Conflict with Pete")
        print("0 - 🚪 Exit Game")
        choice = input("Enter choice: ").strip()
        action = actions.get(choice)
        if action:
            action()
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    main()