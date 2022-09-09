import pandas

class EmptyFileException(Exception):
    pass

def words_to_learn():
    try:
        data = pandas.read_csv("./data/words_to_learn.csv")
        to_learn = data.to_dict(orient="records")
        if not to_learn:
            raise EmptyFileException()
    except FileNotFoundError:
        data = pandas.read_csv("./data/french_words.csv")
        to_learn = data.to_dict(orient="records")

    except EmptyFileException:
        data = pandas.read_csv("./data/french_words.csv")
        to_learn = data.to_dict(orient="records")

    return to_learn


def save_progress(to_learn):

    data = pandas.DataFrame(to_learn)
    data.to_csv("./data/words_to_learn.csv", index=False)

