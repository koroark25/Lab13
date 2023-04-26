#Emliy Nixon and Katie O'Rourke
file_open=open("text.txt","w")
line1="The #fitnessgram pacer test is a multistage aerobic capacity test"
file_open.write(line1)
line2="that progressively gets more #difficult as it continues."
file_open.write(line2)
line3="The #20 meter pacer test will begin in 30 seconds."
file_open.write(line3)
line4="Line up at the #start."
file_open.write(line4)
line5="The #running speed starts slowly, but gets #faster each minute"
file_open.write(line5)
line6="A single lap should be #completed each time you hear the sound."
file_open.write(line6)
file_open.close()

import re

def get_hashtag_ranking(input_sentence):
    hashtag_list = re.findall(r"#\w+", input_sentence)

    hashtag_count = {}
    for hashtag in hashtag_list:
        if hashtag in hashtag_count:
            hashtag_count[hashtag] += 1
        else:
            hashtag_count[hashtag] = 1

    def get_frequency(hashtag_count_pair):
        return hashtag_count_pair[1]

    sorted_hashtags = sorted(hashtag_count.items(), key = get_frequency, reverse=True)

    output_list = [hashtag for (hashtag, count) in sorted_hashtags]

    return output_list

file = open("text.txt", "r")
for n in file:
    print(get_hashtag_ranking(n))
