*** Settings ***
Documentation                               Home resources
Library                                     SeleniumLibrary

# Nämä keywordit on tarkoitettu ohjeelliseksi/malliksi eivätkä ne toimi lokaalissa ajoympäristössä,
# jossa oletettua verkkosivua ei luonnollisesti ole saatavilla.

*** Variables ***
${HOME_PUNCH_LINE}                          We believe there are lots of brilliant product and service ideas out there.\nDo you have one of those great ideas, which deserve to become real?
${VISION_PUNCH_LINE}                        Focus on your dream

*** Keywords ***
Home Content Should Be Present
    Wait Until Page Contains Element        id:sadeInnovationsLogo
    Page Should Contain Element             class:punch-line
    Wait Until Element Contains             class:punch-line    ${HOME_PUNCH_LINE}
    Page Should Contain Element             tag:ion-button
    Page Should Contain                     EXPLORE OUR VISION
    Page Should Contain                     scroll down
    Page Should Contain Element             class:scroll-down-icon
    Page Should Contain Element             class:footer-big-image

Vision Content Should Be Present
    Page Should Contain Element             class:vision-image

Vision Punch Line Should Be Present
    Wait Until Page Contains Element        xpath://span[contains(text(), "VISION")]
    Click Element                           xpath://span[contains(text(), "VISION")]
    Wait Until Page Contains Element        class:vision-full-text
    Wait Until Page Contains Element        class:vision-text
    Wait Until Page Contains Element        class:vision-header
    Wait Until Element Contains             class:vision-header     ${VISION_PUNCH_LINE}