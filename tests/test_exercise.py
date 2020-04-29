import pytest
import src.exercise

def test_exercise():
    input_values = ["Nothing","2010","Random","2013","Random","2013",""]
    input_values_stored = ["1","2"]
    output = []

    def mock_input(s=None):
        if s is not None:
            output.append(s)
            return input_values.pop(0)
        else:
            output.append("")
            return input_values.pop(0)

    src.exercise.input = mock_input
    src.exercise.print = lambda s : output.append(s)

    src.exercise.main()

    assert output == ["Name (empty will stop):","Publication year:",\
                        "Name (empty will stop):","Publication year:",\
                            "Name (empty will stop):","Publication year:","The book is already on the list. Let's not add the same book again."\
                                "Name (empty will stop):","Thank you! Books added: 2"]
