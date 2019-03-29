*** Settings ***
Documentation                       Global resources
Library                             SeleniumLibrary

*** Variables ***
${SERVER}                           sade-9af5f.firebaseapp.com
${BROWSER}                          Chrome
${MAIN URL}                         https://${SERVER}/
${DELAY}                            0

*** Keywords ***
Open Browser To Main Page
    Open Browser                    ${MAIN URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed              ${DELAY}
