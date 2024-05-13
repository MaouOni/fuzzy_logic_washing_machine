def result():
    print("------")
    print("OUTPUT")
    print("------")

    # Silk
    if ((list1[0] == "silk") and (list1[1] == "lightly soiled") and (list1[2] == "below_10kg")):
        print("Wash Duration - 0.35 h")
        print("Temperature - 30c")
        print("RPM - 400")
        print("Dry Time - Quick")
        print("Quality - Good")
    elif ((list1[0] == "silk") and (list1[1] == "lightly soiled") and (list1[2] == "10_to_15kg")):
        print("Wash Duration - 0.47 h")
        print("Temperature - 30c")
        print("RPM - 600")
        print("Dry Time - Intermediate")
        print("Quality - Good")
    elif ((list1[0] == "silk") and (list1[1] == "lightly soiled") and (list1[2] == "above_15kg")):
        print("Wash Duration - 0.50 h")
        print("Temperature - 40c")
        print("RPM - 600")
        print("Dry Time - Intermediate")
        print("Quality - Best")
    elif ((list1[0] == "silk") and (list1[1] == "normally soiled") and (list1[2] == "below_10kg")):
        print("Wash Duration - 0.50 h")
        print("Temperature - 30c")
        print("RPM - 400")
        print("Dry Time - Long")
        print("Quality - Medium")
    elif ((list1[0] == "silk") and (list1[1] == "normally soiled") and (list1[2] == "10_to_15kg")):
        print("Wash Duration - 1.18 h")
        print("Temperature - 30c")
        print("RPM - 800")
        print("Dry Time - Quick")
        print("Quality - Good")
    elif ((list1[0] == "silk") and (list1[1] == "normally soiled") and (list1[2] == "above_15kg")):
        print("Wash Duration - 1.18 h")
        print("Temperature - 40c")
        print("RPM - 600")
        print("Dry Time - Long")
        print("Quality - Medium")
    elif ((list1[0] == "silk") and (list1[1] == "heavily soiled") and (list1[2] == "below_10kg")):
        print("Wash Duration - 0.50 h")
        print("Temperature - 30c")
        print("RPM - 800")
        print("Dry Time - Intermediate")
        print("Quality - Good")
    elif ((list1[0] == "silk") and (list1[1] == "heavily soiled") and (list1[2] == "10_to_15kg")):
        print("Wash Duration - 1.18 h")
        print("Temperature - 40c")
        print("RPM - 800")
        print("Dry Time - Quick")
        print("Quality - Best")
    elif ((list1[0] == "silk") and (list1[1] == "heavily soiled") and (list1[2] == "above_15kg")):
        print("Wash Duration - 2.10 h")
        print("Temperature - 40c")
        print("RPM - 800")
        print("Dry Time - Quick")
        print("Quality - Best")

    # Woolen
    elif ((list1[0] == "woolen") and (list1[1] == "lightly soiled") and (list1[2] == "below_10kg")):
        print("Wash Duration - 0.47 h")
        print("Temperature - 40c")
        print("RPM - 800")
        print("Dry Time - Long")
        print("Quality - Medium")
    elif ((list1[0] == "woolen") and (list1[1] == "lightly soiled") and (list1[2] == "10_to_15kg")):
        print("Wash Duration - 0.50 h")
        print("Temperature - 40c")
        print("RPM - 600")
        print("Dry Time - Intermediate")
        print("Quality - Good")
    elif ((list1[0] == "woolen") and (list1[1] == "lightly soiled") and (list1[2] == "above_15kg")):
        print("Wash Duration - 1.18 h")
        print("Temperature - 40c")
        print("RPM - 800")
        print("Dry Time - Quick")
        print("Quality - Good")
    elif ((list1[0] == "woolen") and (list1[1] == "normally soiled") and (list1[2] == "below_10kg")):
        print("Wash Duration - 0.50 h")
        print("Temperature - 40c")
        print("RPM - 600")
        print("Dry Time - Intermediate")
        print("Quality - Medium")
    elif ((list1[0] == "woolen") and (list1[1] == "normally soiled") and (list1[2] == "10_to_15kg")):
        print("Wash Duration - 0.50 h")
        print("Temperature - 40c")
        print("RPM - 600")
        print("Dry Time - Intermediate")
        print("Quality - Medium")
    elif ((list1[0] == "woolen") and (list1[1] == "normally soiled") and (list1[2] == "above_15kg")):
        print("Wash Duration - 1.18")
        print("Temperature - 40c")
        print("RPM - 800")
        print("Dry Time - Quick")
        print("Quality - Best")
    elif ((list1[0] == "woolen") and (list1[1] == "heavily soiled") and (list1[2] == "below_10kg")):
        print("Wash Duration - 1.18")
        print("Temperature - 60c")
        print("RPM - 800")
        print("Dry Time - Quick")
        print("Quality - Best")
    elif ((list1[0] == "woolen") and (list1[1] == "heavily soiled") and (list1[2] == "10_to_15kg")):
        print("Wash Duration - 1.18")
        print("Temperature - 40c")
        print("RPM - 1000")
        print("Dry Time - Quick")
        print("Quality - Good")
    elif ((list1[0] == "woolen") and (list1[1] == "heavily soiled") and (list1[2] == "above_15kg")):
        print("Wash Duration - 2.10 h")
        print("Temperature - 60c")
        print("RPM - 1200")
        print("Dry Time - Quick")
        print("Quality - Good")

    # Cotton
    elif ((list1[0] == "cotton") and (list1[1] == "lightly soiled") and (list1[2] == "below_10kg")):
        print("Wash Duration - 0.47 h")
        print("Temperature - 40c")
        print("RPM - 400")
        print("Dry Time - Intermediate")
        print("Quality - Good")
    elif ((list1[0] == "cotton") and (list1[1] == "lightly soiled") and (list1[2] == "10_to_15kg")):
        print("Wash Duration - 0.50 h")
        print("Temperature - 40c")
        print("RPM - 600")
        print("Dry Time - Intermediate")
        print("Quality - Good")
    elif ((list1[0] == "cotton") and (list1[1] == "lightly soiled") and (list1[2] == "above_15kg")):
        print("Wash Duration - 1.18")
        print("Temperature - 40c")
        print("RPM - Long")
        print("Dry Time - Quick")
        print("Quality - Best")
    elif ((list1[0] == "cotton") and (list1[1] == "normally soiled") and (list1[2] == "below_10kg")):
        print("Wash Duration - 0.50 h")
        print("Temperature - 40c")
        print("RPM - 600")
        print("Dry Time - Intermediate")
        print("Quality - Best")
    elif ((list1[0] == "cotton") and (list1[1] == "normally soiled") and (list1[2] == "10_to_15kg")):
        print("Wash Duration - 1.18")
        print("Temperature - 40c")
        print("RPM - 800")
        print("Dry Time - Quick")
        print("Quality - Best")
    elif ((list1[0] == "cotton") and (list1[1] == "normally soiled") and (list1[2] == "above_15kg")):
        print("Wash Duration - 2.10 h")
        print("Temperature - 40c")
        print("RPM - 1000")
        print("Dry Time - Quick")
        print("Quality - Good")
    elif ((list1[0] == "cotton") and (list1[1] == "heavily soiled") and (list1[2] == "below_10kg")):
        print("Wash Duration - Long")
        print("Temperature - 60c")
        print("RPM - 1000")
        print("Dry Time - Intermediate")
        print("Quality - Good")
    elif ((list1[0] == "cotton") and (list1[1] == "heavily soiled") and (list1[2] == "10_to_15kg")):
        print("Wash Duration - 1.18")
        print("Temperature - 60c")
        print("RPM - 1200")
        print("Dry Time - Long")
        print("Quality - Best")
    elif ((list1[0] == "cotton") and (list1[1] == "heavily soiled") and (list1[2] == "above_15kg")):
        print("Wash Duration - 2.10 h")
        print("Temperature - 60c")
        print("RPM - 1200")
        print("Dry Time - Long")
        print("Quality - Good")

    input("Press Enter key to exit...")

def fun():
    list1.append(str(input("Enter the Fabric type: ").lower()))
    list1.append(str(input("Enter the Stain category: ").lower()))
    list1.append(str(input("Enter the Fabric weight: ").lower()))
    list1.append(str(input("Enter the Water composition (detergent, water, softener): ").lower()))
    list1.append(str(input("Enter the Dirt type: ").lower()))
    list1.append(str(input("Enter the Dirt quantity: ").lower()))

    print(list1)
    if (((list1[0] == "cotton") or (list1[0] == "silk") or (list1[0] == "woolen")) and
            ((list1[1] == "lightly soiled") or (list1[1] == "normally soiled") or (list1[1] == "heavily soiled")) and
            ((list1[2] == "below_10kg") or (list1[2] == "10_to_15kg") or (list1[2] == "above_15kg"))):
        settings = str(input("Do you want to change the settings (YES OR NO): ").lower())
        if settings == "yes":
            list1.clear()
            fun()
        elif settings == "no":
            result()
        else:
            print("Given input is wrong, try again")
            list1.clear()
            fun()

fun()