from pygithub3 import Github
import base64
import logging

log = logging.getLogger(__name__)


def get_client(config, user, repo):
    """
    Factory for the Github client
    """
    if 'GITHUB_OAUTH_TOKEN' in config:
        gh = Github(
            base_url=config.get('GITHUB_URL'),
            login=config.get('GITHUB_USER'),
            token=config.get('GITHUB_OAUTH_TOKEN'),
            user=user,
            repo=repo)
    else:
        gh = Github(
            base_url=config.get('GITHUB_URL'),
            login=config.get('GITHUB_USER'),
            password=config.get('GITHUB_PASSWORD'),
            user=user,
            repo=repo)
    return gh
