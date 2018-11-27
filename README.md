# CandyAI

It is a marketing solution for a grocery shop chain Alepa that can be useful for any other offline marketing needs.

Hardware:
Dobot Robotic Arm
Digital Camera
Computing block (to connect all things and run software)

Software:
Flask web server (API to control Robot from any device)
Python script (Open CV, Tensor Flow, requests to Google Text-to-Speech API and Clarifai ) 

#User story

1) Someone is walking along our robot

2) Our robot using camera detects a person and pronounce personalized greeting

3) Someone pays attention to this and go to the robot to view a promotion material

4) Robot offers to play a game to win a discount for candies or to make a photo that would be customized using "Candy filter" to share it on social media. Here we can receive personal data like email (to send a picture) or notify about promotion campaign

#How does it work?

OpenCV + Using Tensor Flow - detect person, cut body
Clarify - get personal information like age, gender, unique entities (e.x. backpack, cellphone and so on )
Google Text-to-Speech - pronounce personalize greeting and tinkering

Game for Android
Simple candy crash game sends requests to the robot to get candies if you receive 


Our presentation: https://docs.google.com/presentation/d/1b6JV4bwsVlgIpUdn2Ahok3byx_bOyPbD2FH0jx-ld3E/
