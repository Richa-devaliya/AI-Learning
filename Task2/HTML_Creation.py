# String formatting examples
f_name = input('Enter your first name: ')
l_name = input('Enter your last name: ')
standard = input('Enter your standard (1-12): ')

if standard.isdigit():
    standard = int(standard)
else:
    print("Please enter a valid standard between 1 and 12.")
    exit()
    
if standard < 1 or standard > 12:
    print("Please enter a valid standard between 1 and 12.")
    exit()
# if standard from 1-4 then take only 4 subject marks i.e. Maths, Science, English, and Hindi ; for standard 5-10 take 6 subject marks i.e. Maths, Science, English, Hindi, History, and Geography; for standard 11-12 take 5 subject marks i.e. Maths, Physics, Chemistry, Biology, and English.
# i am using html template and f-string for standard 1-4 and i will use % string for standard 5-10 and i will be using format method for printting standard 11-12 marksheet.

subject_list = {
    'Primary': ['Maths', 'Science', 'English', 'Hindi'],
    'Middle': ['Maths', 'Science', 'English', 'Hindi', 'History', 'Geography'],
    'High': ['Maths', 'Physics', 'Chemistry', 'Biology', 'English']
}

if standard <= 4:
    level = 'Primary'
    formatter = 'f'
elif 5 <= standard <= 10:
    level = 'Middle'
    formatter = '%'
else:
    level = 'High'
    formatter = 'format'
    
subject = subject_list[level]
marks = {}
print(f"\nHello {f_name} {l_name}, \nYou are a {level.lower()} school student. \nEnter your marks out of 100 in the following subjects: \n")
# marks
for sub in subject:
    marks[sub] = int(input(f'{sub}:'))
# Calculate total and percentage    
total = sum(marks.values())
percentage = round(total / len(subject), 2)

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
for sub in subject:
    mark_rows += f'<tr><th>{sub}</th><td>{marks[sub]}</td></tr>'
 
# Add total and percentage rows with blue color
mark_rows += f"<tr><th> Total </th><td style='color: blue;'>{total}</td></tr>"
mark_rows += f"<tr><th> Percentage </th><td style='color: blue;'>{percentage}%</td></tr>"   

html_output = ""

if formatter == 'f':
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
    
elif formatter == '%':
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

import webbrowser
# Save the HTML output to a file
with open('Marksheet.html', 'w') as f:
    f.write(html_output) 
# Open the HTML file in a web browser
webbrowser.open('Marksheet.html', new=2)
