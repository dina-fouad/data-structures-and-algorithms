from data_structure_and_algorithms.python.code_challenges.stack-queue-brackets.stack_queue_brackets import check

def test_true():
    exbected = True
    actual = check('{}')
    assert actual == exbected

def test_true_0():
    exbected = True
    actual = check('{}(){}')
    assert actual == exbected


def test_true_1():
    actual = check('()[[Extra Characters]]')
    exbected = True
    assert actual == exbected
