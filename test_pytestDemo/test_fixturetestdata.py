import pytest


# @pytest.mark.usefixtures("test_pass_content")
# class Testdata:
#     def test_profile(self, test_pass_content):
#         print(test_pass_content)


def test_access_browser(crossBrowser):
    print(crossBrowser)
