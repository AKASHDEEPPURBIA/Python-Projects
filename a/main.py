#Creating a story

def get_input(word_type : str):
    user_input : str = input(f"Enter a {word_type}: ")
    return user_input

noun1 = get_input("noun");
noun2 = get_input("noun");
verb1 = get_input("verb");
verb2 = get_input("verb");

story = f"""
once upon a time there was wiseman called  {noun1}, who is brave, beilive in karma!

And also there was a time when he used to {verb1} cricket a lot!

But, now all he wants to {verb1} with life and get {verb2}!

But, he also want someone to take care of him! Bohot aayi bohtot gayi par koi saath
nak ruka!

Now, ALL he wants to achieve his goals, because he is born to lead the world!

"""

print(story)