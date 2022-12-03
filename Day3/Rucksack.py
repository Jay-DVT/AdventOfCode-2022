import string 
with open('testB.txt') as l:
    ls = l.readlines()

score = 0
num = 1
group = []
for line in ls:
    group.append(line.replace('\n', ''))
    if num < 3:
        num += 1

    else:    
        print(group)
        for letter in group[0]:
            if letter in group[1]:
                if letter in group[2]:
                    lower = list(string.ascii_lowercase)
                    if letter in lower:
                        score += lower.index(letter)+1
                        break
                    cap = list(string.ascii_uppercase)
                    if letter in cap:
                        score += cap.index(letter)+27
                        break
        # for letter in line[0:n//2]:
        #     if letter in line[n//2:]:
        #         lower = list(string.ascii_lowercase)
        #         if letter in lower:
        #             score += lower.index(letter)+1
        #             break
        #         cap = list(string.ascii_uppercase)
        #         if letter in cap:
        #             score += cap.index(letter)+27
        #             break
        num = 1
        group = []


print(score)