![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)
![Coverage Status](https://s3.amazonaws.com/assets.coveralls.io/badges/coveralls_70.svg)

Read me.

Automation framework for JM website, scenarios covering ‘containers validation’ and ‘navigation’.

Environment:
Python 3 Go to https://www.python.org/downloads/    Download the latest version and install.


Pycharm - Go to https://www.jetbrains.com/pycharm/download/ download the latest version and install


Open pycharm , create new empty project use virtual environment (python will ask you automatically during the project creation - press yes). Close pycharm

Clone/download our python automation.
Go to settings, preferences, project, project interpreter - and choose our downloaded version of python to be the project interpreter. 
On the same page go to the ‘+’ sign at the bottom and press it to install our needed packages for current project:
- pytest 
- selenium 

After all done click on JM_Test_scenarios.py on the top will be located all the import packages for the project , stand on the mouse on the red underlines ones and click on install, do it for all red underlines.

Last step - right click on the middle of JM_Test_scenarios.py page then click ‘run file’

Tests will start running, during and after the run scenarios will appear on left and log results on right


To add new scenario we must include ‘test_’ inside the name of the scenario to make pytest recognize it as a test scenario
Also must include ‘Assert statements’ - for data input comparison - 
https://docs.pytest.org/en/reorganize-docs/new-docs/user/assert_statements.html


For any questions / issues please contact - Alex Dzhoharidze, technical consultant (QAC)
