from english_words import english_words_set
# from PyDictionary import PyDictionary
import tkinter as tk

frame = tk.Tk()
frame.title("TextBox Input")
frame.geometry('450x800')

wordset = []

for eachWord in english_words_set:
    if len(eachWord) == 5:
        wordset.append(eachWord.lower())

wordList = []
wordList2 = []
wordList3 = []
wordList4 = []
turn = 0

def clear():
    global wordList
    global wordList2
    global wordList3
    global wordList4
    global turn
    wordList = []
    wordList2 = []
    wordList3 = []
    wordList4 = []
    turn = 0

def printInput():
    x = ""
    global turn
    global y
    turn = turn + 1
    if turn == 1:
        known0inp = known0.get(1.0, "end-1c")
        known1inp = known1.get(1.0, "end-1c")
        known2inp = known2.get(1.0, "end-1c")
        known3inp = known3.get(1.0, "end-1c")
        known4inp = known4.get(1.0, "end-1c")
        wrongLocation0inp = wrongLocation0.get(1.0, "end-1c")
        wrongLocation1inp = wrongLocation1.get(1.0, "end-1c")
        wrongLocation2inp = wrongLocation2.get(1.0, "end-1c")
        wrongLocation3inp = wrongLocation3.get(1.0, "end-1c")
        wrongLocation4inp = wrongLocation4.get(1.0, "end-1c")
        notNeedded0inp = notNeedded0.get(1.0, "end-1c")
        notNeedded1inp = notNeedded1.get(1.0, "end-1c")
        notNeedded2inp = notNeedded2.get(1.0, "end-1c")
        notNeedded3inp = notNeedded3.get(1.0, "end-1c")
        notNeedded4inp = notNeedded4.get(1.0, "end-1c")

        if known0inp == "":
            a = ""
        else:
            a = """ and known0inp in words[0] """
            known0.delete("1.0", tk.END)

        if known1inp == "":
            b = ""
        else:
            b = """and known1inp in words[1] """
            known1.delete("1.0", tk.END)

        if known2inp == "":
            c = ""
        else:
            c = """and known2inp in words[2] """
            known2.delete("1.0", tk.END)

        if known3inp == "":
            d = ""
        else:
            d = """and known3inp in words[3] """
            known3.delete("1.0", tk.END)

        if known4inp == "":
            e = ""
        else:
            e = """and known4inp in words[4] """
            known4.delete("1.0", tk.END)

        if wrongLocation0inp == "":
            f = ""
        else:
            f = """and wrongLocation0inp not in words[0] and wrongLocation0inp in words """
            wrongLocation0.delete("1.0", tk.END)

        if wrongLocation1inp == "":
            g = ""
        else:
            g = """and wrongLocation1inp not in words[1] and wrongLocation1inp in words """
            wrongLocation1.delete("1.0", tk.END)

        if wrongLocation2inp == "":
            h = ""
        else:
            h = """and wrongLocation2inp not in words[2] and wrongLocation2inp in words """
            wrongLocation2.delete("1.0", tk.END)

        if wrongLocation3inp == "":
            i = ""
        else:
            i = """and wrongLocation3inp not in words[3] and wrongLocation3inp in words """
            wrongLocation3.delete("1.0", tk.END)

        if wrongLocation4inp == "":
            j = ""
        else:
            j = """and wrongLocation4inp not in words[4] and wrongLocation4inp in words """
            wrongLocation4.delete("1.0", tk.END)

        if notNeedded0inp == "":
            k = ""
        else:
            k = """and notNeedded0inp not in words """
            notNeedded0.delete("1.0", tk.END)

        if notNeedded1inp == "":
            l = ""
        else:
            l = """and notNeedded1inp not in words """
            notNeedded1.delete("1.0", tk.END)

        if notNeedded2inp == "":
            m = ""
        else:
            m = """and notNeedded2inp not in words """
            notNeedded2.delete("1.0", tk.END)

        if notNeedded3inp == "":
            n = ""
        else:
            n = """and notNeedded3inp not in words """
            notNeedded3.delete("1.0", tk.END)

        if notNeedded4inp == "":
            o = ""
        else:
            o = """and notNeedded4inp not in words """
            notNeedded4.delete("1.0", tk.END)

        for words in wordset:
            x = f"""wordList.append(words) if{a}{b}{c}{d}{e}{f}{g}{h}{i}{j}{k}{l}{m}{n}{o}else print("")""".replace("if and", "if").replace("ifand", "if")
            exec(x)
        print(wordList)
    elif turn == 2:
        turn = turn + 1

        known0inp = known0.get(1.0, "end-1c")
        known1inp = known1.get(1.0, "end-1c")
        known2inp = known2.get(1.0, "end-1c")
        known3inp = known3.get(1.0, "end-1c")
        known4inp = known4.get(1.0, "end-1c")
        wrongLocation0inp = wrongLocation0.get(1.0, "end-1c")
        wrongLocation1inp = wrongLocation1.get(1.0, "end-1c")
        wrongLocation2inp = wrongLocation2.get(1.0, "end-1c")
        wrongLocation3inp = wrongLocation3.get(1.0, "end-1c")
        wrongLocation4inp = wrongLocation4.get(1.0, "end-1c")
        notNeedded0inp = notNeedded0.get(1.0, "end-1c")
        notNeedded1inp = notNeedded1.get(1.0, "end-1c")
        notNeedded2inp = notNeedded2.get(1.0, "end-1c")
        notNeedded3inp = notNeedded3.get(1.0, "end-1c")
        notNeedded4inp = notNeedded4.get(1.0, "end-1c")

        if known0inp == "":
            a = ""
        else:
            a = """ and known0inp in words[0] """
            known0.delete("1.0", tk.END)

        if known1inp == "":
            b = ""
        else:
            b = """and known1inp in words[1] """
            known1.delete("1.0", tk.END)

        if known2inp == "":
            c = ""
        else:
            c = """and known2inp in words[2] """
            known2.delete("1.0", tk.END)

        if known3inp == "":
            d = ""
        else:
            d = """and known3inp in words[3] """
            known3.delete("1.0", tk.END)

        if known4inp == "":
            e = ""
        else:
            e = """and known4inp in words[4] """
            known4.delete("1.0", tk.END)

        if wrongLocation0inp == "":
            f = ""
        else:
            f = """and wrongLocation0inp not in words[0] and wrongLocation0inp in words """
            wrongLocation0.delete("1.0", tk.END)

        if wrongLocation1inp == "":
            g = ""
        else:
            g = """and wrongLocation1inp not in words[1] and wrongLocation1inp in words """
            wrongLocation1.delete("1.0", tk.END)

        if wrongLocation2inp == "":
            h = ""
        else:
            h = """and wrongLocation2inp not in words[2] and wrongLocation2inp in words """
            wrongLocation2.delete("1.0", tk.END)

        if wrongLocation3inp == "":
            i = ""
        else:
            i = """and wrongLocation3inp not in words[3] and wrongLocation3inp in words """
            wrongLocation3.delete("1.0", tk.END)

        if wrongLocation4inp == "":
            j = ""
        else:
            j = """and wrongLocation4inp not in words[4] and wrongLocation4inp in words """
            wrongLocation4.delete("1.0", tk.END)

        if notNeedded0inp == "":
            k = ""
        else:
            k = """and notNeedded0inp not in words """
            notNeedded0.delete("1.0", tk.END)

        if notNeedded1inp == "":
            l = ""
        else:
            l = """and notNeedded1inp not in words """
            notNeedded1.delete("1.0", tk.END)

        if notNeedded2inp == "":
            m = ""
        else:
            m = """and notNeedded2inp not in words """
            notNeedded2.delete("1.0", tk.END)

        if notNeedded3inp == "":
            n = ""
        else:
            n = """and notNeedded3inp not in words """
            notNeedded3.delete("1.0", tk.END)

        if notNeedded4inp == "":
            o = ""
        else:
            o = """and notNeedded4inp not in words """
            notNeedded4.delete("1.0", tk.END)

        for words in wordList:
            v = f"""wordList2.append(words) if{a}{b}{c}{d}{e}{f}{g}{h}{i}{j}{k}{l}{m}{n}{o}else print("")""".replace("if and", "if").replace("ifand", "if")
            exec(v)
        print(wordList2)

    elif turn == 3:
        turn = turn + 1

        known0inp = known0.get(1.0, "end-1c")
        known1inp = known1.get(1.0, "end-1c")
        known2inp = known2.get(1.0, "end-1c")
        known3inp = known3.get(1.0, "end-1c")
        known4inp = known4.get(1.0, "end-1c")
        wrongLocation0inp = wrongLocation0.get(1.0, "end-1c")
        wrongLocation1inp = wrongLocation1.get(1.0, "end-1c")
        wrongLocation2inp = wrongLocation2.get(1.0, "end-1c")
        wrongLocation3inp = wrongLocation3.get(1.0, "end-1c")
        wrongLocation4inp = wrongLocation4.get(1.0, "end-1c")
        notNeedded0inp = notNeedded0.get(1.0, "end-1c")
        notNeedded1inp = notNeedded1.get(1.0, "end-1c")
        notNeedded2inp = notNeedded2.get(1.0, "end-1c")
        notNeedded3inp = notNeedded3.get(1.0, "end-1c")
        notNeedded4inp = notNeedded4.get(1.0, "end-1c")

        if known0inp == "":
            a = ""
        else:
            a = """ and known0inp in words[0] """
            known0.delete("1.0", tk.END)

        if known1inp == "":
            b = ""
        else:
            b = """and known1inp in words[1] """
            known1.delete("1.0", tk.END)

        if known2inp == "":
            c = ""
        else:
            c = """and known2inp in words[2] """
            known2.delete("1.0", tk.END)

        if known3inp == "":
            d = ""
        else:
            d = """and known3inp in words[3] """
            known3.delete("1.0", tk.END)

        if known4inp == "":
            e = ""
        else:
            e = """and known4inp in words[4] """
            known4.delete("1.0", tk.END)

        if wrongLocation0inp == "":
            f = ""
        else:
            f = """and wrongLocation0inp not in words[0] and wrongLocation0inp in words """
            wrongLocation0.delete("1.0", tk.END)

        if wrongLocation1inp == "":
            g = ""
        else:
            g = """and wrongLocation1inp not in words[1] and wrongLocation1inp in words """
            wrongLocation1.delete("1.0", tk.END)

        if wrongLocation2inp == "":
            h = ""
        else:
            h = """and wrongLocation2inp not in words[2] and wrongLocation2inp in words """
            wrongLocation2.delete("1.0", tk.END)

        if wrongLocation3inp == "":
            i = ""
        else:
            i = """and wrongLocation3inp not in words[3] and wrongLocation3inp in words """
            wrongLocation3.delete("1.0", tk.END)

        if wrongLocation4inp == "":
            j = ""
        else:
            j = """and wrongLocation4inp not in words[4] and wrongLocation4inp in words """
            wrongLocation4.delete("1.0", tk.END)

        if notNeedded0inp == "":
            k = ""
        else:
            k = """and notNeedded0inp not in words """
            notNeedded0.delete("1.0", tk.END)

        if notNeedded1inp == "":
            l = ""
        else:
            l = """and notNeedded1inp not in words """
            notNeedded1.delete("1.0", tk.END)

        if notNeedded2inp == "":
            m = ""
        else:
            m = """and notNeedded2inp not in words """
            notNeedded2.delete("1.0", tk.END)

        if notNeedded3inp == "":
            n = ""
        else:
            n = """and notNeedded3inp not in words """
            notNeedded3.delete("1.0", tk.END)

        if notNeedded4inp == "":
            o = ""
        else:
            o = """and notNeedded4inp not in words """
            notNeedded4.delete("1.0", tk.END)

        for words in wordList2:
            v = f"""wordList3.append(words) if{a}{b}{c}{d}{e}{f}{g}{h}{i}{j}{k}{l}{m}{n}{o}else print("")""".replace(
                "if and", "if").replace("ifand", "if")
            exec(v)
        print(wordList3)

    elif turn == 4:
        turn = turn + 1

        known0inp = known0.get(1.0, "end-1c")
        known1inp = known1.get(1.0, "end-1c")
        known2inp = known2.get(1.0, "end-1c")
        known3inp = known3.get(1.0, "end-1c")
        known4inp = known4.get(1.0, "end-1c")
        wrongLocation0inp = wrongLocation0.get(1.0, "end-1c")
        wrongLocation1inp = wrongLocation1.get(1.0, "end-1c")
        wrongLocation2inp = wrongLocation2.get(1.0, "end-1c")
        wrongLocation3inp = wrongLocation3.get(1.0, "end-1c")
        wrongLocation4inp = wrongLocation4.get(1.0, "end-1c")
        notNeedded0inp = notNeedded0.get(1.0, "end-1c")
        notNeedded1inp = notNeedded1.get(1.0, "end-1c")
        notNeedded2inp = notNeedded2.get(1.0, "end-1c")
        notNeedded3inp = notNeedded3.get(1.0, "end-1c")
        notNeedded4inp = notNeedded4.get(1.0, "end-1c")

        if known0inp == "":
            a = ""
        else:
            a = """ and known0inp in words[0] """
            known0.delete("1.0", tk.END)

        if known1inp == "":
            b = ""
        else:
            b = """and known1inp in words[1] """
            known1.delete("1.0", tk.END)

        if known2inp == "":
            c = ""
        else:
            c = """and known2inp in words[2] """
            known2.delete("1.0", tk.END)

        if known3inp == "":
            d = ""
        else:
            d = """and known3inp in words[3] """
            known3.delete("1.0", tk.END)

        if known4inp == "":
            e = ""
        else:
            e = """and known4inp in words[4] """
            known4.delete("1.0", tk.END)

        if wrongLocation0inp == "":
            f = ""
        else:
            f = """and wrongLocation0inp not in words[0] and wrongLocation0inp in words """
            wrongLocation0.delete("1.0", tk.END)

        if wrongLocation1inp == "":
            g = ""
        else:
            g = """and wrongLocation1inp not in words[1] and wrongLocation1inp in words """
            wrongLocation1.delete("1.0", tk.END)

        if wrongLocation2inp == "":
            h = ""
        else:
            h = """and wrongLocation2inp not in words[2] and wrongLocation2inp in words """
            wrongLocation2.delete("1.0", tk.END)

        if wrongLocation3inp == "":
            i = ""
        else:
            i = """and wrongLocation3inp not in words[3] and wrongLocation3inp in words """
            wrongLocation3.delete("1.0", tk.END)

        if wrongLocation4inp == "":
            j = ""
        else:
            j = """and wrongLocation4inp not in words[4] and wrongLocation4inp in words """
            wrongLocation4.delete("1.0", tk.END)

        if notNeedded0inp == "":
            k = ""
        else:
            k = """and notNeedded0inp not in words """
            notNeedded0.delete("1.0", tk.END)

        if notNeedded1inp == "":
            l = ""
        else:
            l = """and notNeedded1inp not in words """
            notNeedded1.delete("1.0", tk.END)

        if notNeedded2inp == "":
            m = ""
        else:
            m = """and notNeedded2inp not in words """
            notNeedded2.delete("1.0", tk.END)

        if notNeedded3inp == "":
            n = ""
        else:
            n = """and notNeedded3inp not in words """
            notNeedded3.delete("1.0", tk.END)

        if notNeedded4inp == "":
            o = ""
        else:
            o = """and notNeedded4inp not in words """
            notNeedded4.delete("1.0", tk.END)

        for words in wordList3:
            v = f"""wordList4.append(words) if{a}{b}{c}{d}{e}{f}{g}{h}{i}{j}{k}{l}{m}{n}{o}else print("")""".replace(
                "if and", "if").replace("ifand", "if")
            exec(v)
        print(wordList4)

known0 = tk.Text(frame, height=1, width=2)
known1 = tk.Text(frame, height=1, width=2)
known2 = tk.Text(frame, height=1, width=2)
known3 = tk.Text(frame, height=1, width=2)
known4 = tk.Text(frame, height=1, width=2)
known = tk.Label(frame, text="Known letters in correct locations (Green)")

wrongLocation0 = tk.Text(frame, height=1, width=2)
wrongLocation1 = tk.Text(frame, height=1, width=2)
wrongLocation2 = tk.Text(frame, height=1, width=2)
wrongLocation3 = tk.Text(frame, height=1, width=2)
wrongLocation4 = tk.Text(frame, height=1, width=2)
wrongLocation = tk.Label(frame, text="Known letters in the wrong location (Yellow)")

notNeedded0 = tk.Text(frame, height=1, width=2)
notNeedded1 = tk.Text(frame, height=1, width=2)
notNeedded2 = tk.Text(frame, height=1, width=2)
notNeedded3 = tk.Text(frame, height=1, width=2)
notNeedded4 = tk.Text(frame, height=1, width=2)
notNeedded = tk.Label(frame, text="Letters that are not needed (Grey)")

lbl = tk.Label(frame, height=20, width=20, text = "testing")

known.grid(row=0, column=0)
known0.grid(row=1, column=1)
known1.grid(row=1, column=2)
known2.grid(row=1, column=3)
known3.grid(row=1, column=4)
known4.grid(row=1, column=5)

wrongLocation.grid(row=2, column=0)
wrongLocation0.grid(row=3, column=1)
wrongLocation1.grid(row=3, column=2)
wrongLocation2.grid(row=3, column=3)
wrongLocation3.grid(row=3, column=4)
wrongLocation4.grid(row=3, column=5)

notNeedded.grid(row=6, column=0)
notNeedded0.grid(row=8, column=1)
notNeedded1.grid(row=8, column=2)
notNeedded2.grid(row=8, column=3)
notNeedded3.grid(row=8, column=4)
notNeedded4.grid(row=8, column=5)

printButton = tk.Button(frame, text="Get Words", command=printInput)
startAgain = tk.Button(frame, text="Start Again", command=clear)


printButton.grid(row=10, column=6)
startAgain.grid(row=11, column=6)

lbl.grid(row=12, column=0)
frame.mainloop()









# for words in english_words_set:
#     if len(words) == 5:
#         if "s" in words[0] and "i" in words[3] and "t" not in words and "a" not in words and "r" not in words:
#             print(words)
        # for letter in words:
        #     print(letter)
        # i = i + 1
        # print(words)
