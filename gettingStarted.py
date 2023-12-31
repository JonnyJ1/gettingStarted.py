# welcome_assignment_answers
# Input - All eight questions given in the assignment.
# Output - The right answer for the specific question.

def welcome_assignment_answers(question):
    if question == "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?":
        answer = "pcap"
    elif question == "Are encoding and encryption the same? - Yes/No":
        answer = "No"
    elif question == "Is it possible to decrypt a message without a key? - Yes/No":
        answer = "No"
    elif question == "Is it possible to decode a message without a key? - Yes/No":
        answer = "Yes"
    elif question == "Is a hashed message supposed to be un-hashed? - Yes/No":
        answer = "No"
    elif question == "What is the SHA256 hashing value of your NYU email and use the answer in your code - ":
        answer = "1e10d90c9436023872eca2b73c5972876a1dff9c6223d77a244270148cc8739c"
    elif question == "Is MD5 a secured hashing algorithm? - Yes/No":
        answer = "No"
    elif question == "What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number":
        answer = 5
    elif question == "What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number":
        answer = 3

    else:
        answer = "This is not the answer you're looking for."
    return answer
# Complete all the questions.


if __name__ == "__main__":
    # use this space to debug and verify that the program works
    questions = ["Are encoding and encryption the same? - Yes/No", "Is it possible to decrypt a message without a key?"
                 " - Yes/No", "Is it possible to decode a message without a key? - Yes/No", "Is a hashed message"
                 " supposed to be un-hashed? - Yes/No", "What is the SHA256 hashing value of your NYU email and use the answer in your code - ", "Is MD5 a secured"
                 " hashing algorithm? - Yes/No", "What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number", "What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number", "In Slack, what is the secret passphrase posted in the"
                 " #lab-python-getting-started channel posted by a TA?"]
    for debug_question in questions:
        print(debug_question)
        print(welcome_assignment_answers(debug_question))
        
