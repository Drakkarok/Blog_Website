from flask import Flask, render_template
import requests
from post import Post

response = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
response.raise_for_status()
posts_data = response.json()

post_objects = []
for post in posts_data:
    post_entity = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_entity)

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", all_posts=post_objects)


@app.route('/blog/<int:number_of_blog>')
def blog_page(number_of_blog):
    return render_template("post.html", number_of_blog=number_of_blog, blog_post=post_objects[number_of_blog-1])


if __name__ == "__main__":
    app.run(debug=True)
