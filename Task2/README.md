# 📝 Python Enum-Based Marksheet Generator

This project generates a subject-wise marksheet in HTML format based on the student's standard (grade) and uses **Python Enums** to organize logic for grade levels and formatting types.  
It takes the student's first name, last name, standard (1–12), and subject marks, and then outputs a clean, styled HTML file.

---
## 🔧 Original (Before) Implementation

```python
# Traditional approach without Enums
if standard <= 4:
    level = 'Primary'
    formatter = 'f'
elif 5 <= standard <= 10:
    level = 'Middle'
    formatter = '%'
else:
    level = 'High'
    formatter = 'format'

subject_list = {
    'Primary': ['Maths', 'Science', 'English', 'Hindi'],
    'Middle': ['Maths', 'Science', 'English', 'Hindi', 'History', 'Geography'],
    'High': ['Maths', 'Physics', 'Chemistry', 'Biology', 'English']
}

subject = subject_list[level]



## 📚 Enum Design

### 1. `StandardLevel` Enum

Defines levels based on standard and holds subject information:

```python
from enum import Enum, auto

class StandardLevel(Enum):
    PRIMARY = auto()
    MIDDLE = auto()
    HIGH = auto()

    def subjects(self):
        return {
            StandardLevel.PRIMARY: ['Maths', 'Science', 'English', 'Hindi'],
            StandardLevel.MIDDLE: ['Maths', 'Science', 'English', 'Hindi', 'History', 'Geography'],
            StandardLevel.HIGH: ['Maths', 'Physics', 'Chemistry', 'Biology', 'English']
        }[self]

    def formatter(self):
        return {
            StandardLevel.PRIMARY: FormatterType.F,
            StandardLevel.MIDDLE: FormatterType.PERCENT,
            StandardLevel.HIGH: FormatterType.FORMAT
        }[self]
