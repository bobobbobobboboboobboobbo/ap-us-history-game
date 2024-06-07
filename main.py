file_number = int(input ("""pick your adventure
1. ride of paul revere
2. battle of tripoli
                         choice: """)) -1
file_list = ["f1.text", "f2.text", 0, 0] #add your own file here to use.
current_file = file_list [file_number]
current_file = open(current_file, "r")
context = current_file.read ()
key = input ("key: ")
while True:
    import google.generativeai as genai
    import time
    promptnum = 0
    model = ''
    error = False
    user_input =''
    while True:
        genai.configure(api_key=key) 
        if error == False: 
            time.sleep (0.1)
            print ("_________________________________________________")
            user_input = input ("input: ")
            model = 'gemini-1.5-flash-latest'
            k = False
        try:
            if k==False: total_input = context + "\n" + user_input
            model = genai.GenerativeModel(model)
            response = model.generate_content(total_input)
            print ("_____________________________________________________________")
            print("\n\n\n"+response.text )
            if k == False: context = context + "\n" + response.text + "\n"
            error = False
        except: 
            print (" \n \n \n \n _________________________ \n AN ERROR HAS OCCURED WARNING WARNING AN ERROR HAS OCCURED \n ____________________________________")
            print ("this is the context just in case you need to restart. in the event of an infinite error chain restart the game and input this as you first input:  " + context, end='\n')
            input ("do you understand. once you give an input here the error chain may or may not continue. if it doesn't keep playing, if it does resart and insert the context you copied: ")
            break
print (promptnum)
