def feed_animals(animals, food):
    if (len(animals) == 0) or (len(food) == 0):
        return 0
    animals = list(reversed(sorted(animals)))
    food = list(reversed(sorted(food)))
    cnt = 0
    for i in range(len(food)):
        for j in range(len(animals)):
            if food[i] >= animals[j]:
                cnt += 1
                break
    return cnt
# Максимальная эффективность тогда, когда пропадает наименьшее кол-во еды => 
# самой большой порцией нужно кормить самого требовательного животного, в этом помогает отсортированный по невозрастанию массив
