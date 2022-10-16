
def intro():
    """Tells the Player the rules

    Returns:
        (Boolean): Begins the loop 
    """
    print(f"Hello and welcome to my quiz.\nYou will be given a series of questions will get 3 attempts to answer per question\nbe sure to have fun!")
    return True

def check_ans(question, ans, attempts, score): 
    """Checks if answer is correct, changes attmepts and score

    Args:
        question (String): Idk the question
        ans (String): The answer to the question
        attempts (Integer): How much more tries the player has for the question
        score (Integer): How much questions the player has gotten right

    Returns:
        (Boolean): _description_
    """
   
    if quiz[question]['answer'].lower() == ans.lower():
        print(f"Well done!")
        return True
    else:
        print(f"Unlucky! You have {attempts - 1} left. Try again...")
        return False

quiz = { #This is the library containing the questions
1 : {
        "question" : "What is the capital of France?",
        "answer" : "Paris"
    },
2 : {
         "question" : "What is 8*6?",
         "answer" : "40"
    },
}

intro()
while True:
    score = 0
    for question in quiz:
        attempts = 3 #The attempts you have for each question
        while attempts > 0: #This loop will break after the player loses their 3 attempts
            print(quiz[question]["question"]) 
            answer = input("Enter Answer:")
            check = check_ans(question, answer, attempts, score) #Checks if the answer inputted is correct
            if check: #If it returns True
                score += 1
                break #Automatically breaks the loop if the answer is correct
        attempts -= 1
    break
    
print("\n")
print(f"Your final score is {score}!\n")
print(f"Thanks for playing my quiz! :|")