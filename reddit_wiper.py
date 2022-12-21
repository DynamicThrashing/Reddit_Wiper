from modules.args import parser
from modules.reddit_session import Wiper

from dotenv import dotenv_values


def check_env_file():
    # Check credentials
    config = dotenv_values(".env")

    # Confirm all credentials are found, else throw an error.
    for field, required_value in config.items():
        if not required_value:
            raise ValueError(
                f"Please make sure the .env file is created in the root directory and that {field} value exists."
            )
        return config


if __name__ == "__main__":
    # Reddit app credentials
    config = check_env_file()

    # get command line options inputted by user
    options = vars(parser.parse_args())

    # Reddit session
    wiper = Wiper(**config)

    if options["delete_e"]:  # delete everything
        print("Deleting all comments:")
        wiper.delete_comments(comment_count=None, no_confirm=options["no_confirm"])
        print("Deleting all submissions:")
        wiper.delete_submissions(
            submissions_count=None, no_confirm=options["no_confirm"]
        )
    elif options["number_of_comments"] != 0:
        print("Deleting comments: ")
        wiper.delete_comments(
            comment_count=options["number_of_comments"],
            no_confirm=options["no_confirm"],
        )
    elif options["number_of_submissions"] != 0:
        print("Deleting submissions: ")
        wiper.delete_submissions(
            submissions_count=options["number_of_submissions"],
            no_confirm=options["no_confirm"],
        )

    print("Script Completed \n")
