# Reddit Automatic Subreddit Replier

Writes Automatic Reddit Replies with ChatGPT. Specify Your Details in the `main.py` and `reply.py`. You'll need an OpenAI Key and Also Reddit Developer Application as a "self-use Script".

## Requirements
Libraries You'll need to install:
 - praw
 - openai
 - discord-webhook
 - customtkinter

## How Does it Work
When Opened `main.py`, you should see this:



![image](https://github.com/f1shyondrugs/Reddit-Automatic-replier/assets/86548888/5f319404-6dc9-4bd6-a686-6b4a09192c53)


It's pretty self-explanating, after entering all the information, click `Get Posts`, after all of your posts got displayed, you can post these comments under every post with the other button.

## Errors that i've encountered
### ImportError: cannot import name 'override' from 'typing_extensions'
Fix This by uninstalling and reinstalling OpenAI
`pip uninstall openai`
`pip install openai`

### I will update this list on further development
