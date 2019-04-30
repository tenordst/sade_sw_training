*** Settings ***
Documentation                       Global resources
Library                             SeleniumLibrary

*** Variables ***

# Luonnollisesti testejä ajetaan normaalitilanteissa vain lokaalissa ajoympäristössä,
# tällöin web-sivun oikea palvelin ei kuormitu turhaan testisessiosta.
# IP-osoite 127.0.0.1 tarkoittaa localhostia (eli testin ajajan omaa konetta).
# 3000 on portti, joka on oletuksena esimerkiksi React web appiksen kehitysympäristössä.

${SERVER}                           127.0.0.1:3000
${BROWSER}                          Chrome
${MAIN URL}                         https://${SERVER}/
${DELAY}                            0

*** Keywords ***
Open Browser To Main Page
    Open Browser                    ${MAIN URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed              ${DELAY}
