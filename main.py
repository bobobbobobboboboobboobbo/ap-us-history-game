file_number = int(input ("""pick your adventure
1. ride of paul revere
                         choice: """)) -1
file_list = ["f1.text", 0, 0, 0]
current_file = file_list [file_number]
current_file = open(current_file, "r")
context = current_file.read ()
while True:
    import google.generativeai as genai
    import time
    promptnum = 0
    key = 'AIzaSyAqsSXE1FJo0XvqDE8pMrVyi6r1K__ruY4'
    model = ''
    error = False
    user_input =''
    while True:
        genai.configure(api_key=key) 
        #if error==True: 
            #model = 'gemini-1.0-pro-latest'
            #error_input = 'do not output anything but a single blank space character.'
            #k = True
        if error == False: 
            time.sleep (0.1)
            user_input = input ("input: ")
            model = 'gemini-1.5-flash-latest'
            k = False
        #print ("model:", model ,"\n _______________________")
        try:
            #if k==True: total_input = error_input
            if k==False: total_input = context + "\n" + user_input
            model = genai.GenerativeModel(model)
            response = model.generate_content(total_input)
            #error = False
        
            print("\n\n\n"+response.text )
            if k == False: context = context + "\n" + response.text + "\n"
            
            #if k == True: 
                #context = context

            

            #file_number +=1
            error = False
        except: 
            #error=True
            print (" \n \n \n \n _________________________ \n AN ERROR HAS OCCURED WARNING WARNING AN ERROR HAS OCCURED \n ____________________________________")
            break
        #error = False
print (promptnum)