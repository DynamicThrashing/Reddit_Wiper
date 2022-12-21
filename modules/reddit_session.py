import datetime
import time

import praw


class Wiper:
    def __init__(self, USERNAME="", PASSWORD="", CLIENT_ID="", CLIENT_SECRET=""):
        self.reddit = praw.Reddit(
            username=USERNAME,
            password=PASSWORD,
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            user_agent=f"localhost:Bot Test:v0.1 (by /u/{USERNAME})",
        )

    def delete_comments(self, comment_count=None, no_confirm=False):
        if comments_list := self.reddit.user.me().comments.new(limit=comment_count):
            for comment in comments_list:
                print(f"Comment : {comment.body}")
                print(f"in r/{comment.subreddit}")
                print(
                    f"Posted on: {datetime.datetime.fromtimestamp(int(comment.created))}"
                )
                if no_confirm:
                    comment.delete()
                    print("Deleted. \n")
                    # a 2 sec delay between deletion to adhere to Reddit's 30 requests per minute restriction.
                    time.sleep(2)
                elif deletion_confirmed := self.confirm():
                    comment.delete()
                else:
                    print("Comment saved.\n")

        else:
            print("There are no comments to delete")
        print("Comments deletion complete.")

    def delete_submissions(self, submissions_count=None, no_confirm=False):
        if submissions_list := self.reddit.user.me().submissions.new(
            limit=submissions_count
        ):
            for submission in submissions_list:
                print(f"Submission: {submission.title}")
                print(f"in r/{submission.subreddit}")
                print(
                    f"Submitted on: {datetime.datetime.fromtimestamp(int(submission.created))}"
                )
                if no_confirm:
                    submission.delete()
                    print("Deleted. \n")
                    # a 2 sec delay between deletion to adhere to Reddit's 30 requests per minute restriction.
                    time.sleep(2)
                elif deletion_confirmed := self.confirm():
                    submission.delete()
                else:
                    print("Submission saved.\n")
        else:
            print("There are no submissions to delete")
        print("Submissions deletion complete.")

    def confirm(self):
        confirm_deletion = input("Would you like to delete this? (Y/N): ")
        if confirm_deletion.upper() == "Y":
            return True
        elif confirm_deletion.upper() == "N":
            return False
        else:
            print("Input value error. Please enter (Y/N): \n")
            return self.confirm()
