#pytest rules
#File name should be started with test_
#Function name should start with test_
#code should be wrapped in method only
#-k stands for method name execution  -s logs in to output -v stands for more info metadata
#run specific file with py.test
#you can mark (tag) tests @pytest.mark.smoke and then run with -m smoke(marker name)
#you can skip particular test case @pytest.mark.skip
#@pytest.mark.xfail tets case need to run but error will not be reported



import pytest


@pytest.mark.smoke
def test_firstcharmprogram():
    print("Hello")

@pytest.mark.skip
def test_secondcharmprogram():
    print("test output")