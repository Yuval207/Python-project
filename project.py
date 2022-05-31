import pickle


def Menu():
    print("*" * 144)
    print("~AXIAL FINANCES~".center(230))
    print("--------------------------------------------------".center(230))
    print("MENU-")
    print("1. Insert Record/Records")
    print("2. Display Records asper Account Number")
    print("3. Display Records asper Customer Name")
    print("4. Display Records asper Customer Balance")
    print("5. Delete Record")
    print("6. Update Record")
    print("7. Search Record Details asper the account number")
    print("8. Search Record Details asper the Customer Name")
    print("9. Debit/Withdraw from the account")
    print("10. Credit into the account")
    print("11. Exit")
    print("*" * 144)


def SortAcc(F):
    try:
        with open(F, 'rb+') as fil:
            rec = pickle.load(fil)
            rec.sort(key=lambda rec: rec[0])
            fil.seek(0)
            pickle.dump(rec, fil)
    except FileNotFoundError:
        print(F, "File has no records")


def SortName(F):
    try:
        with open(F, 'rb+') as fil:
            rec = pickle.load(fil)
            rec.sort(key=lambda rec: rec[1])
            fil.seek(0)
            pickle.dump(rec, fil)
    except FileNotFoundError:
        print(F, "File has no records")


def SortBal(F):
    try:
        with open(F, 'rb+') as fil:
            rec = pickle.load(fil)
            rec.sort(key=lambda rec: rec[7])
            fil.seek(0)
            pickle.dump(rec, fil)
    except FileNotFoundError:
        print(F, "File has no records")


def Insert(F):
    fil = open(F, 'ab+')
    if fil.tell() > 0:
        fil.seek(0)
        Rec1 = pickle.load(fil)
    else:
        Rec1 = []
    fil.close()
    print("_" * 125)
    print("ENTER RECORD".center(230))
    Acc = int(input("Enter account no :"))
    for i in Rec1:
        if i[0] == Acc:
            print("this acount no. has been taken")
            print("plz. insert new and unique one")
            Insert(F)
        else:
            pass
    Name = input("Enter Name :")
    Mob = input("Enter Mobile :")
    if len(Mob) == 10:
        pass
    else:
        print("this is no valid mobile no. plz start over again")
        Insert(F)
    email = input("Enter Email :")
    if '@' and '.com' in email:
        pass
    else:
        print("this is no valid email id plz start over again")
        Insert(F)
    Add = input("Enter Address :")
    City = input("Enter City :")
    Country = input("Enter County :")
    Bal = float(input("Enter Balance :"))
    Rec = [Acc, Name.upper(), Mob, email, Add.upper(), City.upper(), Country.upper(), Bal]
    Rec1.append(Rec)
    ch = input("Do you want to enter more records (Y/N) :")
    if ch in "Yy":
        Insert(F)
    elif ch in 'Nn':
        with open(F, 'wb') as fil:
            pickle.dump(Rec1, fil)
    print("ok then bringing up menu...")


def Display(F):
    try:
        with open(F, 'rb') as fil:
            print("=" * 140)
            F = "%15s %15s %15s %15s %15s %15s %15s %15s"
            print(F % ("ACCNO", "NAME", "MOBILE", "EMAIL", "ADDRESS", "CITY", "COUNTRY", "BALANCE"))
            print("=" * 140)
            Rec = pickle.load(fil)
            c = len(Rec)
            for i in Rec:
                for j in i:  # print(j,end='\t')
                    print("%15s" % j, end=' ')
                print()
            print("*" * 140)
            print("Records Read : ", c)
            print("*" * 140)
    except EOFError:
        print("=" * 140)
        print("Records Read : ", c)
    except FileNotFoundError:
        print(F, "File Doesn't exist")


def Update(F):
    try:
        with open(F, 'rb+') as fil:
            Rec1 = pickle.load(fil)
            found = -1
            A = int(input("Enter the accound no whose details to be changed :"))
            for i in Rec1:
                if i[0] == A:
                    found = 0
                    ch = input("Change Name(Y/N) :")
                    if ch == 'y' or ch == 'Y':
                        i[1] = input("Enter Name :")
                        i[1] = i[1].upper()
                    ch = input("Change Mobile(Y/N) :")
                    if ch == 'y' or ch == 'Y':
                        i[2] = input("Enter Mobile :")
                    ch = input("Change Email(Y/N) :")
                    if ch == 'y' or ch == 'Y':
                        i[3] = input("Enter email :")
                        i[3] = i[3].upper()
                    ch = input("Change Address(Y/N) :")
                    if ch == 'y' or ch == 'Y':
                        i[4] = input("Enter Address :")
                        i[4] = i[4].upper()
                    ch = input("Change city(Y/N) :")
                    if ch == 'y' or ch == 'Y':
                        i[5] = input("Enter City :")
                        i[5] = i[5].upper()
                    ch = input("Change Country(Y/N) :")
                    if ch == 'y' or ch == 'Y':
                        i[6] = input("Enter country :")
                        i[6] = i[6].upper()
                    ch = input("Change Balance(Y/N) :")
                    if ch == 'y' or ch == 'Y':
                        i[7] = float(input("Enter Balance :"))
            if found == -1:
                print("Account details not found...")
            else:
                fil.seek(0)
                pickle.dump(Rec1, fil)
    except EOFError:
        print("Records Read : ", c)
    except FileNotFoundError:
        print(F, "no record to be updated...")


def Delete(F):
    try:
        with open(F, 'rb+') as fil:
            Rec = pickle.load(fil)
            ch = int(input("Enter the accountno to be deleted :"))
            for i in range(0, len(Rec)):
                if Rec[i][0] == ch:
                    print(Rec.pop(i))
                    print("Record Deleted ...")
                    break
            else:
                print("Record Not found !!!")

            fil.seek(0)
            pickle.dump(Rec, fil)
    except FileNotFoundError:
        print(F, "File Doesn't exist")
    except KeyError:
        print("Record Not found")
    except IndexError:
        print("Record Not found")


def SearchAcc(F):
    try:
        with open(F, 'rb') as fil:
            Rec = pickle.load(fil)
            ch = int(input("Enter the accountno to be searched"))
            for i in range(0, len(Rec)):
                if Rec[i][0] == ch:
                    print("=" * 140)
                    F = "%15s %15s %15s %15s %15s %15s %15s %15s"
                    print(F % (
                    "ACCNO", "NAME", "MOBILE", "EMAILADDRESS", "COMPLETE ADDRESS", "CITY", "COUNTRY", "BALANCE"))
                    print("=" * 140)
                    for j in Rec[i]:
                        print('%15s' % j, end=' ')
                    print()
                    break
            else:
                print("Record Not found ...!  recheck the number and select the same option after checking")
    except FileNotFoundError:
        print(F, "File has no entries to be searched !!")


def SearchName(F):
    try:
        with open(F, 'rb') as fil:
            Rec = pickle.load(fil)
            ch = input("Enter the Customer Name to be searched :")
            for i in range(0, len(Rec)):
                if Rec[i][1] == ch.upper():
                    print("=" * 140)
                    F = "%15s %15s %15s %15s %15s %15s %15s %15s"
                    print(F % (
                    "ACCNO", "NAME", "MOBILE", "EMAILADDRESS", "COMPLETE ADDRESS", "CITY", "COUNTRY", "BALANCE"))
                    print("=" * 140)
                    for j in Rec[i]:
                        print('%15s' % j, end=' ')
                    print()
                    break
            else:
                print("Record Not found ...")
    except FileNotFoundError:
        print(F, "there is no entries to be searched !!!!")


def Debit(F):
    try:
        with open(F, 'rb+') as fil:
            Rec = pickle.load(fil)
            print(" ! ! ! Please Note that the money can only be debited if min balance of Rs 5000 exists ! ! !")
            acc = int(input("Enter the account no from which the money is to be debited :"))
            for i in range(0, len(Rec)):
                if Rec[i][0] == acc:
                    Amt = float(input("Enter the amount to be withdrawn :"))
                    if Rec[i][7] - Amt >= 5000:
                        Rec[i][7] = Rec[i][7] - Amt
                        print("Amount Debited......")
                        break
                    else:
                        print("There must be min balance of Rs 5000")
                        break
            else:
                fil.seek(0)
                print("Record Not found")
        with open(F, 'wb') as f:
            pickle.dump(Rec, f)

    except FileNotFoundError:
        print(F, "File Doesn't exist")


def Credit(F):
    try:
        with open(F, 'rb+') as fil:
            Rec = pickle.load(fil)
            acc = int(input("Enter the account no from which the money is to be credited :"))
            for i in range(0, len(Rec)):
                if Rec[i][0] == acc:
                    Amt = float(input("Enter the amount to be added :"))
                    Rec[i][7] += Amt
                    print("Amount Credited")
                    break
            else:
                print("Record Not found")
                fil.seek(0)
                pickle.dump(Rec, fil)
        with open(F, 'wb') as f:
            pickle.dump(Rec, f)
    except FileNotFoundError:
        print(F, "File Doesn't exist")


Fi = "Yuval_finances"
while True:
    Menu()
    ch = input("Enter your Choice :")
    if ch == "1":
        Insert(Fi)
    elif ch == "2":
        SortAcc(Fi)
        Display(Fi)
    elif ch == "3":
        SortName(Fi)
        Display(Fi)
    elif ch == "4":
        SortBal(Fi)
        Display(Fi)
    elif ch == "5":
        Delete(Fi)
    elif ch == "6":
        Update(Fi)
    elif ch == "7":
        SearchAcc(Fi)
    elif ch == "8":
        SearchName(Fi)
    elif ch == "9":
        Debit(Fi)
    elif ch == "10":
        Credit(Fi)
    elif ch == "11":
        print("Exiting...")
        break
    else:
        print("Wrong Choice Entered plz check the menu again")
