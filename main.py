#!/usr/bin/env python3

import os, sys, time

w = '\033[0m'
b = '\033[1;94m'
d = '\033[90m'
webwarp = f'{d}<{b}webwarp{d}>{w}'

# This function checks that all necessary requirements have been met
def check_requirements():
    pass

# If the necessary requirements havent been met yet this function installs them
def install_requirements():
    os.system("pip install -r requirements.txt")

# This function creates the typing effect
def prints(text):
    for line in text:
        print(line, end='', flush=True)
        time.sleep(0.008)
    print('')


def decompile_apk(x):
    os.system("java -jar apktool.jar d test.apk")

def modify_apk(x, y, z):
    pass

def compile_apk(x):
    os.system(f'''java -jar apktool.jar b test -o test.apk''')
    pass

def sign_apk(x):
    os.system(f'''java -jar uber-apk-signer.jar {x}''')

def main():
    os.system("clear||cls")

    prints(f''' 
{webwarp} : Hello user, welcome to Web-Warp

{webwarp} : WebWarp is a convenient solution to convert your website into an APK file.

{webwarp} : how can i help you ?

          (1) Convert web To mobile (apk)
          (2) exit!
''')
    
    try:
        choice= int(input("Select: "))
    except:
        print("Invalid Choice")
        main()

    if choice == 1:
        os.system("clear||cls")
        try:
            url= str(input("Set Website URL(https://example.com): "))
            name= str(input("Set App Name: "))
            icon= str(input("Set App Icon: "))

            #decompile the apk to raw native code    
            decompile_apk()
            print("Decompilation complete")
           
            #modify the native code
            modify_apk(url,name, icon)
            print("modification Complete")

            #compile The apk
            compile_apk(name)
            print("Compilation complete")
           
            #Sign The apk
            sign_apk(name)
            print("Your apk is Ready")
              
        except:
            print(f''' 
        `   {webwarp} : Error
            ''')
            time.sleep(5)
            main()
        pass

    else:
        exit()


if __name__ == "__main__":
    main()