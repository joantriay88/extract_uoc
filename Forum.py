# -*- coding: utf-8 -*-


class Forum (object):

    def __init__(self):
        pass

    def calculate_threads_created(self, json_file):
        lines_thread_created = []
        line_data = "Username#CommentID#UnicIDThread#UserRole#Title#Body\n"
        lines_thread_created.append(line_data)
        for line in json_file:
            if "name" in line:
                if line['name'] == "edx.forum.thread.created":
                    line_data = ""
                    username = str(line['username'])
                    event = line['event']
                    body = str(event['body'].encode('utf8')).replace("\n", " ")
                    commentable_id = str(event['commentable_id'])
                    u_id = str(event['id'])
                    title = str(event['title'].encode('utf8')).replace("\n", " ")
                    user_forums_roles = event['user_forums_roles']
                    line_users = ""
                    i = 0
                    for roles_users in user_forums_roles:
                        if i == 0:
                            line_users = str(roles_users)
                            i += 1
                        else:
                            line_users = line_users+";"+str(roles_users)
                            i += 1

                    line_data = username+"#"+commentable_id+"#"+u_id+"#"+line_users+"#"+title+"#"+body+"\n"
                    lines_thread_created.append(line_data)
        return lines_thread_created

    def calculate_responses_created(self, json_file):
        lines_response_created = []
        line_data = "Username#CommentID#UnicIDThread#UnicIDResponse#UserRole#Body\n"
        lines_response_created.append(line_data)

        for line in json_file:
            if "name" in line:
                if line['name'] == "edx.forum.response.created":
                    line_data = ""
                    username = str(line['username'])
                    event = line['event']
                    body = str(event['body'].encode('utf8')).replace("\n", " ")
                    commentable_id = str(event['commentable_id'])
                    discussion = event['discussion']
                    thread_u_id = str(discussion['id'])
                    u_id = str(event['id'])
                    user_forums_roles = event['user_forums_roles']
                    line_users = ""
                    i = 0
                    for roles_users in user_forums_roles:
                        if i == 0:
                            line_users = str(roles_users)
                            i += 1
                        else:
                            line_users = line_users+";"+str(roles_users)
                            i += 1

                    line_data = username+"#"+commentable_id+"#"+thread_u_id+"#"+u_id+"#"+line_users+"#"+body+"\n"
                    lines_response_created.append(line_data)

        return lines_response_created

    def calculate_comments_created(self, json_file):
        lines_comment_created = []
        line_data = "Username#CommentId#UnicIdResponse#UnicIdComment#UserRole#Body\n"
        lines_comment_created.append(line_data)

        for line in json_file:
            if "name" in line:
                if line['name'] == "edx.forum.comment.created":
                    line_data = ""
                    username = str(line['username'])
                    event = line['event']
                    body = str(event['body'].encode('utf8')).replace("\n", " ")
                    commentable_id = str(event['commentable_id'])
                    response = event['response']
                    response_id = str(response['id'])
                    u_id = str(event['id'])
                    user_forums_roles = event['user_forums_roles']
                    line_users = ""
                    i = 0
                    for roles_users in user_forums_roles:
                        if i == 0:
                            line_users = str(roles_users)
                            i += 1
                        else:
                            line_users = line_users+";"+str(roles_users)
                            i += 1

                    line_data = username+"#"+commentable_id+"#"+response_id+"#"+u_id+"#"+line_users+"#"+body+"\n"
                    lines_comment_created.append(line_data)

        return lines_comment_created
