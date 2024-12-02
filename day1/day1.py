
def loadFile():
    print("santas helper")
    left_list = []
    right_list = []
    with open('day1/input.txt', 'r') as file:
        lines = [line.rstrip() for line in file]
        for l in lines:
            left, right = l.split("   ", 2)
            left_list.append(int(left))
            right_list.append(int(right))

        left_list.sort()
        right_list.sort()

        return left_list, right_list

def calculateDif(left_list, right_list):
    total_dif = 0
    for i in range(len(left_list)):
        dif = left_list[i] - right_list[i]
        if dif < 0:
            dif *= -1
        total_dif += dif
    return total_dif

def calculateSimilarity(left_list, right_list):
    total_similarity = 0
    for i in range(len(left_list)):
        similarity = left_list[i] * right_list.count(left_list[i])
        total_similarity += similarity
    return total_similarity

if __name__ == "__main__":
    print("hey yo santa")
    left_list, right_list = loadFile()

    total_dif = calculateDif(left_list, right_list)
    print("Total dif: " + str(total_dif))

    similarity_score = calculateSimilarity(left_list, right_list)
    print("Similarity: " + str(similarity_score))

