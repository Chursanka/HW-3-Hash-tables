def feed_animals(animals, food):
    if (len(animals) == 0) or (len(food) == 0):
        return 0
    animals = list(reversed(sorted(animals)))
    food = list(reversed(sorted(food)))
    cnt = 0
    j = 0
    for i in range(len(animals)):
        while j < len(food):
            if food[j] >= animals[i]:
                cnt += 1
                j += 1
                break
            j += 1
        if j == len(food):
            break
    return cnt
# Максимальная эффективность тогда, когда пропадает наименьшее кол-во еды => 
# самой большой порцией нужно кормить самого требовательного животного, в этом помогает отсортированный по невозрастанию массив
# UPDATED: теперь для каждого животоного нахожу его личную порцию, а не иду по массивам параллельно
