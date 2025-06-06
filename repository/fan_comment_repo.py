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

        return {"message": "Comment added successfully."}, 201

    # def get_comments_by_fan_id(self, fan_id):
    #     return db.session.query("SELECT * FROM comments WHERE fan_id = ?", (fan_id,))


    # def delete_comment(self, comment_id):
    #     db.session.execute("DELETE FROM comments WHERE id = ?", (comment_id,))
    #     db.session.commit()