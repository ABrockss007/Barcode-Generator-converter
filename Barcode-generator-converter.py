import random
from barcode import ISBN13
from barcode.writer import ImageWriter
n = 11
terms = []
num = 0
am = ""
a_s = []
sum_13=[]
last_digit=0
lst = [0,1,2,3,4,5,6,7,8,9]
for i in range(1,10):
    a = random.choice(lst)
    a_s.append(a)
    n = n - 1
    term = a*n
    num = int(num) + int(term)
    am = am + str(a)

    terms.append(term)

for i in range(0,9):
    if i%2==0:
        term=a_s[i]*3
    else :
        term=a_s[i]*1
    sum_13.append(term)
sum13=sum(sum_13)+38
check1=int(sum13) %10
if check1==0:
    last_digit13=0
else:
    last_digit13=10-check1
am13=str(978)+am+str(last_digit13)
#print("am13 "+str(am13))
check = int(num) % 11
#print(am)
if check!=0:
    last_digit = 11 - check
am10 =am +str(last_digit)
#print(terms)
#print("l "+str(last_digit))
#print(check)
#print(am)
x=False
while(x==False):
    print("---------------WELCOME-------------")
    choice=int(input("what do you want to do ? 1) generate a random ISBN13 bar code with check digit "
          "2) Convert ISBN13 to ISBN10  3)Details of UPC Code  4) exit"))
    match choice:
        case 1:
            # import ImageWriter to generate an image file

            # Make sure to pass the number as string
            number = am13

        #   Now, let's create an object of EAN13 class and
             # pass the number with the ImageWriter() as the
        # writer
            my_code = ISBN13(number, writer=ImageWriter())

        # Our barcode is ready. Let's save it.
            my_code.save("new_code1")
            # Imports PIL module
            from PIL import Image

        # open method used to open different extension image file

            im = Image.open(r"/Users/aryan/Desktop/pythonProject/DM_Project/new_code1.png")

            # This method will show image in any image viewer
            im.show()
            print("Check digit= "+str(last_digit13))
        case 2:
            print("converting...........................")
            print("your ISBN10 code is : "+am10)
        case 3:

            x=0
            while(x!=1):
                code=input("Please put your UPC Number shown on bar code ")
                if(len(code)==12):
                    x=1
                else:
                    print("pls put correct code")
                print("-------------------DETAILS OF YOUR BAR CODE----------------")
                print("manufacture code is : "+code[1:6])
                print("product code is : "+code[7:12])
        case 4:
            x=True


