db={"name": "siddharth","city":"pune","passing_year":2024,"course":"python"}
print("-"*100)
print(F"{" "*45}THE KIRAN ACADEMY{" "*45}")
print("-"*100)
while True:
    print("""
                DASHBOARD
          1.Add student data
          2.display data
          3.update student data
          4.delete student data
          5.filter""")
    choice=int(input("Enter your choice:"))
    if choice==1:
        name=input("Enter student name:")
        city=input("Enter student city:")
        passing_year=int(input("Enter student passing year:"))
        course=input("Enter student course:")
        db[name]={"city":city,"passing_year":passing_year,"course":course}
        print("Data added successfully")
        print("-"*100)
    elif choice==2:
        print(db)
        print("-"*100)
    elif choice==3:
        name=input("Enter student name to update:")
        if name in db:
            city=input("Enter new student city:")
            passing_year=int(input("Enter new student passing year:"))
            course=input("Enter new student course:")
            db[name]={"city":city,"passing_year":passing_year,"course":course}
            print("Data updated successfully")
        else:
            print("Student not found")
        print("-"*100)
    elif choice==4:
        name=input("Enter student name to delete:")
        if name in db:
            del db[name]
            print("Data deleted successfully")
        else:
            print("Student not found")
        print("-"*100)
    elif choice==5:
        print("Enter the criteria to filter data:")
        criteria=input("Enter criteria(city/passing_year/course):")
        if criteria=="city":
            city=input("Enter city:")
            filtered_data={k:v for k,v in db.items() if v["city"].lower()==city.lower()}
            print(filtered_data)
        elif criteria=="passing_year":
            passing_year=int(input("Enter passing year:"))
            filtered_data={k:v for k,v in db.items() if v["passing_year"]==passing_year}
            print(filtered_data)
        elif criteria=="course":
            course=input("Enter course:")
            filtered_data={k:v for k,v in db.items() if v["course"].lower()==course.lower()}
            print(filtered_data)
        else:
            print("Invalid criteria")
        print("-"*100)
    else:
        print("Invalid choice")
        print("-"*100)
        break