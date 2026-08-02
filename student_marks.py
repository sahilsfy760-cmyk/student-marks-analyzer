def student_data():
    number=("First","Second","Third","Fourth","Fifth","Sixth","Seventh","Eighth","Ninth","Tenth")
    
    #marks is main list
    marks=[]
    
    #take input from the user
    for  i in number:
        num=int(input(f"Enter {i} student marks: "))
        print()
        marks.append(num)
        
     # conver into tuple
    marks_student=tuple(marks)         
    
    #count total
    total_marks=0
    
    for i in marks:
        total_marks+=i
        
    
    # find avarage
    avg=total_marks/len(marks)

    
    # find largest marks
    largest_mark=marks[0]
    for i in marks:
        if i > largest_mark:
            largest_mark=i
    
    #find lowest mark
    lowest_mark=marks[0]
    for i in marks:
        if i < lowest_mark:
            lowest_mark=i

    
    #find even marks
    even_marks=[i for i in marks if i%2==0]
    
    #find odd marks
    odd_marks=[i for i in marks if i%2!=0]

    
    
    # find unique marks
    unique_marks=[]
    for i in marks:
        if i not in unique_marks:
            unique_marks.append(i)
            
    #sort marks
    unique_marks1= unique_marks.copy()
    unique_marks1.sort()
    
    #count pass and fail students
    pass_students=[]
    fail_students=[]
    for i in marks:
        if i>=35 and i<=100:
            pass_students.append(i)
        elif i>=0 and i<=34:
            fail_students.append(i)
        elif i<0 or i>100:
            print(f"{i} is invalid marks")
            break
    print()
      
    grade_a=[]
    grade_b=[]
    grade_c=[]
    grade_d=[]
    fail=[]           
    for i in marks:
          if 90<= i <=100:
                grade_a.append(i)
          if 75<= i <=89:
                grade_b.append(i)                
          if 60<= i <=74:
                grade_c.append(i)         
          if 35<= i <=59:
                grade_d.append(i)
          if 0<= i <=34:
                fail.append(i)                        
            
    for i,j in zip(marks,number):
         if i in grade_a:
             print(f"{f'{j} Student Grade is':<24}: A")
         if i in grade_b:
             print(f"{f'{j} Student Grade is':<24}: B")
         if i in grade_c:
             print(f"{f'{j} Student Grade is':<24}: C")   
         if i in grade_d:
             print(f"{f'{j} Student Grade is':<24}: D")
         if i in fail:
             print(f"{f'{j} Student Grade is':<24}: Fail")
    print()        
    topper_marks = []                  
    for i in marks:
        if i>75:
            topper_marks.append(i)
    print(f"{'Topper student marks in list':<24}: {topper_marks}")
    topper_marks=tuple(topper_marks)
    print(f"{'Topper student marks in tuple':<24}: {topper_marks}")
    print()        
    print(f"{'Student marks in list':<24}: {marks}")
    print(f"{'Student marks in tuple':<24}: {marks_student}")
    print(f"{'Total marks':<24}: {total_marks}")
    print(f"{'Average':<24}: {avg}")
    print(f"{'Largest mark':<24}: {largest_mark}")
    print(f"{'Lowest mark':<24}: {lowest_mark}")
    print(f"{'Even marks':<24}: {even_marks}")
    print(f"{'Odd marks':<24}: {odd_marks}")
    print(f"{'Unique marks':<24}: {unique_marks}")
    print(f"{'Sorted unique list':<24}: {unique_marks1}")
    print(f"{'Pass Students':<24}: {len(pass_students)}")
    print(f"{'Fail Students':<24}: {len(fail_students)}")
    print()
    run_again=input("Do you want to analyze another class? (Y/N):")
    if run_again=="y" or run_again=="Y":
         student_data()
    elif run_again=="n" or run_again=="N"  :
         print("Thank you")
    else:
         print("invalid input")
         
      
         

student_data()
        