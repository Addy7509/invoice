from functions import master
ob1 = master()
print("*** INVOIVE MANAGEMENT SYSTEM ***")
print("*** Master press(1)||Invoice press(2)||View press(3) ***")
ch = input("Enter choice : ")
#__MASTER__
if ch == "1":
    print("*** MASTER PAGE ***")
    print("category press(1)||brand press(2)||client press(3)")
    ch1 = input("Enter choice : ")
    # category (1)
    if ch1 == "1":
        print("*** Category Management System ***")
        print("ADD category(1)|| DELETE category(2)")
        catch = input("Enter Choice : ")
        
        if catch == "1":
            # Adding category
            ob1.cat_Add()
        if catch=="2":
            # Deleting category
            ob1.cat_display()
            delcat = int(input("enter category ID : "))
            sure = input("Are you Sure you want to Delete, press ? y/n : ")
            if sure=="y":
                ob1.cat_Del(delcat)
            else:
                print("Aborted!!!")
    # brand(2)
    elif ch1=="2":
        print("*** Brand Management System ***")
        print("ADD brand(1)|| DELETE brand(2)")
        brandch = input("Enter Choice : ")
        #brand_add
        if brandch=="1":
            print("{All Brands}")
            ob1.brand_display()
            print()
            print("--> enter UPPERCASE letters only <--")
            ob1.brand_Add()
        #brand_delete
        if brandch=="2":
            print("{All Brands}")
            ob1.brand_display()
            print()
            ob1.brand_Del()




