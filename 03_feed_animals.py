def feed_animals(animals, food):
    if (len(animals) == 0) or (len(food) == 0):
        return 0
    animals = list(reversed(sorted(animals)))
    food = list(reversed(sorted(food)))
    cnt = 0
    for i in range(len(food)):
        if food[i] >= animals[cnt]:
            cnt += 1
    return cnt
# Максимальная эффективность тогда, когда пропадает наименьшее кол-во еды => 
# самой большой порцией нужно кормить самого требовательного животного, в этом помогает отсортированный по невозрастанию массив
