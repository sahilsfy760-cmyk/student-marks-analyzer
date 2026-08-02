def student_data():
    number=("First","Second","Third","Fourth","Fifth","Sixth","Seventh","Eighth","Ninth","Tenth")
    
    #marks is main list
    marks=[]
    
    #take input from the user
    for  i in number:
        num=int(input(f"Enter {i} student marks: "))
        marks.append(num)
        
     # conver into tuple
    marks_student=tuple(marks)
    
    # print marks
    print("studen marks in list:-",marks)
    print("student marks in tuple:-",marks_student)       
    
    #count total
    total_marks=0
    
    for i in marks:
        total_marks+=i
        
    #print total
    print("Total marks is:-",total_marks)
    
    # find avarage
    avg=total_marks/10
    print("avaragw is:-",avg)
    
    # find largest marks
    largest_mark=marks[0]
    for i in marks:
        if i > largest_mark:
            largest_mark=i
    print("largest mark is: ",largest_mark)
    
    #find lowest mark
    lowest_mark=marks[0]
    for i in marks:
        if i < lowest_mark:
            lowest_mark=i
    print("lowest mark is:-",lowest_mark)
    
    #find even marks
    even_marks=[i for i in marks if i%2==0]
    
    #find odd marks
    odd_marks=[i for i in marks if i%2!=0]
    print("Even number is:-",even_marks)
    print("Odd number is:-",odd_marks)
    
    
    # find unique marks
    unique_marks=[]
    for i in marks:
        if i not in unique_marks:
            unique_marks.append(i)
    print("unique marks is:-",unique_marks)
    
    unique_marks.sort()
    print("sorted unique list is:-",unique_marks)
    
    
        

student_data()
        