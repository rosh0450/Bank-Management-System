import mysql.connector
from tabulate import tabulate
import getpass
from datetime import datetime

mydb=mysql.connector.connect(
    user='client1',
    passwd='client1',
    host='localhost',
    database='bankdb',
    auth_plugin='mysql_native_password')


mycursor=mydb.cursor(buffered=True)

#created database bankdb
#mycursor.execute('create database bankdb')
'''
def Welcome():
    print("*"*210)
    print("WELCOME".center(210))
    print("TO".center(210))
    print("XYZ Bank!!!".center(210))
    print("*"*210)

def Menu():
    print("*"*210)
    print("MAIN MENU".center(210))
    print("    1. Insert Record/Records".center(210))
    print("    2. Display Records".center(210))
    print("       a. Sorted as per Account Number".center(210))
    print("       b. Sorted as per Customer Name".center(210))
    print("       c. Sorted as per Customer Balance".center(210))
    print("    3. Search Record Details as per the account number".center(210))
    print("    4. Update Record".center(210))
    print("    5. Delete Record".center(210))
    print("    6. Perform Transactions from the account".center(210))
    print("       a. Debit/Withdraw from the account". center(210))
    print("       b. Credit/Deposit into the account".center(210))
    print("    7. Review Transactions from the account".center(210))
    print("    8. Review any Information Updates from the account".center(210))
    print("    9. Exit".center(210))
    print("*"*210)
'''

#print(str_time.rjust(210," "))

def Welcome():
    print("*"*210)
    print("WELCOME".center(210))
    print("TO".center(210))
    print("XYZ Bank!!!".center(210))
    print("*"*210)

def Menu():
    print("*"*210)
    print("\tMAIN MENU")
    print("\t1. Insert Record/Records")
    print("\t2. Display Records")
    print("\t   a. Sorted as per Account Number")
    print("\t   b. Sorted as per Customer Name")
    print("\t   c. Sorted as per Customer Balance")
    print("\t3. Search Record Details as per the account number")
    print("\t4. Update Record")
    print("\t5. Delete Record")
    print("\t6. Perform Transactions from the account")
    print("\t   a. Debit/Withdraw from the account")
    print("\t   b. Credit/Deposit into the account")
    print("\t7. Review Transactions from the account")
    print("\t8. Review any Information Updates from the account")
    print("\t9. Exit")
    print("*"*210)


def MenuSort():
    print("\t   a. Sorted as per Account Number")
    print("\t   b. Sorted as per Customer Name")
    print("\t   c. Sorted as per Customer Balance")
    print("\t   d. Back")

def MenuTransaction():
    print("\t   a. Debit/Withdraw from the account")
    print("\t   b. Credit/Deposit into the account")
    print("\t   c. Back")

def Create():
    #try:
        #mycursor.execute("CREATE TABLE bank(accno VARCHAR(10), name VARCHAR(10), mobile VARCHAR(20), email VARCHAR(20), adderss VARCHAR(20), city VARCHAR(15), country VARCHAR(15), balance int)")
        #print("Table Created")
        #Insert()
    #except:
        #print("Table exist")
        #Insert()
    Insert()

def Insert():
    while True:
        acc=input("Enter account no: ")
        name=input("Enter Name: ")
        mob=input("Enter Mobile Number: ")
        email=input("Enter Email: ")
        add=input("Enter Address: ")
        city=input("Enter City: ")
        country=input("Enter Country: ")
        bal=int(input("Enter Balance: "))
        rec=[acc, name.upper(), mob, email.upper(), add.upper(), city.upper(), country.upper(), bal]
        cmd="INSERT INTO bank values(%s, %s, %s, %s, %s, %s, %s, %s)"
        mycursor.execute(cmd, rec)
        mydb.commit()

        ch=input("Do you want to enter more records ")
        if ch=='N' or ch=='n':
            break;

def DispSortAcc():
    try:
        cmd="SELECT * FROM bank ORDER BY accno"
        mycursor.execute(cmd)
        F="%26s %26s %26s %26s %26s %26s %26s %26s"
        #print(tabulate(mycursor, headers=["USER", "ACCNO", "STATUS", "TIMESTAMP"], tablefmt="fancy_grid"))
        print(tabulate(mycursor, headers=["ACCNO", "NAME", "MOBILE", "EMAIL", "ADDRESS", "CITY", "COUNTRY", "BALANCE"], tablefmt="fancy_grid"))
        
    except:
        print("Table doesn't exist")

def DispSortName():
    try:
        cmd="SELECT * FROM bank ORDER BY name"
        mycursor.execute(cmd)
        F="%15s %15s %15s %15s %15s %15s %15s %15s"
        #print(F % ("ACCNO", "NAME", "MOBILE", "EMAIL", "ADDRESS", "CITY", "COUNTRY", "BALANCE"))
        print(tabulate(mycursor, headers=["ACCNO", "NAME", "MOBILE", "EMAIL", "ADDRESS", "CITY", "COUNTRY", "BALANCE"], tablefmt="fancy_grid"))
    except:
        print("Table doesn't exist")

#print ("{:<8} {:<15} {:<10} {:<10}".format(k, lang, perc, change))


def DispSortBal():
    try:
        cmd="SELECT * FROM bank ORDER BY balance"
        mycursor.execute(cmd)
        F="%15s %15s %15s %15s %15s %15s %15s %15s"
        
        print(tabulate(mycursor, headers=["ACCNO", "NAME", "MOBILE", "EMAIL", "ADDRESS", "CITY", "COUNTRY", "BALANCE"], tablefmt="fancy_grid"))
    except:
        print("Table doesn't exist")

        
 ############################################################################################################################################################
def DispTransac():
    #try:
        acc=input("Enter the account no. to review the transactions ")
        print()
        p=0
        cmd="SELECT * from transac where ano=%s and ibal<>fbal order by uptime desc"
        val=(acc,)
        mycursor.execute(cmd,val)
        
        F="%36s %36s %36s %36s %36s"
        #print(F % ("USER", "ACCNO", "INITIAL BALANCE", "FINAL BALANCE", "TIMESTAMP"))
        print(tabulate(mycursor, headers=["USER", "ACCNO", "INITIAL BALANCE", "FINAL BALANCE", "TIMESTAMP"], tablefmt="fancy_grid"))
    
    #except:
       # print("Table doesn't exist")

'''

def DispTransac():
    #try:
        acc=input("Enter the account no. to review the transactions ")
        print()
        p=0
        cmd="SELECT * from transac where ano=%s and ibal<>fbal order by uptime desc"
        val=(acc,)
        mycursor.execute(cmd,val)
        #mycursor.execute(cmd)

        for i in mycursor:
            if i[1]==acc:
                F="%36s %36s %36s %36s %36s"
                #print(F % ("USER", "ACCNO", "INITIAL BALANCE", "FINAL BALANCE", "TIMESTAMP"))
                print(tabulate(mycursor, headers=["USER", "ACCNO", "INITIAL BALANCE", "FINAL BALANCE", "TIMESTAMP"], tablefmt="fancy_grid"))
                print()
                p+=1

        if p==0:
            print("Record Not Found!!\n")
                
            
    #except:
       # print("Table doesn't exist")
'''


def DispSearchAcc():
    try:
        cmd="SELECT * FROM bank where accno=%s"
        
        ch=input("Enter the account no. to be searched ")
        print()
        val=(ch,)
        mycursor.execute(cmd, val)
        print(tabulate(mycursor, headers=["ACCNO", "NAME", "MOBILE", "EMAIL", "ADDRESS", "CITY", "COUNTRY", "BALANCE"], tablefmt="fancy_grid"))
        print()
                
    except:
        print("Table doesn't exist")

def Update():
    #try:
        cmd="SELECT * FROM bank"
        mycursor.execute(cmd)
        A=input("Enter the account no. whose details need to be changed ")
        print()
        for i in mycursor:
            i=list(i)
            if i[0]==A:
                ch=input("Change Name(Y/N)")
                if ch=='Y' or ch=='y':
                    i[1]=input("Enter Name ")
                    i[1]=i[1].upper()
                print()

                ch=input("Change Mobile(Y/N) ")
                if ch=='Y' or ch=='y':
                    i[2]=input("Enter Mobile No. ")
                print()

                ch=input("Change Email(Y/N) ")
                if ch=='Y' or ch=='y':
                    i[3]=input("Enter Email ")
                    i[3]=i[3].upper()
                print()

                ch=input("Change Address(Y/N) ")
                if ch=='Y' or ch=='y':
                    i[4]=input("Enter Address ")
                    i[4]=i[4].upper()
                print()

                ch=input("Change City(Y/N) ")
                if ch=='Y' or ch=='y':
                    i[5]=input("Enter City ")
                    i[5]=i[5].upper()
                print()

                ch=input("Change Country(Y/N) ")
                if ch=='Y' or ch=='y':
                    i[6]=input("Enter Country ")
                    i[6]=i[6].upper()
                print()

                ch=input("Change Balance(Y/N) ")
                if ch=='Y' or ch=='y':
                    i[7]=int(input("Enter Balance "))
                print()

                cmd="UPDATE bank SET name=%s, mobile=%s, email=%s, adderss=%s, city=%s, country=%s, balance=%s WHERE accno=%s"
                val=(i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[0])
                mycursor.execute(cmd, val)
                mydb.commit()
                print("Account Updated!!")
                print()
                break
        else:
            print("Record Not Found!!")
            print()

    #except:
     #   print("No such Table")


def Delete():
    try:
        cmd="SELECT * FROM bank"
        mycursor.execute(cmd)
        A=input("Enter the Account No. which needs to be deleted ")
        print()
        p=0
        for i in mycursor:
            i=list(i)
            if i[0]==A:
                cmd="DELETE FROM bank WHERE accno=%s"
                val=(i[0],)
                mycursor.execute(cmd, val)
                mydb.commit()
                print("Account Deleted")
                print()
                p+=1
                break;
        if p==0:
            print("Record Not Found")
            print()

    except:
        print("No such Table")


def Debit():
    try:
        cmd="SELECT * FROM bank"
        mycursor.execute(cmd)
        print("Please note that a minimum balance of Rs.5000 needs to be maintained")
        acc=input("Enter the account no. from which the money is to be debited ")
        print()
        p=0
        for i in mycursor:
            i=list(i)
            if i[0]==acc:
                p+=1
                Amt=int(input("Enter the Amount to be Debited/Withdrawn "))
                print()
                if i[7]-Amt>=5000:
                    i[7]-=Amt
                    cmd="UPDATE bank SET BALANCE=%s WHERE accno=%s"
                    val=(i[7], i[0])
                    mycursor.execute(cmd, val)
                    mydb.commit()
                    print("Amount Debited/Withdrawn")
                    print()
                    break
                else:
                    print("Minimum Balance of Rs.5000 needs to be maintained!!\nGiven amount can't be withdrawn\nPlease Try Again!!!")
                    print()
                    break

        if p==0:
            print("Record Not Found!!")
            print()


    except:
        print("No such Table")


def Credit():
    try:
        cmd="SELECT * FROM bank"
        mycursor.execute(cmd)
        
        acc=input("Enter the account no. from which the money is to be Credited ")
        print()
        p=0
        for i in mycursor:
            i=list(i)
            if i[0]==acc:
                p+=1
                Amt=int(input("Enter the Amount to be Credited/Deposited "))
                print()
                i[7]+=Amt
                cmd="UPDATE bank SET BALANCE=%s WHERE accno=%s"
                val=(i[7], i[0])
                mycursor.execute(cmd, val)
                mydb.commit()
                print("Amount Credited/Deposited")
                print()
                break
                

        if p==0:
            print("Record Not Found!!")
            print()

    except:
        print("No such Table")


def DispUpdates():
    try:
        acc=input("Enter the account no. to review the Updates ")
        cmd="SELECT * from updates where ano=%s order by uptime desc"
        val=(acc,)
        mycursor.execute(cmd,val)
        
        F="%30s %20s %100s %30s"
        print(tabulate(mycursor, headers=["USER", "ACCNO", "STATUS", "TIMESTAMP"], tablefmt="fancy_grid"))
    
    except:
        print("Table doesn't exist")



'''
main() function of project from where all the functions are called
'''
Welcome()
time_obj=datetime.now()
str_time=time_obj.strftime("TIME & DATE:  %H:%M:%S.%f - %b %d %Y")

print("\nUSER: client1@localhost", end='')
print(str_time.rjust(185," "))
print("Hello user client1@localhost")
pas=getpass.getpass(prompt="\nEnter the password: ")

while True:
    
    if pas=="client1":
        Menu()
        ch=input("Enter your Choice ")
        #print()
        if ch=="1":
            print()
            Create()

    

        elif ch=="2":
            while True:
                print()
                print("*"*210)
                MenuSort()
                print("*"*210)
                print()
                ch1=input("Enter Choice a/b/c/d ")
                print()
                if ch1 in ['a', 'A']:
                    DispSortAcc()
                elif ch1 in ['b', 'B']:
                    DispSortName()
                elif ch1 in ['c', 'C']:
                    DispSortBal()
                elif ch1 in ['d', 'D']:
                    print("Back to the main menu")
                    print()
                    break
                else:
                    print("Invalid Choice!!")

        elif ch=="3":
            print()
            DispSearchAcc()
            
        elif ch=="4":
            print()
            Update()
            
        elif ch=="5":
            print()
            Delete()

        elif ch=="6":
            while True:
                print()
                print("*"*210)
                MenuTransaction()
                print("*"*210)
                print()
                ch1=input("Enter Choice a/b/c ")
                print()
                if ch1 in ['a', 'A']:
                    Debit()
                elif ch1 in ['b', 'B']:
                    Credit()
                elif ch1 in ['c', 'C']:
                    print("Back to the main menu")
                    print()
                    break
                else:
                    print("Invalid Choice!!")

        elif ch=="7":
            print()
            DispTransac()

        elif ch=="8":
            print()
            DispUpdates()
            
        elif ch=="9":
            print()
            r=input("Press Enter to Exit!!")
            if r=="":
                break
            
        else:
            print("Wrong Choice Made!!")

    else:
        print("ERROR: Access denied for user 'client1'@'localhost' (using password: YES)")
        pas=getpass.getpass(prompt="\nEnter the password: ")
