
# 🔎 🔢 Guess That Number 🔎 🔢 


## Authors 📝

- [Chanelle Washington](https://github.com/see-chan-code)
- [Kenneth W](https://github.com/Kennov8)
- [Angel Fernandez](https://github.com/Avixph)
- [Nicholas Samuels](https://github.com/nssamuels1)


## Overview 📖
Through the use of Google Cloud App Engine as the serverless solution of choice, the team deployed a simple game (Guess that Number) in which the player attempts to guess the correct number. 

Cloud Function was used to create the Player, Questioner and Manager. Cloud Firestore was used as the database solution to store the events. Pub/Sub was used to trigger the event and return the answers. Finally, Access and Security measures were incorporated through the use of IAM (Identity and Access Management) to restrict access and IAP (Identity-Aware Proxy) to store players identifiable information.

### Goals
- Create Players
- Create Questioners
- Create Managers
- Maintain a database of events utilizing Firestore
- Create Functions on Cloud Functions
- Create triggers on Pub/Sub
- Deploy on App Engine
- Restrict access using IAM
- Store identifiable information via IAP
- Setup Readme.txt/Complete Tech Doc

### Non Goals
- Additional players
- Crash encountered during setup of Smarter Player
- Crash encountered during deployment on App Engine
- Crashed during testing but was corrected with changes to Pub/Sub

### Design
![Drag Racing](https://lh4.googleusercontent.com/ADOllo24relgXy_yUaeX6kaUJPRtgxs6zpGfYj2659HjZXv-55vX3wq8SWfoSnKzs9riEeCrikOdffb3SflUhgOywC71beLiSc9ejtg7lxb6QlDTklEYt3rDAlhNDLulF1EXU-8fuw)


## Alternatives Considered ⤴️
Initially, the group was going to use Concentration (The Memory Game) but quickly realized this would be an undertaking that would require more time and coding experience than the collective had. Next, taking into account we needed to scale down our project, the group entertained the idea of using tic-tac-toe as the game of choice. However, after further thought the collective took into account the time constraints and the possible variables after each player’s move, it was decided this would not be a good idea either.

## Security Considerations 🔐
To protect the integrity of the game, a secret variable has been added. This ensures that the only results accepted by the functions are those triggered by Pub/Sub messages. Additionally,  an Identity-Aware Proxy has been set up to require each player’s email address to be authenticated by one of the administrators and they must have the player URL to access the game. The IAP also allows for a nickname to be created and stored for each player thereby recording all of that individual’s game play and increases game play accessibility. History will be used to eliminate numbers already selected and prevent the player from identifying patterns which would allow them to predict the correct answer. 
## Privacy Considerations 🛑
Each player must provide their email address which must be approved by an administrator (Google Accounts are accessible without approval due to settings of Identity-Aware Proxy; this can be edited at any time). Administrators are the only ones with access to individual player’s information.

## References

 - [The Serverless Architecture by Example](https://serverlessworkshop.dev/)
 - [Google App Engine Documentation](https://cloud.google.com/appengine/docs/standard/python3/building-app)
 - [Developer Cheat Sheet](https://googlecloudcheatsheet.withgoogle.com/architecture)

