#!/bin/bash

name="Charwekey"
echo "Good afternoon $name, how are you doing today?"

date

mkdir session_logs


touch session_logs/$(date +%F).log

echo "I'm Charwekey Rabi Sabutey
I am a software developer with a passion for creating innovative solutions. 
I have experience in various programming languages and frameworks, and 
I enjoy working on projects that challenge me to learn and grow. 
In my free time, I like to explore new technologies and contribute to open-source projects." >session_logs/$(date +%F).log

echo " Setup complete!"