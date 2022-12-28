from time import sleep
import random


INTRO_HAS_RAN = False
NAME_CHOSEN = False

leaderboard = {
    "Bob": 1,
    "Tim": 4,
    "Jim": 0,
    "Bartholamew": 10,
}

hardware_questions = {
    1: {
        "question": "What does the R in ROM stand for?",
        "answer": "Read"
    },
    2: {
        "question": "What does ALU stand for?",
        "answer": "Arithmetic Logic Unit"
    },
    3: {
        "question": "What does the R in RAM stand for?",
        "answer": "Random"
    },
    4: {
        "question": "Which type of main memory storage is closest to the CPU?",
        "answer": "Registers"
    },
    5: {
        "question": "What is the fastest type of Cache?",
        "answer": "L1"
    },
    6: {
        "question": "What is the main circuit board of computers?",
        "answer": "Motherboard"
    },
    7: {
        "question": "What's the architecture which many general purpose computers are based on?",
        "answer": "Von Neumann Architecture"
    },
    8: {
        "question": "What word describes RAM losing it's data when the computer is powered off?",
        "answer": "Volatile"
    },
    9: {
        "question": "What part of the computer is the BIOS stored?",
        "answer": "Rom"
    },
    10: {
        "question": "True or False - Optical storage devices have no moving parts.",
        "answer": "False"
    },
}

network_questions = {
    1: {
        "question": "What represents the connections in a network?",
        "answer": "Edges"
    },
    2: {
        "question": "What represents the devices in a network?",
        "answer": "Nodes"
    },
    3: {
        "question": "Can devices in peer-to-peer networks act as the client and server (Yes/No)?",
        "answer": "Yes"
    },
    4: {
        "question": "What is the most common network topology?",
        "answer": "Mesh"
    },
    5: {
        "question": "What is the top layer of the TCP/IP model?",
        "answer": "Application Layer"
    },
    6: {
        "question": "What is the cheapest network topology?",
        "answer": "Bus"
    },
    7: {
        "question": "Which of these is a Link Layer Protcol: UDP, WIFI, IP, TCP, IMAP",
        "answer": "Wifi"
    },
    8: {
        "question": "What type of tranmission media has the highest bandwith?",
        "answer": "Fibre Optic"
    },
    9: {
        "question": "What word is the delay between a signal being sent and received?",
        "answer": "Latency"
    },
    10: {
        "question": "What's the type of computer network used over large areas (abbreviation)?",
        "answer": "Wan"
    },
}

all_quizzes = {
    1: hardware_questions,
    2: network_questions,
}


def quiz_selection(score):
    """Lets the user select which quiz they want to do,
    more efficient than indivisual subroutines especially
    with a larger amount of topics.

    Args:
        score (int): The players score earnt by getting questions right.
    """
    print("Welcome to Quiz Selection",
          "Press 1 to attempt Hardware Quiz",
          "Press 2 to attempt Network Quiz")
    try:
        user_input = int(input())
        score = quiz(all_quizzes[user_input], score)
    except KeyError:
        # An error that would happen if python tries to find a dictionary key that doesn't exist.
        print("Invalid. Try Again: ")
        sleep(1)
    sleep(1)
    print(f"Finished! Your score is {score}.")
    global NAME_CHOSEN
    while True:
        try:
            if NAME_CHOSEN is False:
                name = input(
                    "Your score will be added to the leaderboard.\nEnter your name: ")
                NAME_CHOSEN = True
                intro()
            leaderboard.update({name.capitalize(): score})
            if name == "":
                raise ValueError
            break
        except ValueError:
            print("Please Enter Something")
            sleep(1)
    sleep(1)
    print("You will now be sent to the Main Menu:")


def check_answer(quiz_arg, question_arg, answer_arg, attempts_arg):
    """This function checks whether the user has entered in the correct
    answer to the current question and then returns a boolean value
    depending on that.

    Args:
        quiz_arg (dict): The dictionary containing the questions of the current quiz topic.
        question_arg (int): The current question number that is being attempted.
        answer_arg (str): The answer provided by the user.
        attempts_arg (int): The current amount of attempts the user has for the current question.

    Returns:
        bool: Boolean value depending on whether the user got the question right or wrong
    """
    if quiz_arg[question_arg]['answer'] == answer_arg.title():
        print("Correct!")
        return True
    # Everything in this function below this will only run if the if statement above is false,
    # because otherwise the return statement runs and ends the function. So I dont need to use else.
    print(f"Incorrect! You have {attempts_arg - 1} attempts left.")
    if attempts_arg == 1:
        print("You ran out of tries")
        print(f"The answer was '{quiz_arg[question_arg]['answer']}'")
    return False


def quiz(questions_dict, score):
    """The actual revision quiz. Goes through a dictionary of questions
    in a random order and lets the user enter in an answer for them,
    given a limited amount of attempts

    Args:
        questions_dict (dict): The dictionary containing the questions of the current topic.
        score (int): The score of the user earnt by getting questions right.

    Returns:
        int: The score of the user after finishing the quiz.
    """
    questions_dict_list = list(questions_dict.items())
    random.shuffle(questions_dict_list)
    questions_dict = dict(questions_dict_list)
    for key, questions in questions_dict.items():
        if "True" in questions['question'] or "Yes" in questions['question']:
            attempts = 1
        else:
            attempts = 3
        while attempts > 0:
            print(questions['question'])
            answer = input("Enter Answer: ")
            check = check_answer(questions_dict, key, answer, attempts)
            if check:
                score += 1
                break
            attempts -= 1
    return score


def intro():
    """Just the introduction to the revision quiz code.
    """
    print("""
Hello, Welcome to this Computer Science Revision Quiz!
You can test yourself against two different topics, hardware and networks.
After selecting a topic to do, you will be asked a series of questions and be given
a few attempts to answer them. Your score will increase every question you get right
and you'll be told your result after completing the quiz.
""")
    sleep(5)
    print("There isn't much else to this, so now you'll be directerd to the main menu. \n")
    sleep(1)
    main()


def main():
    """The main part of the code where the player can go the selection place,
    leaderboard, or decide to the quit the program.
    """
    score = 0
    global INTRO_HAS_RAN
    if INTRO_HAS_RAN is False:
        INTRO_HAS_RAN = True
        intro()
    try:
        user_input = input("Main Menu - Press 1 to see quiz selection. Press 2 to see leaderboard. \
Press 3 to quit. \n")
        sleep(1)
        if user_input == "1":
            quiz_selection(score)
        elif user_input == "2":
            print(leaderboard)
            sleep(1)
            print("You can add/update your name on this leaderboard.")
            sleep(1)
            print("Returning to Main Menu:")
            sleep(1)
            main()
        elif user_input == "3":
            pass
        else:
            raise ValueError
    except ValueError:
        print("You have entered an invalid option. Try Again: \n")
        sleep(1)
        main()
