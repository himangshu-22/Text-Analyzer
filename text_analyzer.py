user_input = input("enter the text: ")
print("Total Number of characters:", len(user_input))

ch_wo_space= user_input.replace(" ","")
print("Number of characters without space:", len(ch_wo_space))

no_of_words = user_input.split()
print("Total Number of words:", len(no_of_words))