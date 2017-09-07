# Self Check
import random


# 1st generate sentence using words in s
def generate_sentence(s):
    wordlist = s.split()
    random.shuffle(wordlist)
    print(wordlist)
    count = 0
    while True:
        if ' '.join(wordlist) == s:
            print(count)
            return
        random.shuffle(wordlist)
        count += 1
        print(count)


# 2nd generate a word(27 characters long)
def generate_word():
    ori_chr = [chr(i) for i in range(97, 123)]
    ori_chr.append(' ')
    random.shuffle(ori_chr)
    return ''.join(ori_chr)


# challenge
def generate_word_2(correct_list, s):
    correct_set = set(correct_list)
    all_set = set(range(len(s)))
    remain_set = all_set - correct_set
    rand_choice1 = random.choice(list(remain_set))
    remain_set.remove(rand_choice1)
    rand_choice2 = random.choice(list(remain_set))
    temp = s[rand_choice1]
    s = list(s)
    s[rand_choice1] = s[rand_choice2]
    s[rand_choice2] = temp
    return ''.join(s)


# 3rd compare and score
def compare_score(generate, goal):
    score = 0
    correct_list = []
    if generate == goal:
        score = 1
    else:
        for i in range(27):
            if generate[i] == goal[i]:
                score += (1/27.0)
                correct_list.append(i)
    return score, correct_list


# 4th compare and score 1000
def game(goal, max_iter):
    best_guess = ''
    best_score = 0.0
    guess_word = generate_word()
    for i in range(max_iter):
        score, correct_list = compare_score(guess_word, goal)
        if score == 1:
            print('Congraduations!')
            print('guess %d times!' % i)
            return
        else:
            if score > best_score:
                best_score = score
                best_guess = guess_word
        guess_word = generate_word_2(correct_list, guess_word)
        print('%d: score: %f, word: %s' % (i, score, guess_word))
    print('Have alredy guessed 1000 times!')
    print('The best score: %f' % best_score)
    print('The best guess word is %s' % best_guess)

# set up goal
goal_src = [chr(i) for i in range(97, 123)]
goal_src.append(' ')
goal_src = ''.join(goal_src)

game(goal_src, 1000)
