def value_gathering():
    try:
        physics_mark = int(input("Enter your physics mark: "))
        maths_mark = int(input("Enter your maths mark: "))
        chemistry_mark = int(input("Enter your chemistry mark:"))
        ov_mark = physics_mark + maths_mark + chemistry_mark
        percentage_total = (ov_mark/300) * 100
        if percentage_total >= 40 and percentage_total < 50:
            print('"D"')
        elif percentage_total >= 50 and percentage_total < 60:
            print('"C"')
        elif percentage_total >= 60 and percentage_total < 70:
            print('"B"')
        elif percentage_total >= 70:
            print('"A"')
        elif percentage_total < 40:
            print("FAIL!")
    except ValueError:
        print("Whole numbers only!")
        value_gathering()
value_gathering()