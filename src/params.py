# All standard variable types are supported.
BOOL = True
INT = 2
FLOAT = 0.001
STR = "abc"
DICT = {"a": 1, "b": 2}
LIST = [1, 2, 3, 4, 5]
SET = {4, 5, 6, 7, 8}
TUPLE = (10, 102)
NONE = 1
UNARY_OP = -3

# Complex expressions will be ignored.
DICT_EXP = dict(a=1, b=2)
WEIGHTS = {"tfidf_jigsaw_regression": 3, "tfidf_ruddit": 2}

# DVC can retrieve class constants and variables defined in __init__


class TrainConfig:

    EPOCHS = 723

    def __init__(self):
        self.layers = 5
        self.layers = 11  # TrainConfig.layers param will be 9
        self.sum = 1 + 2  # Will NOT be found due to the expression
        bar = 3  # Will NOT be found since it's locally scoped


class TestConfig:

    TEST_DIR = "path"
    METRICS = ["metric"]
