from tkinter import *

root = Tk()
root.title("Fibonacci series")
root.geometry("400x400")

label_series = Label(root, text="Fibonacci Series: ")
label_flower = Label(root)
label_spiral = Label(root)

def fibonacci():
    num = 10
    first_no = 0
    second_no = 1
    sum = 1
    counter = 1
    # fibonacci sereis upto 10 numbers:
    # 1 1 2 3 5 8 13 21 34 55
    while counter <= num:
        label_series["text"] += str(sum) + ' '
        sum = first_no + second_no
        first_no = second_no
        second_no = sum
        counter += 1
    label_flower["text"] = "Flower is fully bloomed"


btn = Button(root, command=fibonacci, text="Show fibonacci series", relief=SUNKEN)

btn.pack()
label_series.pack()
label_flower.pack()

root.mainloop()
