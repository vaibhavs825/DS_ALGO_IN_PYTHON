magazine = "give me one grand today night"
note = "give one grand today"

word_count = {}
for i in note.split():
    if i in word_count.keys():
        word_count[i] += 1
    else:
        word_count[i] = 1

magazine_list = list(magazine.split())
flag = 0
for word in magazine_list:
    if word not in word_count or word_count[word]<=0:
        flag = 1
        break
    else:
        word_count[word] -=1
# for word,count in word_count.items():
#     magazine_count = magazine_list.count(word)
#     if magazine_count<count:
#         flag = 1
if(flag ==1):
    print("Not Possible")
else:
    print("Possible")

