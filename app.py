import time

from config import reddit_config
from reddit_func import get_reddit_object, calculate_users, print_top_users


def main():
    start_time = time.time()
    reddit = get_reddit_object(reddit_config)
    subreddit_name = input("Введите название сабреддита: ")
    top_posts, top_comments = calculate_users(reddit, subreddit_name)
    print_top_users(top_posts, top_comments)
    print(f"Время работы программы: {time.time() - start_time:.2f} секунд")


if __name__ == '__main__':
    main()
