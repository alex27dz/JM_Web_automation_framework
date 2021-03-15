![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)
![Coverage Status](https://s3.amazonaws.com/assets.coveralls.io/badges/coveralls_100.svg)

# Automation framework for JM website, 
Scenarios made for ‘containers validation’ and ‘navigation’. 

#### Supporting Chrome and IE web drivers.
#### Supporting STAGE environment.

## Environment setup:

Python 3 - Go to https://www.python.org/downloads/    Download the latest version and install.

Pycharm - Go to https://www.jetbrains.com/pycharm/download/ Download the latest version and install.


Set up framework:

0 - Crate a new project using Virtual environment - you will be asked at first what python version to use and what environment - choose virtual.

1 - Download chromeDriver, make sure it matches our chrome browser version: https://chromedriver.chromium.org/downloads

2 - Go to settings, preferences, project, project interpreter - and choose our downloaded version of python to be the project interpreter. 
On the same page go to the ‘+’ sign at the bottom and press it to install our needed packages for current project:
- pytest 
- selenium 

3 - Click on JM_Test_scenarios.py on the top will be located all the import packages for the project , stand on the mouse on the red underlines ones and click on install, do it for all red underlines.

4 - right click on the middle of JM_Test_scenarios.py page then click ‘run file’, or on top right of pycharm window press play on the name of the file

5 - Tests will start running, during and after the run scenarios will appear on left and log results on right

New scenario
To add new scenario we must include ‘test_’ inside the name of the scenario to make pytest recognize it as a test scenario
Also must include ‘Assert statements’ - for data input comparison - 
https://docs.pytest.org/en/reorganize-docs/new-docs/user/assert_statements.html

Pytests structure  example 
<img src="https://usaupload.com/cache/plugins/filepreviewer/6554/7a01e47ea9b6ad052e4db31176fc9cd5386325b5bd621414fdd10fe9b87a93cb/1100x800_cropped.jpg">
tact - Alex Dzhoharidze, technical consultant (QAC)
