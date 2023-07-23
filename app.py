import jinja2
import pdfkit
from datetime import datetime, timedelta, date
import os
import sys

# current directory of script
script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))
print(script_directory)

# set template folder
TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__), 'templates'),)

# current working directory
current_dir = os.getcwd()
print(f'current directory {current_dir}')

if script_directory != current_dir:
    os.chdir(script_directory)

# current working directory updated
current_dir = os.getcwd()
print(f'current directory updated {current_dir}')

client_name = "Appan"
item1 = "TV"
item2 = "Couch"
item3 = "Washing machine"

item1_qty = 3
item2_qty = 2
item3_qty = 1

item1_price = 150
item2_price = 199
item3_price = 349

item1_subtotal = item1_qty * item1_price
item2_subtotal = item2_qty * item2_price
item3_subtotal = item3_qty * item3_price

total = item1_subtotal + item2_subtotal + item3_subtotal

today_date = datetime.today().strftime("%d %b, %Y")
#print(f'Today date: {today_date}')

# Due date is 15 days from current date
due_date = date.today() + timedelta(days=15)
#print(f'Due date {due_date}')

context = {'client_name': client_name, 'today_date': today_date, 'due_date': due_date,\
           'item1': item1, 'item1_qty': item1_qty, \
           'item1_price': f'${item1_price:.2f}', 'item1_subtotal': f'${item1_subtotal:.2f}', \
           'item2': item2, 'item2_qty': item2_qty, \
           'item2_price': f'${item2_price:.2f}', 'item2_subtotal': f'${item2_subtotal:.2f}', \
           'item3': item3, 'item3_qty': item3_qty, \
           'item3_price': f'${item3_price:.2f}', 'item3_subtotal': f'${item3_subtotal:.2f}', \
           'total': f'${total:.2f}'       
          }


template_loader = jinja2.FileSystemLoader(TEMPLATE_DIRS)
ENV = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATE_DIRS))
template = ENV.get_template('invoice.html')

# Output variable from rendrered HTML 
output_text = template.render(context)


def urltopdf(output_text,pdffile):
    '''
        input
        - string  : target HTML
        - pdffile : target pdf file name
    '''
    path_wkthmltopdf = 'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
    pdfkit.from_string(output_text,pdffile,configuration=config, css="invoice.css")

# Call function to create invoice pdf from HTML
urltopdf(output_text,'invoice.pdf')

