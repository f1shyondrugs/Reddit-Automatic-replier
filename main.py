import praw
import customtkinter as tk
import os
from openai import OpenAI
from reply import reply

openai_api_key = "YOUR OPENAI API KEY"
reddit = praw.Reddit(username="YOUR USERNAME",
                     password="YOUR ACCOUNT PASSWORD",
                     client_id="CLIENT_ID",
                     client_secret="CLIENT_SECRET",
                     user_agent="praw_scraper_1.0"
)

def get_reddit_posts():
    

    subreddit_name = subreddit_entry.get()
    limit = int(limit_entry.get())
    category = category_var.get()

    subreddit = reddit.subreddit(subreddit_name)

    if category == 'Hot':
        posts = subreddit.hot(limit=limit)
    elif category == 'New':
        posts = subreddit.new(limit=limit)
    elif category == 'Top (All Time)':
        posts = subreddit.top(limit=limit)
    else:
        print("Ungültige Kategorie")
        return
    
    output_text.delete('1.0', tk.END)

    for file in os.listdir("output/"):
        os.remove(os.path.join("output/", file))
    for file in os.listdir("chatgpt/"):
        os.remove(os.path.join("chatgpt/", file))
    


    output_text.insert(tk.END, f"Every Description is in the .txt files in /output/*.txt\n")
    output_text.insert(tk.END, f"The {limit} {category} Posts of r/{subreddit_name} are:\n\n")

    i = 0
    for post in posts:
        i = i + 1
        output_text.insert(tk.END, f"Title: {post.title}\n")
        output_text.insert(tk.END, f"Upvotes: {post.score}\n")
        output_text.insert(tk.END, f"Link: {post.url}\n\n")
        
        with open("output/" + str(i) + ".txt", "w") as w:    
            w.write(f"{post.url}\nTitle: {post.title}\nUpvotes: {post.score}\n\nDescription:\n{post.selftext}")


        with open("chatgpt/" + str(i) + ".txt", "w") as a:
            
            client = OpenAI(api_key=openai_api_key)
            system = [{"role": "system", "content": "Write a cool and experienced sounding comment for a forum on Reddit about the Post i'll give you. The comment should be informative and engaging, proportional to the length of the initial prompt. Never write your response in quotation marks or use any Hashtags in your response."}]
            chat_history = []

            question = f"The Title of the post is: '{post.title}', The Description of the Post is '{post.selftext}'. Generate a good, but short comment to that in the style of a social media comment, maybe add additional information, maximum 200 characters. "

            user = [{"role": "user", "content": question}]
            

            chat_completion = client.chat.completions.create(
                messages = system + chat_history + user,
                model = "gpt-3.5-turbo",
                temperature = 1,

            )
            a.write(f"{post.url}\n" + chat_completion.choices[0].message.content)
        
    

        
        


root = tk.CTk()
root.title("Reddit Posts")



subreddit_CTkLabel = tk.CTkLabel(root, text="Subreddit:")
subreddit_CTkLabel.pack()


subreddit_entry = tk.CTkEntry(root)
subreddit_entry.pack()

limit_CTkLabel = tk.CTkLabel(root, text="Count of Posts:")
limit_CTkLabel.pack()

limit_entry = tk.CTkEntry(root)
limit_entry.pack()


limit_CTkLabel = tk.CTkLabel(root, text="Category:")
limit_CTkLabel.pack()

category_var = tk.StringVar()
category_var.set("Hot")

category_frame = tk.CTkFrame(root)
category_frame.pack()

category_options = ['Hot', 'New', 'Top (All Time)']
for option in category_options:
    category_radio = tk.CTkRadioButton(category_frame, text=option, variable=category_var, value=option)
    category_radio.pack(side=tk.LEFT)


output_text = tk.CTkTextbox(root, height=500, width=400)
output_text.pack()


get_posts_button = tk.CTkButton(root, text="Get Posts", command=get_reddit_posts)
get_posts_button.pack()

replybtn = tk.CTkButton(root, text="Post comments w/ chatgpt (wait till finished)", command=reply)
replybtn.pack()

root.mainloop()
