from random import choice


def task9(alphabet):
    statistics = {}

    def get_statistics(sequence):
        for i in alphabet:
            statistics[i] = sequence.count(i)
        return statistics

    return get_statistics


if __name__ == "__main__":
    # сгенерируем случайную последовательность из символов алфавита ['A', 'C', 'G', 'T']
    n = 35
    generated_sequence = "".join(choice(['A', 'C', 'G', 'T']) for i in range(n))
    print(generated_sequence)  # CATGTTGGGACAGTCTTATTCTGTTGGCCAGATAC
    print(task9(['A', 'C', 'G', 'T'])(generated_sequence))  # {'A': 7, 'C': 7, 'G': 9, 'T': 12}
