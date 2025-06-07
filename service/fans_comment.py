from repository.fan_comment_repo import CommentRepository

class FansCommentUseCase:
    def __init__(self, comment_repo: CommentRepository):
        self.comment_repo = comment_repo

    def save_fans_comment_to_db(self, team_name, username, comment):
        return self.comment_repo.add_fans_comment(team_name, username, comment)