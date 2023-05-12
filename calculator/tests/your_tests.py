#!/usr/bin/env python3
from calculator_adapter import run


### ADD AT LEAST TWO TESTS HERE!
# Check that program outputs "12" for an input of "4 + 8"
assert run("4 + 8").output == "12"
# Check that program outputs "45" for an input of "9 * 5"
assert run("9 * 5").output == "45"
# Check that program outputs "-7" for an input of "3 - 10"
assert run("3 - 10").output == "-7"
# Check that program outputs "0" for an input of "0 / 70"
assert run("0 / 70").output == "0"
# Check that program exits successfully (no errors) with an input of "99 + 1"
assert run("99 + 1").exit_status == 0
# Check that programs fails (correctly errors) with an input of "87 & 2"
assert run("87 & 2").exit_status != 0



print("All tests passed!")
