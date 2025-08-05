marks=[]
n=int(input("how many students? "))
for i in range(n):
    mark=float(input(f"Enter marks for student {i+1}: "))
    marks.append(mark)
total=0
for mark in marks:
    total+=mark
Average= total/len(marks)
maximum=max(marks)
minimum=min(marks)
while True:
    print("\nwhat do you want to do: ")
    print("1.Total marks")
    print("2.Average marks")
    print("3.Highest marks")
    print("4.Lowest marks")
    print("Type 'exit' to quit")

    choice = input("Enter you choice:(1/2/3/4): ")
    if choice == '1':
        print("total marks: ", total)
    elif choice == '2':
        print("Average marks: ", Average)
    elif choice == '3':
        print("Highest marks: ", maximum)
    elif choice == '4':
        print("Lowest marks: ", minimum)
    elif choice=='exit':
        print("exiting the program. Goodbye")
        break
    else:
        print("invalid choice. please enter 1,2,3,4, or 'exit'. ")
