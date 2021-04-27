# calculateInitialRisk

## Micro Service Description
Microservice that calculates the initial risk based on the information provided on the new reunion

## Functional Requirements
- The day 0 of possible infection will be the day the reunion is created
- An initial risk % (initialRiskFactor) is calculated as soon as the reunion is created based on the following metrics and weighting their inputs:
  * Algorithm should take into account number of people in the reunion
  * Algorithm should take into account how many time was the reunion
  * Algorithm should take into account if people were waring mask
  * Algorithm should take into account whether or not was an open space
  * Algorithm should take into account the two week span of transmission
- The initial risk will be classified on quarters in a semaphore scale:
  * 1 - Green: 0-25%
  * 2 - Yellow: 25-50%
  * 3 - Orange: 50-75%
  * 4 - Red: 75-100%

## Non Functional Requirements
- The risk of reunion is presented easily and visually on the UI
- All information about the reunion should be provided


## Deployment URL
https://us-south.functions.appdomain.cloud/api/v1/web/is708177%40iteso.mx_dev/ProyectoFinal/calculateInitialRisk
