# if standard from 1-4 then take only 4 subject marks i.e. Maths, Science, English, and Hindi ; for standard 5-10 take 6 subject marks i.e. Maths, Science, English, Hindi, History, and Geography; for standard 11-12 take 5 subject marks i.e. Maths, Physics, Chemistry, Biology, and English.
# i am using html template and f-string for standard 1-4 and i will use % string for standard 5-10 and i will be using format method for printting standard 11-12 marksheet.

# ============================ ENUM DEFINITIONS ============================ #
from enum import Enum, auto
# Enum for categorizing students by standard level
class StandardLevel(Enum):
    PRIMARY = auto()
    MIDDLE = auto()
    HIGH = auto()

    # Subjects for each level
    def subject(self):
        return{StandardLevel.PRIMARY: ['Maths', 'Science', 'English', 'Hindi'],
            StandardLevel.MIDDLE: ['Maths', 'Science', 'English', 'Hindi', 'History', 'Geography'],
            StandardLevel.HIGH: ['Maths', 'Physics', 'Chemistry', 'Biology', 'English']
        }[self]
        
    # Formatter method for each level
    def formatter(self):
        return {
            StandardLevel.PRIMARY: FormatterType.F,
            StandardLevel.MIDDLE: FormatterType.PERCENT,
            StandardLevel.HIGH: FormatterType.FORMAT
        }[self]
        
    # Custom string and debug output
    def __str__(self):
        return self.name.capitalize()

    def __repr__(self):
        return f'StandardLevel.{self.name}'

# Enum to represent different formatting techniques
class FormatterType(Enum):
    F = auto()         # f-string formatting
    PERCENT = auto()   # % formatting
    FORMAT = auto()    # .format() method
    
    def __str__(self):
        return self.name.lower()

    def __repr__(self):
        return f'FormatterType.{self.name}'
    
# ============================ USER INPUT SECTION ============================ #

f_name = input('Enter your first name: ')
l_name = input('Enter your last name: ')
standard = input('Enter your standard (1-12): ')

# Input validation for standard
if not standard.isdigit():
    print("Please enter a valid standard between 1 and 12.")
    exit()

standard = int(standard)
if not (1 <= standard <= 12):
    print("Please enter a valid standard between 1 and 12.")
    exit()


# Determine level and formatter based on standard
if standard <= 4:
    level = StandardLevel.PRIMARY
elif 5 <= standard <= 10:
    level = StandardLevel.MIDDLE
else:
    level = StandardLevel.HIGH

formatter = level.formatter()
subject_list = level.subject()

# ============================ MARK ENTRY SECTION ============================ #

# Ask the student to enter marks for subjects relevant to their standard
print(f"\nHello {f_name} {l_name},\nYou are a {level} school student.\nEnter your marks out of 100:")

marks = {}
for subject in subject_list:
    marks[subject] = int(input(f"{subject}: "))

# Calculate total marks and percentage
total = sum(marks.values())
percentage = round(total / len(subject_list), 2)

# ============================ STYLE + ROW GENERATION ============================ #

style_block = """
<style>
    body {
        background-color: #fffdd0; /* Cream background */
        font-family: Arial, sans-serif;
        color: black;
    }
    table {
        border-collapse: collapse;
        width: 50%;
        margin: 20px auto;
        color: black;
        background-color: white;
    }
    th, td {
        border: 1px solid #000;
        padding: 10px;
        text-align: center;
        text-transform: capitalize;
    }
    h2 {
        text-align: center;
        color: black;
        font-size: 30px;
        font-weight: bold;
    }
</style>
"""
# Generate HTML rows from subjects
mark_rows = ""
for subject in subject_list:
    mark_rows += f'<tr><th>{subject}</th><td>{marks[subject]}</td></tr>'

# Add total and percentage rows
mark_rows += f"<tr><th>Total</th><td style='color: blue;'>{total}</td></tr>"
mark_rows += f"<tr><th>Percentage</th><td style='color: blue;'>{percentage}%</td></tr>"

html_output = ""

# Standard 1-4: Use f-string
if formatter == FormatterType.F:
    html_output = f'''
    <html>
    <head>
    <title>Marksheet standard 1-4</title>
    {style_block}
    </head>
    <body>
    <h2>Student Marksheet</h2>
    <table>
        <tr><th>First Name</th><td>{f_name}</td></tr>
        <tr><th>Last Name</th><td>{l_name}</td></tr>
        <tr><th>Standard</th><td>{standard}</td></tr>
        <tr><th colspan="2">Marks</th></tr>
        {mark_rows}
    </table>
    </body>
    </html>
    '''
    
# Standard 5-10: Use % formatting
elif formatter == FormatterType.PERCENT:
    html_output = '''
    <html>
    <head>
    <title>Marksheet standard 5-10</title>
    %s
    </head>
    <body>
    <h2>Student Marksheet</h2>
    <table>
        <tr><th>First Name</th><td>%s</td></tr>
        <tr><th>Last Name</th><td>%s</td></tr>
        <tr><th>Standard</th><td>%s</td></tr>
        <tr><th colspan="2">Marks</th></tr>
        %s
    </table>
    </body>
    </html>'''% (style_block, f_name, l_name, standard, mark_rows)

# Standard 11-12: Use .format() method   
else:
    html_output = '''
    <html>
    <head>
    <title>Marksheet standard 11-12</title>
    {0}
    </head>
    <body>
    <h2>Student Marksheet</h2>
    <table>
        <tr><th>First Name</th><td>{1}</td></tr>
        <tr><th>Last Name</th><td>{2}</td></tr>
        <tr><th>Standard</th><td>{3}</td></tr>
        <tr><th colspan="2">Marks</th></tr>
        {4}
    </table>
    </body>
    </html>'''.format(style_block, f_name, l_name, standard, mark_rows)

# ============================ OUTPUT FILE HANDLING ============================ #
import webbrowser
# Save the HTML output to a file
with open('Marksheet.html', 'w') as f:
    f.write(html_output) 
# Open the HTML file in a web browser
webbrowser.open('Marksheet.html', new=2)
