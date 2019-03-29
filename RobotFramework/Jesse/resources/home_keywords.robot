*** Settings ***
Documentation                       Home resources
Library                             SeleniumLibrary

*** Variables ***
${HOME_PUNCH_LINE}                  We believe there are lots of brilliant product and service ideas out there.\nDo you have one of those great ideas, which deserve to become real?

*** Keywords ***
Home Content Should Be Present
    Page Should Contain Image       id:sadeInnovationsLogo
    Page Should Contain Element     class:punch-line
    Element Text Should Be          class:punch-line    ${HOME_PUNCH_LINE}
    Page Should Contain Element     tag:ion-button
    Page Should Contain             EXPLORE OUR VISION
    Page Should Contain             scroll down
    Page Should Contain Element     class:scroll-down-icon
    Page Should Contain Element     class:footer-big-image


Vision Content Should Be Present
    Page Should Contain Element     class:vision-image