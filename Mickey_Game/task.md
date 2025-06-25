# 🏰 Mickey's Magical Park Adventure — Task List

## 📌 PART 1: Basic Game Setup

- [ ] Create a Mickey dictionary with keys: `"energy": 10`, `"fun": 5`, `"mood": "happy"`
- [ ] Bonus: Add `"with_friends": ["Donald", "Goofy"]`, `"pete_angry": False`

### 🎨 Decorator 1: `@show_action`
- [ ] Print BEFORE and AFTER messages using the function name (e.g., `dance_with_minnie`)
- [ ] Use `func.__name__.replace("_", " ")` for clean formatting

---

## 📌 PART 2: Energy-Based Actions

### 🎯 Decorator 2: `@requires_energy(min_energy)`
- [ ] If Mickey has enough energy, allow the action and deduct it
- [ ] If not, print `"Too tired to do that!"`

### ✨ Game Task: `ride_rollercoaster()`
- [ ] Deduct 4 energy, add 2 fun
- [ ] Use `@show_action` and `@requires_energy(4)`

---

## 📌 PART 3: Friends, Mood, and Fun

### 👫 Decorator 3: `@fun_meter_boost`
- [ ] If Mickey is with "Donald" or "Goofy", add extra fun points

### Game Task: `help_donald()`
- [ ] Adds fun, uses `@fun_meter_boost`, `@show_action`

---

## 📌 PART 4: Repeating Cute Actions

### 🎉 Decorator 4: `@repeat(times)`
- [ ] Run the action `times` number of times (e.g., Mickey tail wag)

### Game Task: `dance_with_minnie()`
- [ ] Use `@show_action` and `@repeat(3)`

---

## 📌 PART 5: Blocking and Cooldowns

### 🚫 Decorator 5: `@block_if_angry`
- [ ] If `pete_angry` is True, block the action with a warning

### Game Task: `eat_cheese()`
- [ ] Adds energy, blocked when Pete is angry

---

## 🧪 BONUS EXTENSIONS

- [ ] Turn `@show_action` into a **class-based decorator**
- [ ] Implement `@cooldown(n_seconds)` to block fast-repeating spells
- [ ] Build a menu-driven CLI where user types number to perform an action


