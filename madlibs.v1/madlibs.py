from random import choice


def extract_a_story(datafile):
    stories = {}
    num = 0
    with open(datafile, 'r') as file:
        for line in file.readlines():
            if "-starts-" in line:
                num += 1
                stories['story' + str(num)] = ""
                continue
            else:
                stories['story' + str(num)] += line
    random_pick = choice(list(stories.values()))
    return random_pick

# print(extract_a_story('madlibs_stories.txt'))

def find_patters(story, replace_with = None):
    index = 0
    types = []
    replace_with_index = 0
    while index < len(story):
        if not replace_with:
            if story[index] == "{" and story[index + 1] == "{":
                index = index + 2
                thetype = ""
                while (story[index] != "}" or story[index + 1] != "}"):
                    thetype += story[index]
                    index += 1
                types.append(thetype)
            index += 1
        else:

            if story[index] == "(":
                index = index + 1
                digit = ""
                while story[index] != ")":
                    digit += story[index]
                    index += 1
                if digit.isdigit() and story[index] == ")":
                    index = index + 2
                    start = index
                    while story[index] != "{" or story[index + 1] != "{":
                        index += 1
                    end = index

                    story = story[:start] + " " + replace_with[replace_with_index] + " " + story[end: ]
                    replace_with_index += 1
            index += 1     


    return types, story

#print(find_patters(extract_a_story('madlibs_stories.txt'))

def take_inputs(types):
    user_inputs = []
    num = 1
    for type in types:
        print(f"({num}) {type}")
        user_inputs.append(input("Your Input: "))
        num += 1
    return user_inputs

# print(take_inputs(find_patters(extract_a_story('madlibs_stories.txt'))[0]))

def final_story(user_inputs):
    story = extract_a_story('madlibs_stories.txt')
    return find_patters(story, user_inputs)[1]

def main():
    # display the story
    story = extract_a_story('madlibs_stories.txt')
    print("\n\n MAD LIBS \n\n")
    print(story)

    types = find_patters(story)[0]
    user_inputs = take_inputs(types)
    final_story = find_patters(story, user_inputs)[1]
    print("\n\n\n")
    print(final_story)

# start game    
main()
