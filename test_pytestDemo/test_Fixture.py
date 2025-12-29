# Fixture helps to run the prerequisites first and then run the dependent test case
# #we need to pass the prerequisite test case as parameter to dependent case

#tear down
#this is like post run first all the test cases will run and at last these will run we will use yield key so that this test case runs at last.
#normal generator function once you use yield it pauses and then use next to resume but in this case once yield is reached pytest will work as next so it holds the pause state and resumes at last


import pytest


def  test_fixture_mode(test_base_fixture):
    print("I am dependent on fixture method")




