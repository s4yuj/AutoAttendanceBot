import glob
import os
import csv
import smtplib
from datetime import date

list_of_files = glob.glob(r'FULL PATH')                 #enter the path to the csv file but replace the name of the csv file with a * as shown in eg.
latest_file = max(list_of_files, key=os.path.getctime)
file = os.path.basename(latest_file)
filename=file.split('.csv')[0]

f=open('%s.csv'%filename ,'r')
l1=list(csv.reader(f))[4:]

for row in l1:
    if l1.index(row)>0:
        row[1]=row[1].split(' ')[1]


data=f"Greetings ma'am,\nPFA the attendance for {date.today()}\n\n"
for row in l1:
    data+=f'{" , ".join(row)}\n'


addrs=('YOUR EMAIL')
teachers_dict={'chem':'[chemistry]@dpsnoida.co.in','cs':'[cs]@dpsnoida.co.in'}      #enter teacher's emails here

subject=str(input('enter subject: '))
teacher=teachers_dict.get(subject)
addrs += (teacher,)

x=str(input(f'{data}\n Do you wish to send email to {str(addrs)}: '))
if x.lower()=='yes':
    with smtplib.SMTP('smtp.gmail.com',587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(EMAIL, PASSWORD)                #enter email and password in single/double quotes.

        subject=f'Attendance for Class [CLASS] | {date.today()}'
        body=f"Greetings ma'am, PFA the attendance for {date.today()}\n\n"
        for row in l1:
            # print(row[0],row[1],row[2],sep='\t')
            body+=f'{" , ".join(row)}\n'

        msg=f'Subject: {subject}\n\n{body}'

        smtp.sendmail(from_addr=EMAIL,to_addrs=addrs,msg= msg)
    print('\nemail sent successfully')
    str=input('')
else:
    str1=input('')
