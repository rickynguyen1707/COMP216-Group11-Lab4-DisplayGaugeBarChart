import random

NUM_FILES = 10


def seed():
    def genfile(idx):
        filename = f'integers-{idx}.txt'
        with open(filename, "w") as file:
            intcount = random.randint(5, 10)
            for _ in range(0, intcount):
                randint = random.randint(100, 1000)
                file.writelines([randint.__str__(), '\n'])

    for idx in range(1, NUM_FILES + 1):
        genfile(idx)


if __name__ == "__main__":
    seed()
