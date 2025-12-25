<<<<<<< HEAD
class User:
    # Other methods remain the same...

    def view_feed(self):
        print(f"{self.name}'s Feed:")
        for user in self.following:
            for post in user.posts:
                print(f"{post.author.name}: {post.content} ({post.timestamp})")
=======
class User:
    # Other methods remain the same...

    def view_feed(self):
        print(f"{self.name}'s Feed:")
        for user in self.following:
            for post in user.posts:
                print(f"{post.author.name}: {post.content} ({post.timestamp})")
>>>>>>> ad12eb181427590f30d26fd51061b42124f2f380
