import praw

from collections import Counter
from datetime import datetime, timedelta

from config import reddit_config


def get_reddit_object(reddit_config: dict[str, str]) -> praw.Reddit:
    return praw.Reddit(client_id=reddit_config['client_id'],
                       client_secret=reddit_config['client_secret'],
                       user_agent=reddit_config['user_agent'],
                       username=reddit_config['username'],
                       password=reddit_config['password'],
                       )


def calculate_users(reddit: praw.Reddit,
                    subreddit_name: str,
                    ) -> tuple[Counter, Counter]:
    subreddit = reddit.subreddit(subreddit_name)
    three_days_ago = (datetime.utcnow() - timedelta(days=3)).timestamp()
    post_counter = Counter()
    comment_counter = Counter()
    for post in subreddit.new(limit=None):
        if post.created_utc < three_days_ago:
            break
        if post.author is not None:
            post_counter[post.author.name] += 1
        post.comments.replace_more(limit=None)
        for comment in post.comments.list():
            if comment.created_utc < three_days_ago:
                continue
            if comment.author is not None:
                comment_counter[comment.author.name] += 1
    return post_counter, comment_counter


def print_top_users(post_counter: Counter[str, int],
                    comment_counter: Counter[str, int],
                    ) -> None:
    print("Топ 10 пользователей по количеству постов:")
    if len(post_counter) == 0:
        print('Похоже никого нет -_-')
        return None
    for author, count in sorted(post_counter.items(), key=lambda x: x[1], reverse=True)[:10]:
        print(f"{author}: {count}")
    print('-' * 20)
    print("Топ 10 комментаторов:")
    if len(comment_counter) == 0:
        print('Похоже никого нет -_-')
        return None
    for author, count in sorted(comment_counter.items(), key=lambda x: x[1], reverse=True)[:10]:
        print(f"{author}: {count}")
