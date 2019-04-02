*** Settings ***
Documentation       Test suite to test Home Page
Resource            ./resources/global_keywords.robot
Resource            ./resources/home_keywords.robot

*** Test Cases ***
Valid Home Page
    Open Browser To Main Page
    Home Content Should Be Present
    Vision Content Should Be Present
    [Teardown]  Close Browser

Valid Vision Punch Line
    Open Browser To Main Page
    Vision Punch Line Should Be Present
    [Teardown]  Close Browser