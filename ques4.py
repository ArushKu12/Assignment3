from prettytable import PrettyTable
#making an object from the class
my_table = PrettyTable()
my_table.add_column("Letter grade", ["A+", "A", "B+", "B", "C+", "C", "D"])
my_table.add_column("Performance",
                    ["Outstanding", "Excellent", "Very Good", "Good", "Average", "Below Average", "Poor"])
my_table.add_column("Grade Points", [10, 9, 8, 7, 6, 5, 4])
print(my_table)
grade_point = int(input("Enter the grade point: "))
grading_method = {
    10: ["Outstanding", "A+"],
    9: ["Excellent", "A"],
    8: ["Very Good", "B+"],
    7: ["Good", "B"],
    6: ["Average", "C+"],
    5: ["Below Average", "C"],
    4: ["Poor", "D"]
}
if grade_point in range(4, 11):
    print(f"Your Grade is '{grading_method[grade_point][1]}' and {grading_method[grade_point][0]}")
else:
    print("Error")
