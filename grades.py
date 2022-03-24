def grades(nom, marks):

    if 70 <= marks <= 100:
        print('A is your grade ' + nom)

    elif 60 <= marks < 70:
        print(f"{nom} well done, you scored a B ")

    elif 50 <= marks < 60:
        print(f"{nom} , try harder next time a C isn't bad ")

    elif 40 <= marks < 50:
        print('D')

    else:
        print('Fail! ')

    print(marks)













# if __name__=='__main__':
#     a = str(input("nom: "))
#     b = float(input("enter your grade"))
#     grades(a, b)

# def displaytest():
#     print("boom")