def make_student(id,name):

    return [id,name,0,0.0]

def add_student(population,id,name):

    for index in range(len(population)):
        student = population[index]
        if student [0] == id:
            population.pop(index)
            break
    
    new_studnet = make_student(id,name)
    population += (new_studnet)


        
def get_student(population, id):

    for student in population:
        if student[0] == id:
            return student
    return None

def add_credit(population,id,credits):
    student = get_student(population,id)
    if student is not None:
        student[2] += credits


def get_credits(population, id):
    student = get_student(population,id)
    if student is not None:
        return

def count_words(filename):
    with open(filename) as file:
        words = {}
        for line in file:
            line = line.lower()
            line_words = line.split

            for word in line_words:
                if word in words:

                    words[word] += 1
                
                else:
                    words[word] = 1
                

        
def main():
    student1 = make_student("cb1234", "charlie Brown")
    print(student1)

    population = []
    add_student(population, 'cb1234', "charlie brown")
    charlie = get_student(population,"cb1234")
    print("charlie", charlie)

    count_words()


main()