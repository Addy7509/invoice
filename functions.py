from dbcon import DBcon

class master(DBcon):
    #__category__table
    def cat_display(self):
        sql = "select * from category"
        self.mycursor.execute(sql)
        myval = self.mycursor.fetchall()
        for x in myval:
            print("ID->",x)
    #adding Category
    def cat_Add(self):
        for x in range(1,3):
            print("Enter Category Name(",x,") : ")
            self.newcat = input()
            sql = "select count(name) from category where name=%s"
            value = [self.newcat]
            self.mycursor.execute(sql, value)
            val1 = self.mycursor.fetchall()
            for x in val1:
                v1 = int(x[0])
                if v1==1:
                    print("Category Alredy Exists, Enter Different Category!!!")
                    ob1.cat_Add()
                else:
                    v2=input("Are You Sure, You Want to Add This Category? PRESS y/n : ")
                    if v2=="y":
                        sql = "insert into category(name) values(%s)"
                        values = [self.newcat]    
                        self.mycursor.execute(sql,values)
                        self.mydb.commit()
                        print("!! CATEGORY successfully added !!")
                    else:
                        print("!! Aborted !!")
    # Deleting category
    def cat_Del(self, cat_id):
        self.cat_id = cat_id
        sql = "delete from category where cat_id=%s "
        values = [self.cat_id]
        self.mycursor.execute(sql, values)
        self.mydb.commit()
        print("!! CATEGORY successfully Deleted !!")

    #__brand_table_
    def brand_display(self):
        sql = "select * from brand"
        self.mycursor.execute(sql)
        myval = self.mycursor.fetchall()
        for x in myval:
            print("ID->", x)
    # Adding Brand
    def brand_Add(self):
        self.name = input("enter new Brand : ")
        if self.name == "":
            print("field can not be NULL")
            ob1.brand_Add()
        if self.name >="a" or self.name<="z":
            print("use only capital letters")
            ob1.brand_Add()     
        else:
            sql = "insert into brand(brand_name) values(%s)"
            values = [self.name]
            self.mycursor.execute(sql, values)
            self.mydb.commit()
            print("!! BRAND successfully added !!")
    # Deleting Brand
    def brand_Del(self):
        self.brand_id = input("Enter Brand ID : ")
        if self.brand_id=="":
            print("NULL value, Please Re-Enter !!")
            ob1.brand_Del()
        else:
            sql = "select count(brand_id) from brand where brand_id=%s"
            value = [self.brand_id]
            self.mycursor.execute(sql,value)
            val1 = self.mycursor.fetchall()
            for x in val1:
                v1= int(x[0])
                if v1==1:
                    ch1 = input("Are You Sure,You Want To Delete ? PRESS -> y/n  ")
                    if ch1=="y":
                        sql = "delete from brand where brand_id=%s "
                        values = [self.brand_id]
                        self.mycursor.execute(sql, values)
                        self.mydb.commit()
                        print("!! BRAND successfully Deleted !!")
                    else:
                        print("!!!Aborted !!!")                 
                else:
                    print("Brand ID does not exists,Please Re-Enter !!")
                    ob1.brand_Del()
    #customer_add
    def cust_Add(self):
        


                    
# class calling --
ob1 = master()
