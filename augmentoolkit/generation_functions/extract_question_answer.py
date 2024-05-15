import re


def extract_question_answer(response):
    # Define the regex pattern to match the question and answer
    # print("\n\n===\/====\n\nEXTRACT QUESTION ANSWER RESPONSE: ")
    # print(response)
    # print("\n\n\n====/\====\n\n")
    pattern = r"### Question Rewording:\n\*\*QUESTION:\*\*\s*((?:.|\n)*?)\s*\*\*ANSWER:\*\*\s*((?:.|\n)*)"

    # Search for the pattern in the response
    match = re.search(pattern, response)

    # Extract and return the question and answer if a match is found
    if match:
        question = match.group(1).strip()
        answer = match.group(2).strip()
        return question, answer
    else:
        response = response.replace("\\n","\n")
        response = response.replace("\\\"","\"")
        match = re.search(pattern, response)
        if match:
            question = match.group(1).strip()
            answer = match.group(2).strip()
            return question, answer
        else:
            print("Returned none, failed to match")
            print(response)
            return None, None
