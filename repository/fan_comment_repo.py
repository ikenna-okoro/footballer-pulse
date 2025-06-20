from repository.fan_models import FansComment, db

class CommentRepository:

    def add_fans_comment(self, team_name: str, username: str, comment: str):
        new_comment = FansComment(
            team_name=team_name,
            username=username,
            comment=comment
        )
        db.session.add(new_comment)
        db.session.commit()

        return {"message": "Comment added successfully."}, 202