"""
Lab 4:
"""

def main():
    feedback = get_feedback(15, 20)
    print(feedback)
##    print(get_feedback(100, 200))
##    print(get_feedback(65, 90))
##    print(get_feedback(30, 30))

def get_feedback(mark, out_of):
    percentage = (mark / out_of) * 100
    percentage_rounded = round(percentage)
    if percentage_rounded >= 80:
        mark_feedback = "Excellent"
        return mark_feedback
    elif percentage_rounded >= 60 and percentage_rounded <= 79:
        mark_feedback = "Good"
        return mark_feedback
    elif percentage_rounded >= 50 and percentage_rounded <= 59:
        mark_feedback = "Pass"
        return mark_feedback
    else:
        mark_feedback = "Not a pass"
        return mark_feedback
    return

main()








