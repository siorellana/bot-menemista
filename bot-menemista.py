import tweepy
import os
import datetime
import random

# Access the value of the CONSUMER_KEY environment variable
consumer_key = os.environ["CONSUMER_KEY"]

# Access the value of the CONSUMER_SECRET environment variable
consumer_secret = os.environ["CONSUMER_SECRET"]

# Access the value of the ACCESS_TOKEN environment variable
access_token = os.environ["ACCESS_TOKEN"]

# Access the value of the ACCESS_TOKEN_SECRET environment variable
access_token_secret = os.environ["ACCESS_TOKEN_SECRET"]


# Authenticate with Twitter API using dummy credentials
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Get the current time
now = datetime.datetime.now()
hour_string = now.strftime("%H:%M:%S")

# Post a tweet
#api.update_status("#MenemismoParaChile")
#api.update_status("#MaximoMenem2042")
#api.update_status("#ChileNecesitaMenemismo")

future = datetime.datetime(2042, 1, 1, 1, 12, 13)

# Calculate the difference between the current and future date and time
delta = future - now

# Calculate the number of days, hours, and minutes in the difference
days = delta.days
hours = delta.seconds // 3600
minutes = (delta.seconds % 3600) // 60

# Print the result
print(f"There are {days} days, {hours} hours, {minutes} minutes until 2042.")

# Open the quotes file
with open("menemismo.txt") as file:
    # Read the lines of the file into a list
    quotes = file.readlines()

# Select a random quote from the list
quote = random.choice(quotes)

# print the quote
print(quote)

message_pair = f"Quedan {days} días, {hours} horas y {minutes} minutos para el progreso. {quote} "
message = f"Esto es lo que falta para el cambio real en Chile: {days} días, {hours} horas y {minutes} minutos. {quote}"

# Check if the minute of the current time is even
if now.second % 2 == 0:
    api.update_status(message_pair)
else:
    api.update_status(message)