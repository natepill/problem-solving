
jsonArray = [
    {
        "receiver": "amy@yelp.com",
        "message": "They helped me get unblocked",
        "sender": "dorothy@yelp.com"
    },
    {
        "receiver": "bailey@yelp.com",
        "message": "They helped me get unblocked",
        "sender": "dorothy@yelp.com"
    },
     {
        "receiver": "dorothy@yelp.com",
        "message": "They were a fun interviewer",
        "sender": "cenz@yelp.com"
    },
    {
        "receiver": "amy@yelp.com",
        "message": "They helped me get unblocked",
        "sender": "dorothy@yelp.com"
    }]



def employee_review_tally(love_sent):

    "Takes in JSON array of employee reviews and returns a dictionary with key: employee email and value: tally of positive reviews"

    employee_dict = {}
    for review in love_sent:
        if review['receiver'] in employee_dict:
            employee_dict[review['receiver']] += 1
        else:
            employee_dict[review['receiver']] = 1

    # print(employee_dict)
    return employee_dict

def most_positive_feedback(love_sent, k):

    ''''Takes in array of JSON objects and number of emails to return. Returns list of 'k' number of emails of the employees with the most love '''
    employee_tally = employee_review_tally(love_sent)
    # print(employee_tally)
    loved_employees = list()


    zipped_list = sorted(zip(employee_tally.values(), employee_tally.keys())) #zips dictionary to create a sorted list of tuples with (value,email)

    # most_loved_list = zipped_list[::-k]
    # print('zipped_list:', zipped_list)
    list_of_emails = list()
    for employee in reversed(zipped_list):
        list_of_emails.append(employee[1])

    # print(list_of_emails[:k])
    return list_of_emails[:k]



# Question 2
# How would you find `k` employees that sent the most love (positive feedback) on other employees
# • Same constraints for input and output as above


def employee_reviewer_tally(love_sent):
    employee_dict = {}
    for review in love_sent:
        if review['sender'] in employee_dict:
            employee_dict[review['sender']] += 1
        else:
            employee_dict[review['sender']] = 1

    # print(employee_dict)
    return employee_dict


def sent_most_love(love_sent, k):

    ''''Takes in array of JSON objects and number of emails to return. Returns list of 'k' number of emails of the employees with the most love '''
    employee_tally = employee_reviewer_tally(love_sent)
    # print(employee_tally)
    loved_employees = list()


    zipped_list = sorted(zip(employee_tally.values(), employee_tally.keys()))

    # most_loved_list = zipped_list[::-k]
    # print('zipped_list:', zipped_list)
    list_of_emails = list()
    for employee in reversed(zipped_list):
        list_of_emails.append(employee[1])

    # print(list_of_emails[:k])
    return list_of_emails[:k]


def main():
    'Edit first function for Q1, and second function for Q2'

    print('Employees who GOT most postive feedback:', most_positive_feedback(jsonArray, 2))
    print('Employees who SENT most postive feedback:', sent_most_love(jsonArray, 1))

if __name__ == "__main__":m
    main()
