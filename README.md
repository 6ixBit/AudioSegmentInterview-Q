# Full stack application that returns stats based on timestamps sourced from a csv file on the server

## Frontend
- [GET] localhost:8080

## Backend Endpoints [Python Server]
- [GET] /stat/timestalked - Returns numbers of number of times a participant appeared in the audio segment
  
- [GET] /stat/callcontribution - Returns duration in seconds of audio segment from every participant

- [GET] /stat/all - Returns all calculated stats per participant

### Run
1. docker-compose build
2. docker-compose up
3. visit localhost:8080
