list1 = 'Why do you write? I write because I have an innate need to write. I write because I can’t do normal work as other people do. I write because I want to read books like the ones I write. I write because I am angry at everyone. I write because I love sitting in a room all day writing. I write because I can partake of real life only by changing it. I write because I want others, the whole world, to know what sort of life we lived, and continue to live, in Istanbul, in Turkey. I write because I love the smell of paper, pen, and ink. I write because I believe in literature, in the art of the novel, more than I believe in anything else. I write because it is a habit, a passion.'
word = input("Enter the word to be search\t")
if word in list1:
    print("The word you entered is ",word)
    count=list1.count(word, 0, len(list1))
    # print(list1.count(word))
    # print(list1s.count(word, 0, len(list1)))
    if count>10:
        new_word=input("This word lies more than 10 time, enter new word=>")
        repalce=list1.replace(word, new_word)
        print(repalce)
    else:
        print(count)
else:
    print("the word you entered is not occure")
