
import os, csv, getpass, pickle
from tabulate import tabulate
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox

#function calls
def intro():
  f = open("intro.txt", 'r')
  print(f.read())
  f.close()

import getpass

def login1():
    f = open("usernames.csv")
    username = input('Enter your username: ')
    password = getpass.getpass('Enter your password: ')
    print()
    l = f.readlines()
    
    for i in range(1, len(l)):
        tempv = l[i].strip()  
        templ = tempv.split(',')
        
        if username == templ[0]:  
            pwd = templ[1]
            
            if pwd == password:
                u1 = ''
                formatted_username = username[0:].capitalize()
                #print("formatted watever",formatted_username)
                for j in formatted_username:
                    if j.isupper():
                        u1 += ' ' + j
                    elif j.islower():
                        u1 += j
                print("Welcome", u1, '\n')
                return True
            else:
                print("Incorrect password entered!")
                return False
    
    print("Wrong username entered!")
    return False

#PROGRAM
intro()
print()

while 1:
  ch=eval(input("1. User\n2. Managing Partner\n3. Lawyer\n4. New Register\nTO END PROGRAM, ENTER 90\nEnter choice:"))  #choice-to confirm identity

#USER-(MARIAM)

  if ch == 1:   
    x=True ##
    while True:
      x = login1()
      if x == False:
        print('Enter 0, if you would you like to go back to the main menu, else, enter 1 if you want to enter credentials again ')
        logch = eval(input("Enter value:"))
        if logch == 0:
          print("Returning to the main menu")
          print()
          break
        elif logch == 1:
          login1()

      elif x == True:
        pass     #if login credentials are right-it prints the next menu
      ch1 = eval(input("1. Services Offered\n2. More About Law Firm\n3. Return to Previous Menu\nEnter choice: "))
      if ch1 == 1:
        print("List Of Lawyers:")
        f = open("AttorneyProfile.csv")
        r = csv.reader(f)
        data = f.readlines()
        nl=[]
        for jk in data:
          tempjk=jk.rstrip('\n')
          splittedone=tempjk.split(',')
          nl.append(splittedone)
        print(tabulate(nl, headers='firstrow', tablefmt='grid'))
        print()
        explore = input("Would you like to explore more about our lawyers?")  #Input = Yes/ No
        if explore.upper() == "YES":
          while True:
            reqlawyer = eval(input("Enter Lawyer ID=")) #user will enter the id of the lawyer and info
            templ=[]
            reqid=str(reqlawyer)
            f2=open("AttorneyProfile.csv")
            r2=csv.reader(f2)
            ll=f2.readlines()
            for jj in ll:
              if reqid in jj:
                splitone=jj.split(',')
                templ.append(reqlawyer)
                x1=splitone[1]
                x2=splitone[2]
                templ.append(x1)
                templ.append(x2)
                fg=True
                break
            if templ==[]:
              print("Wrong ID Entered")
              fg=False
            if fg==True:
              print(templ)
            else:
              print("Returning To Previous Menu")
              break
            clientname=input("Enter client name: ")
            doreq=input("Enter today's date seperated with '/': ")
            des=input("Enter short description of your case: ")
            uc=eval(input("Enter how urgent your case must be solved --> 1 = VIP Prioritiy, 2 = Normal Priority: "))
            templ.insert(1,clientname)
            templ.insert(2,doreq)
            templ.append(des)
            templ.append(uc)
            f3=open("requests.csv","a",newline="")
            w1=csv.writer(f3)
            w1.writerow(templ)
            f3.close()
            f2.close()
            break
        elif explore.upper()=='NO':
          print("You have successfully logged out.")
          print("Returning to previous menu")
        print()
        break

      elif ch1==2:
        print("About Justice League Law Firm")
        print()
        f=open("intro.txt")
        xx=f.read()
        print(xx)
        f.close()
        print()
        break

      elif ch1==3:
        print("Returning to previous menu")
        print()
        break

#EXECUTIVE-Managing Partner(GREHNA)
  elif ch == 2:  
    x=login1()
    if x==True:
      while 1:
        print("1. View Client Details") 
        print("2. View Case File")
        print("3. View Attorney Profiles")
        print("4. Track Revenue")
        print("5. See New Applicants")
        print("6. To Update Changes To The Case File")
        print()
        print("TO RETURN TO MAIN MENU, ENTER 21:")
        print()
        ch2=eval(input("Enter Choice="))
        if ch2==1:                                                  #CLIENT INFO
          f1 = open("admindatabase.csv")
          r = csv.reader(f1)
          data = f1.readlines()
          nl=[]
          for jk in data:
            tempjk=jk.rstrip('/n')
            splittedone=tempjk.split(',')
            nl.append(splittedone)
          print(tabulate(nl, headers='firstrow', tablefmt='grid'))
          print("NOTE: For Status\n1 = Open\n0 = Closed")
          print()
        elif ch2==2:                                               #CASES INFO
          f1 = open("casefiles.csv")
          r = csv.reader(f1)
          data = f1.readlines()
          nl=[]
          for jk in data:
            tempjk=jk.rstrip('/n')
            splittedone=tempjk.split(',')
            nl.append(splittedone)
          print(tabulate(nl, headers='firstrow', tablefmt='grid'))
          print()

        elif ch2==3:                                               #LAWYER INFO
          f2 = open("AttorneyProfile.csv")
          r1 = csv.reader(f2)
          data = f2.readlines()
          n2=[]
          for jk1 in data:
            tempjk1=jk1.rstrip('/n')
            splittedone1=tempjk1.split(',')
            n2.append(splittedone1)
          print(tabulate(n2, headers='firstrow', tablefmt='grid'))
          print()

        elif ch2==4:                                                #REVENUE(PAST 10 YRS)
          while True:
            year = [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
            revenue_rate = [7.5, 6.3, 5.5, 6.2, 6.5, 7, 6.9, 7.2, 8, 9.5, 12]
            plt.plot(year, revenue_rate, color='red', marker='o')
            plt.title('Revenue Statistics Over Past 10 years', fontsize=14)
            plt.xlabel('Year', fontsize=14)
            plt.ylabel('Revenue', fontsize=14)
            plt.grid(True)
            plt.show()
            print()
            break
          
          #SQL PART
        elif ch2==5:#make a file for the applicants-SQL                   #TO SEE NEW APPLICANTS 
          print()
  
        elif ch2==6:                                                 #TO UPDATE
          print("1.To Add")
          print("2.To Delete")
          cc=eval(input("Enter choice="))
          if cc==1:
            def appending():
              f=open("casefiles.csv","a",newline="")
              w=csv.writer(f)
              n=eval(input("Enter the no. of cases to be added="))
              for i in range(n):
                a=eval(input("Enter File No.="))
                b=input("Enter 1st Name=")
                c=input("Enter Last Name=")
                d=input("Enter Email=")
                e=input("Enter Nationality=")
                f_input=input("Date Of Registeration=")
                g=input("Enter Type Of Case=")
                h=input("Enter Reporting Office=")
                i=input("Enter Status=")
                l=[a, b, c, d, e, f_input, g, h, i]  # Store data in a list
                w.writerow(l)
              f.close()
            appending()
            print()
            print("DATA ADDED TO THE FILE!")  
            print()
          elif cc==2:
            def delete(yy):#yy=row index to delete
              lines = []
              f=open("casefiles.csv","r")
              r= csv.reader(f)
              for i, row in enumerate(r):
                if i!= yy:
                  lines.append(row)
              f.close()    
              f1=open("casefiles.csv", "w", newline="")
              w=csv.writer(f1)
              w.writerows(lines)
              f1.close()
            yy=eval(input("Input Row Index To Delete="))
            delete(yy)
            print()
            print("ROW DELETED FROM THE FILE!") 
            print()
          else:
            print()
            print("WRONG INPUT PLEASE TRY AGAIN!")  
            print()
        elif ch2==21:                                                #TO RETURN TO MAIN MENU
          print()
          print("RETURNING TO PREVIOUS MENU!")
          print()
          break
        else:                                                      #IF WRONG CHOICE ENTERED
          print()
          print("INVALID CHOICE! PLEASE TRY AGAIN.")
          print()
      

#LAWYERS(SHRESTI)

  elif ch == 3:  
    login1()
    while True:
      ch3 = eval(input("1. View requests\n2. View client information\n3.To return to main menu, enter 23: "))
      print()
      if ch3==1:
        f4=open("requests.csv")
        r3 = csv.reader(f4)
        data1 = f4.readlines()
        l=[]
        if len(data1) <= 2:
          root = tk.Tk()
          root.withdraw() 
          messagebox.showerror("Error", "It does not exist")
          
        else:  
          for m in data1:
            print(data1)
            tempm = m.rstrip('\n')  
            splittedone = tempm.split(',')
            l.append(splittedone)
          print(tabulate(l, headers='firstrow', tablefmt='grid'))

      if ch3==2:
        f5=open("admindatabase.csv")
        r=csv.reader(f5)
        data=f5.readline()
        choice=input("Enter clients of which law? Input should be first letter of Law, for eg: for Family Law input should be F")
        if choice=="F":
          l1=[]
          while data:
            tempm = data.rstrip('\n')    
            splittedone = tempm.split(',')
            if "Family Law"==splittedone[-1]:
              l1.append(splittedone)
            data=f5.readline()
          print(tabulate(l1, headers='firstrow', tablefmt='grid'))
        elif choice=="R":
          l1=[]
          while data:
            tempm = data.rstrip('\n')    
            splittedone = tempm.split(',')
            if "Real Estate Law"==splittedone[-1]:
              l1.append(splittedone)
            data=f5.readline()
          print(tabulate(l1, headers='firstrow', tablefmt='grid'))
        elif choice=="C":
          l1=[]
          while data:
            tempm = data.rstrip('\n')    
            splittedone = tempm.split(',')
            if "Criminal Law"==splittedone[-1]:
              l1.append(splittedone)
            data=f5.readline()
          print(tabulate(l1, headers='firstrow', tablefmt='grid'))
        elif choice=="B":
           l1=[]
           while data:
            tempm = data.rstrip('\n')    
            splittedone = tempm.split(',')
            if "Bankruptcy Law"==splittedone[-1]:
              l1.append(splittedone)
              data=f5.readline()
           print(tabulate(l1, headers='firstrow', tablefmt='grid'))
        elif choice=="I":
          l1=[]
          while data:
            tempm = data.rstrip('\n')    
            splittedone = tempm.split(',')
            if "Immigration Law"==splittedone[-1]:
              l1.append(splittedone)
            data=f5.readline()
          print(tabulate(l1, headers='firstrow', tablefmt='grid'))
        elif choice=="B":
          l1=[]
          while data:
            tempm = data.rstrip('\n')    
            splittedone = tempm.split(',')
            if "Business Law"==splittedone[-1]:
              l1.append(splittedone)
            data=f5.readline()
          print(tabulate(l1, headers='firstrow', tablefmt='grid'))
        elif choice=="T":
          l1=[]
          while data:
            tempm = data.rstrip('\n')    
            splittedone = tempm.split(',')
            if "Tax"==splittedone[-1]:
              l1.append(splittedone)
            data=f5.readline()
          print(tabulate(l1, headers='firstrow', tablefmt='grid'))
        f5.close()
      elif ch3==23:
        print("Returning to previous menu")
        break
      print()


    
  elif ch==4: 
    while 1:
      ch4_1=eval(input("1. New Lawyer\n2. New User\nTo return to previous menu, enter 91\nEnter choice:"))
      print()

      if ch4_1==1: #NEW LAWYER
        f=open("newlawyers.csv",'r+')
        al=f.read()
        role=input("Would you like to apply as an intern?\nYour Answer: ")
        if role.upper()=='YES':
          role='Intern'
        else:
          role='Lawyer'
        name=input("Name of applicant: ")
        email=input("email: ")
        phone=input("Enter phone number with code: ")
        address=input("Enter your address: ")
        dob=input("Enter date of birth seperated '/': ")
        qual=input("List your law degrees: ") #not a list
        objective=input("What do you plan to achieve by being apart of the Justice League Law Firm?\nYour answer: ")
        yshdwechooseu=input("Why should we choose you?\nYour answer: ")
        gradf=input("Which university have you graduated from?\nYour answer: ")
        skills=input("Do you have any skills that you would like to emphasize?*\n(*Optional)\nYour Answer: ")
        if skills=='':
          skills=''
        if role.upper()=='LAWYER':
          pastexp=input("Tell us more about your past experience\nYour Answer: ")
        l=[role,name,dob,qual,gradf,phone,address,objective,yshdwechooseu,skills,pastexp,email]
        #WE NEED TO APPEND l into newlawyers.csv and we need to add the role
        f.close()

      elif ch4_1==2: #NEW USER

        fullname=input("Enter full name: ")
        l=fullname.split()
        t=tuple(l)
        username=''.join(t)

        pwd=input("Enter  password: ")
        rpwd=input("Re-enter password: ")
        if rpwd==pwd:
          print(l[0],"Welcome to Justice League Law Firm!")
          print("Your username is ",username,'and your password is ',pwd)
          f=open("usernames.csv","a")
          l=[username,pwd,"User"]
          w=csv.writer(f)
          w.writerow(l)
          #Done
          f.close()
        else:
          print("Second entry doesn't match the first entry, please try again")
          break
                                           #NEW REGISTER  
    print()
    
  elif ch == 90:  #EXIT
    print('Program END.')
    break
  


  #priority
  #hours client required
  #Append the the request chosen to seperate file with lawyer name