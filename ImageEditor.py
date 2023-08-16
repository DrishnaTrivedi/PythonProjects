from PIL import Image,ImageFilter
print("Welcome to the image editor app !!")
img= input("Paste the img path here: ")
def filter():
    f = input("Which filter to be applied ? \nBLUR, DETAIL,EDGEENHANCE,SHARPEN,SMOOTH: ")
    if (f == "BLUR" or f == "blur"):
        img1 = img.filter(ImageFilter.BLUR)
        img1.save("Blur.jpg")
    elif(f == "DETAIL" or f ==  "detail"):
        img1 = img.filter(ImageFilter.DETAIL)
        img1.save("Detail.jpg")
    elif (f == "EDGE_ENHANCE" or f == "edge_enhance"):
        img1 = img.filter(ImageFilter.EDGE_ENHANCE)
        img1.save("EDGE_ENHANCE.jpg")
    elif (f == "SHARPEN" or f == "sharpen"):
        img1 = img.filter(ImageFilter.SHARPEN)
        img1.save("SHARPEN.jpg")
    else:
        img1 = img.filter(ImageFilter.SHARPEN)
        img1.save("SMOOTH.jpg")
def crop():
    l,r,u,d= input("Enter size to be cropped from all sides: ").split(",")
    area= (int(l),int(r),int(u),int(d))
    img1 = img.crop(area)
    img1.save("CroppedImg.jpg")

inp = input("enter the operation you want to perform: \nCROP,ROTATE,RESIZE,FILTER? ")
with Image.open(img)as img:

    if(inp == "FILTER" or inp == "filter"):
        filter()
    elif(inp=="CROP" or inp == "crop"):
        crop()
    elif(inp=="ROTATE" or inp == "rotate"):
        x= int(input("enter the angle of rotation: "))
        img=img.rotate(x)
        img.save("Rotated.jpg")
    elif(inp=="RESIZE" or inp == "resize"):
        w,h = input("enter the width and height ").split(",")
        img1 = img.resize((int(w),int(h)))
        img1.save("RESIZED.jpg")
    else:
        raise Exception("Enter valid command")




