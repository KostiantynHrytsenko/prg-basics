class SocialMediaProfile:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def add_post(self, content):
        self.posts.append(content)
        print(f"{self.username} added a new post: {content}")

    def display_timeline(self):
        print(f"Post history of {self.username}:")
        j = 1
        for i in self.posts:
            print(f"{j}.{self.posts[j - 1]}")
            j+=1

def main():
    profile = SocialMediaProfile("johndoe")
    profile.add_post("Hello world!")
    profile.add_post("Had a great day at the park!")
    profile.add_post("What's up, Natalie? How are you?")
    profile.display_timeline()


if __name__ == "__main__":
    main()
