import os
def main():

    x = "C:\\Users\\Jenam\\Pictures\\digital painting backgrounds\\"
    for count, filename in enumerate(os.listdir(x)):
        dst = str(count) + ".jpg"
        src =x + filename
        dst =x + dst
          
        # rename() function will
        # rename all the files
        print(os.rename(src, dst))
  
# Driver Code
if __name__ == '__main__':
      
    # Calling main() function
    main()