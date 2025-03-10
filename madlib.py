def mad_libs():
    print("Welcome to Mad Libs: A Story of Home and Dreams!")
    
    # Collect user input
    name = input("Enter a name: ")
    adjective1 = input("Enter an adjective: ")
    place = input("Enter a place: ")
    noun1 = input("Enter a noun (something special): ")
    emotion = input("Enter an emotion: ")
    verb = input("Enter a verb (past tense): ")
    family_member = input("Enter a family member (e.g., mother, grandfather): ")
    adjective2 = input("Enter another adjective: ")
    noun2 = input("Enter another noun: ")
    
    # Generate story
    story = f"""
    {name} grew up in a {adjective1} village near {place}.  
    Every evening, they would hold onto their {noun1}, feeling {emotion}, dreaming of the future.  
    One day, they {verb} with their {family_member} under the {adjective2} sky,  
    listening to stories of hope, love, and the power of {noun2}.
    """
    
    print("\nHere is your Mad Libs story:\n")
    print(story)

mad_libs()