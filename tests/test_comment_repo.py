import pytest
from unittest.mock import patch, MagicMock
from repository.fan_comment_repo import CommentRepository

def test_add_fans_comment_success():
    
    repo = CommentRepository()
    team_name = "Arsenal"
    user_name = "Gooner123"
    comment = "I really like this team!"

    # Patch the db session and FansComment
    with patch("repository.fan_comment_repo.FansComment") as MockFansComment:
         with patch("repository.fan_comment_repo.db.session") as mock_session:
             
             result, status_code = repo.add_fans_comment(team_name, user_name, comment)

             # Assert: Verify methods were called correctly
             MockFansComment.assert_called_once_with(team_name=team_name, username=user_name, comment=comment)
            #  mock_session.add.assert_called_once()
            #  mock_session.commit.assert_called_once()
             assert status_code == 202
             assert result["message"] == "Comment added successfully."