# CandyAI

It is a marketing solution for a grocery shop chain Alepa that can be useful for any other offline marketing needs.

***Hardware:***

Dobot Robotic Arm

Digital Camera

Computing block (to connect all things and run software)

***Software:***

Flask web server (API to control Robot from any device)

Python script (Open CV, Tensor Flow, requests to Google Text-to-Speech API and Clarifai) 

## **User story**

1) Someone is walking along our robot in shopping center

2) Our robot using camera detects a person and pronounce personalized greeting

3) Someone pays attention to this and go to the robot to view a promotion material

4) Robot offers to play a game to win a discount for candies or to make a photo that would be customized using "Candy filter" to share it on social media. Here we can receive personal data like email (to send a picture) or notify about promotion campaign

## **How does it work?**

**Greeting Robot**

OpenCV + Using Tensor Flow - detect person and capture image (for some future features we also cut body)

Clarify - get personal information like age, gender, unique entities (e.x. backpack, cellphone and so on)

Google Text-to-Speech - pronounce personalize greeting and tinkering (for different ages and genders we use different accents)

Live demo: https://youtu.be/IFU1Du42fDE

**Game for Android**

Simple candy crash game sends requests to the robot to get candies if you get checkpoint score
(https://github.com/theshadowagent/candyAI/tree/master/android)

Live demo: https://youtu.be/xvgWo0OYYHk

**"Candies filter"**

OpenCV gets picture of user and using marked by colors library of candies pictures creates a "candy picture" 

Live demo: https://youtu.be/3LFDOJPKbvU

## **Our presentation**

https://docs.google.com/presentation/d/1b6JV4bwsVlgIpUdn2Ahok3byx_bOyPbD2FH0jx-ld3E/

## **How to run it**

python backend/server.py //runs Rest API and web application to control robot (https://documenter.getpostman.com/view/1332969/RzfZQZ5r)

- localhost:5000/base //interface to run application to create a picture

- localhost:5000/controlpanel //interface to manually control robot

python image_recognition/video_caption_with_tf.py //runs script to detect customer and make personal greeting. You need to put pre-trained models in image_recognition/models/ folder (you can find full repository with models here: https://drive.google.com/open?id=1UoGnoikGLMVD-UgQ1bmuRXtixW5C0Ksm) and set up the environment variable GOOGLE APPLICATION CREDENTIALS
