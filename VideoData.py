# -*- coding: utf-8 -*-
import json
import urllib
import isodate
from settings import API_KEY


class VideoData:

    def __init__(self, li_usernames, li_ids_videos):
        self.usernames = li_usernames
        self.ids_video = li_ids_videos

    def printing(self):
        print self.usernames
        print self.ids_video
        return

    '''
    This method return the times of every event video for student
    dict_tplays_videos_students: return the total times of play_video event for every video and for every student
    dict_tstops_videos_students: return the total times of stop_video event for every video and for every student
    dict_tpauses_videos_students: return the total times of pause_video event for every video and for every student
    '''
    def calculate_times_plstpa_event(self, json_file):
        dict_videos_times = {}
        dict_tplays_videos_students = {}
        dict_tstops_videos_students = {}
        dict_tpauses_videos_students = {}

        for video in self.ids_video:
            dict_videos_times[video] = 0

        for student in self.usernames:
            dict_tplays_videos_students[student] = dict_videos_times.copy()
            dict_tstops_videos_students[student] = dict_videos_times.copy()
            dict_tpauses_videos_students[student] = dict_videos_times.copy()

        for line in json_file:
            if not ("name" not in line):
                if line["name"] == "play_video":
                    stud = str(line["username"])
                    event = line['event']
                    elements_events = json.loads(event)
                    code_video = str(elements_events['code'])
                    dict_tplays_videos_students[stud][str(code_video)] = dict_tplays_videos_students[stud][code_video]+1

                if line["name"] == "stop_video":
                    stud = str(line["username"])
                    event = line['event']
                    elements_events = json.loads(event)
                    code_video = str(elements_events['code'])
                    dict_tstops_videos_students[stud][str(code_video)] = dict_tstops_videos_students[stud][code_video]+1

                if line["name"] == "pause_video":
                    stud = str(line["username"])
                    event = line['event']
                    elements_events = json.loads(event)
                    code_video = str(elements_events['code'])
                    dict_tpauses_videos_students[stud][str(code_video)] = dict_tpauses_videos_students[stud][code_video]+1

        return dict_tplays_videos_students, dict_tstops_videos_students, dict_tpauses_videos_students

    '''
    This method return a dictionary of students where every student have another
    dictionary of videos where the number of every video is the times of seek video event
    success. Seek event is divided in two types seek backward and seek forward.
    dict_tseek_for_videos_student:return the total times of seek_video forward event for every video and for every student
    dict_tseek_back_videos_students:return the total times of seek_video backward event for every video and for every student
    '''
    def calculate_number_kind_seeks(self, json_file):
        dict_video_seek_num = {}
        dict_tseek_for_videos_student = {}
        dict_tseek_back_videos_students = {}

        for video in self.ids_video:
            dict_video_seek_num[str(video)] = 0

        for student in self.usernames:
            dict_tseek_for_videos_student[str(student)] = dict_video_seek_num.copy()

        for student in self.usernames:
            dict_tseek_back_videos_students[str(student)] = dict_video_seek_num.copy()

        for line in json_file:
            if not ("name" not in line):
                if line["name"] == "seek_video":
                    stud = str(line["username"])
                    event = line['event']
                    elements_events = json.loads(event)
                    code_video = str(elements_events['code'])
                    old_time = str(elements_events['old_time'])
                    new_time = str(elements_events['new_time'])

                    if old_time != "None" and new_time != "None":

                        if float(old_time) > float(new_time):
                            dict_tseek_back_videos_students[stud][str(code_video)] = dict_tseek_back_videos_students[stud][str(code_video)]+1

                        if float(old_time) < float(new_time):
                            dict_tseek_for_videos_student[stud][str(code_video)] = dict_tseek_for_videos_student[stud][str(code_video)]+1

        return dict_tseek_for_videos_student, dict_tseek_back_videos_students

    '''
    This method return 6 diferent dictionaries, all dictionaris have every videos key:
    dict_tseek_for_videos: return the total number of times of seek forward for every video
    dict_tseek_back_videos: return the total number of times of seek backward for every video
    dict_seek_for_av_videos: return the average time of every seek forward events
    dict_seek_back_av_videos: return the average time of every seek backward events
    dict_seek_for_acc_time_videos: return the accumulated time of all seek forward events
    dict_seek_back_acc_time_videos: return the accumulated time of all seek backward events
    '''
    def calculate_average_ac_time_kind_seeks(self, json_file):
        dict_tseek_for_videos = {}
        dict_tseek_back_videos = {}
        dict_seek_for_av_videos = {}
        dict_seek_back_av_videos = {}
        dict_seek_for_acc_time_videos = {}
        dict_seek_back_acc_time_videos = {}

        for video in self.ids_video:
            dict_tseek_for_videos[str(video)] = 0
            dict_tseek_back_videos[str(video)] = 0
            dict_seek_for_av_videos[str(video)] = float(0)
            dict_seek_back_av_videos[str(video)] = float(0)
            dict_seek_for_acc_time_videos[str(video)] = float(0)
            dict_seek_back_acc_time_videos[str(video)] = float(0)

        for line in json_file:
            if not ("name" not in line):
                if line["name"] == "seek_video":
                    event = line['event']
                    elements_events = json.loads(event)
                    code_video = str(elements_events['code'])
                    old_time = str(elements_events['old_time'])
                    new_time = str(elements_events['new_time'])

                    if old_time != "None" and new_time != "None":
                        if float(old_time) > float(new_time):
                            time_replayed = float(old_time)-float(new_time)
                            dict_seek_back_av_videos[str(code_video)] = dict_seek_back_av_videos[str(code_video)] + time_replayed
                            dict_seek_back_acc_time_videos[str(code_video)] = dict_seek_back_acc_time_videos[str(code_video)] + time_replayed
                            dict_tseek_back_videos[str(code_video)] = dict_tseek_back_videos[str(code_video)] + 1

                        if float(old_time) < float(new_time):
                            time_skipped = float(new_time)-float(old_time)
                            dict_seek_for_av_videos[str(code_video)] = dict_seek_for_av_videos[str(code_video)] + time_skipped
                            dict_seek_for_acc_time_videos[str(code_video)] = dict_seek_for_acc_time_videos[str(code_video)] + time_skipped
                            dict_tseek_for_videos[str(code_video)] = dict_tseek_for_videos[str(code_video)] + 1

        for video in self.ids_video:
            if dict_seek_for_av_videos[str(video)] != float(0):
                dict_seek_for_av_videos[str(video)] = dict_seek_for_av_videos[str(video)]/dict_tseek_for_videos[str(video)]
            if dict_seek_back_av_videos[str(video)] != float(0):
                dict_seek_back_av_videos[str(video)] = dict_seek_back_av_videos[str(video)]/dict_tseek_back_videos[str(video)]

        return dict_seek_for_av_videos, dict_seek_back_av_videos, dict_seek_for_acc_time_videos, dict_seek_back_acc_time_videos, dict_tseek_back_videos, dict_tseek_for_videos

    '''
    This method calculate the number of times of change speed and the average of changed speed.
    Change_speed_video event is divided in two different events, change speed down and change speed up.
    dict_change_speed_up_average_videos: returns a dictionary of videos with the speed up average
    dict_change_speed_up_times_videos: returns a dictionary of videos with number of times of speed up
    dict_change_speed_down_average_videos: returns a dictionary of videos with the speed down average
    dict_change_speed_down_times_videos: returns a dictionary of videos with number of times of speed down

    '''
    def calculate_change_speed(self, json_file):
        dict_change_speed_up_average_videos = {}
        dict_change_speed_up_times_videos = {}
        dict_change_speed_down_average_videos = {}
        dict_change_speed_down_times_videos = {}

        for video in self.ids_video:
            dict_change_speed_up_average_videos[str(video)] = 0
            dict_change_speed_down_average_videos[str(video)] = 0
            dict_change_speed_up_times_videos[str(video)] = 0
            dict_change_speed_down_times_videos[str(video)] = 0

        for line in json_file:
            if not ("name" not in line):
                if line["name"] == "speed_change_video":
                    event = line['event']
                    elements_events = json.loads(event)
                    code_video = str(elements_events['code'])
                    old_speed = str(elements_events['old_speed'])
                    new_speed = str(elements_events['new_speed'])

                    if float(old_speed) < float(new_speed):
                        dict_change_speed_up_average_videos[str(code_video)] = dict_change_speed_up_average_videos[str(code_video)] + float(new_speed)
                        dict_change_speed_up_times_videos[str(code_video)] = dict_change_speed_up_times_videos[str(code_video)]+1

                    if float(old_speed) > float(new_speed):
                        dict_change_speed_down_average_videos[str(code_video)] = dict_change_speed_down_average_videos[str(code_video)] + float(new_speed)
                        dict_change_speed_down_times_videos[str(code_video)] = dict_change_speed_down_times_videos[str(code_video)]+1

        for video in self.ids_video:
            if dict_change_speed_up_times_videos[str(video)] != 0:
                dict_change_speed_up_average_videos[str(video)] = float(dict_change_speed_up_average_videos[str(video)])/dict_change_speed_up_times_videos[str(video)]

            if dict_change_speed_down_times_videos[str(video)] != 0:
                dict_change_speed_down_average_videos[str(video)] = float(dict_change_speed_down_average_videos[str(video)])/dict_change_speed_down_times_videos[str(video)]

        return dict_change_speed_up_average_videos, dict_change_speed_up_times_videos, dict_change_speed_down_average_videos, dict_change_speed_down_times_videos

    '''
    This method calcuates for every video the total number of play, stop and pause events.
    dict_times_plays_videos: this method returns for every video the total of play events
    dict_times_stops_videos: this method returns for every video the total of stop events
    dict_times_pauses_videos: this method returns for every video the total of pause events
    '''
    def calculate_number_plstpa_events(self, json_file):
        dict_times_plays_videos = {}
        dict_times_stops_videos = {}
        dict_times_pauses_videos = {}

        for video in self.ids_video:
            dict_times_plays_videos[str(video)] = 0
            dict_times_stops_videos[str(video)] = 0
            dict_times_pauses_videos[str(video)] = 0

        for line in json_file:
            if not ("name" not in line):
                if line['event_type'] == "play_video":
                    event = line['event']
                    elements_events = json.loads(event)
                    code_video = str(elements_events['code'])
                    dict_times_plays_videos[code_video] = dict_times_plays_videos[code_video]+1

                if line['event_type'] == "stop_video":
                    event = line['event']
                    elements_events = json.loads(event)
                    code_video = str(elements_events['code'])
                    dict_times_stops_videos[code_video] = dict_times_stops_videos[code_video]+1

                if line['event_type'] == "pause_video":
                    event = line['event']
                    elements_events = json.loads(event)
                    code_video = str(elements_events['code'])
                    dict_times_pauses_videos[code_video] = dict_times_pauses_videos[code_video]+1

        return dict_times_plays_videos, dict_times_stops_videos, dict_times_pauses_videos

    '''
    This method calculates the duration of every video, it uses youtube api v3 for calculae it.
    dict_durations_yt_videos: returns a dictionary with the durations of every videos.
    dict_titles_yt_videos: return the title of every video
    '''
    def calculate_duration_videos(self):
        dict_durations_yt_videos = {}
        dict_titles_yt_videos = {}
        for video in self.ids_video:
            dict_titles_yt_videos[str(video)] = ""
            dict_durations_yt_videos[str(video)] = 0

        for video in self.ids_video:
            video_id = str(video)
            api_key = API_KEY
            searchUrl = "https://www.googleapis.com/youtube/v3/videos?id="+video_id+"&key="+api_key+"&part=snippet,contentDetails"
            response = urllib.urlopen(searchUrl).read()
            data = json.loads(response)
            all_data = data['items']
            snippet = all_data[0]['snippet']
            title = str(snippet['title'].encode('utf8'))
            contentDetails = all_data[0]['contentDetails']
            dur = isodate.parse_duration(contentDetails['duration'])
            dict_durations_yt_videos[video_id] = dur.total_seconds()
            dict_titles_yt_videos[video_id] = title

        return dict_durations_yt_videos, dict_titles_yt_videos

    '''
    This method calculates the total time of video viwed.
    dict_video_time_viwed_students: it returns a dictionary students wehre
    all students contains other dictionay of videos, every video have
    the total time viewed in seconds.
    '''
    def calculate_time_video_watched_student(self, json_file):
        dict_video_list = {}
        dict_video_list_students = {}
        dict_video_time_viwed_students = {}

        for video in self.ids_video:
            dict_video_list[str(video)] = 0

        for student in self.usernames:
            dict_video_list_students[str(student)] = dict_video_list.copy()
            dict_video_time_viwed_students[str(student)] = dict_video_list.copy()

        for student in self.usernames:
            for video in self.ids_video:
                dict_video_list_students[str(student)][str(video)] = []
                dict_video_time_viwed_students[str(student)][str(video)] = 0

        for line in json_file:
            if not ("name" not in line):
                if line['name'] == "pause_video":
                    student = str(line["username"])
                    event = line['event']
                    elements_events = json.loads(event)
                    code_video = str(elements_events['code'])
                    time = str(elements_events['currentTime'])
                    if time != "None":
                        li_pause = ["pause", time]
                        dict_video_list_students[student][code_video].append(li_pause)

                if line['name'] == "stop_video":
                    student = str(line["username"])
                    event = line['event']
                    elements_events = json.loads(event)
                    code_video = str(elements_events['code'])
                    time = str(elements_events['currentTime'])
                    if time != "None":
                        li_stop = ["stop", time]
                        dict_video_list_students[student][code_video].append(li_stop)

                if line['event_type'] == "play_video":
                    student = str(line["username"])
                    event = line['event']
                    elements_events = json.loads(event)
                    code_video = str(elements_events['code'])
                    time = str(elements_events['currentTime'])
                    if time != "None":
                        li_play = ["play", time]
                        dict_video_list_students[student][code_video].append(li_play)

        for student in self.usernames:
            for video in self.ids_video:
                '''I filtered for >1 because we need minimum 2 events 1:play 2:pause/stop'''
                total_time = 0
                if len(dict_video_list_students[str(student)][str(video)]) > 1:
                    i = 0
                    for line in dict_video_list_students[str(student)][str(video)]:
                        if i < len(dict_video_list_students[str(student)][str(video)])-1:
                            if dict_video_list_students[str(student)][str(video)][i][0] == "play" and (dict_video_list_students[str(student)][str(video)][i+1][0] == "stop" or dict_video_list_students[str(student)][str(video)][i+1][0] == "pause"):
                                play_time = float(dict_video_list_students[str(student)][str(video)][i][1])
                                stop_time = float(dict_video_list_students[str(student)][str(video)][i+1][1])
                                total_time = total_time+(stop_time-play_time)

                        i = i+1

                dict_video_time_viwed_students[str(student)][str(video)] = total_time

        return dict_video_time_viwed_students

    '''
    This method calculates the quota, this is timeViwedVideo / durationVideo
    for every student and video.
    dict_quotas_video_students: it returns the quota for every student and video
    '''
    def calculate_quota_video_viwed(self, dict_total_times_video, dict_video_time_viwed_student):
        dict_quotas_video_students = {}
        dict_video_list = {}

        for video in self.ids_video:
            dict_video_list[str(video)] = 0

        for student in self.usernames:
            dict_quotas_video_students[str(student)] = dict_video_list.copy()

        for student in self.usernames:
            for video in self.ids_video:
                viewed = dict_video_time_viwed_student[str(student)][str(video)]
                all_time = dict_total_times_video[str(video)]
                quota = abs(viewed/all_time)
                dict_quotas_video_students[str(student)][str(video)] = round(quota, 2)

        return dict_quotas_video_students

    '''
    This method calculates the viwed total accumulated time for every video and
    the average of time viewd video.
    dict_accumulated_time_videos: it returns the total time viwed accumulated in seconds
    dict_average_time_videos: it returns the average of time viwed in seconds
    '''
    def calculate_accumulated_and_average_time_viewed_video(self, dict_video_time_viwed_student):
        dict_accumulated_time_videos = {}
        dict_average_time_videos = {}

        for video in self.ids_video:
            dict_accumulated_time_videos[str(video)] = 0
            dict_average_time_videos[str(video)] = 0

        for video in self.ids_video:
            for student in self.usernames:
                dict_accumulated_time_videos[str(video)] = dict_accumulated_time_videos[str(video)]+dict_video_time_viwed_student[str(student)][str(video)]
                dict_average_time_videos[str(video)] = dict_average_time_videos[str(video)]+dict_video_time_viwed_student[str(student)][str(video)]

        for video in self.ids_video:
            dict_average_time_videos[str(video)] = dict_average_time_videos[str(video)]/len(self.usernames)

        return dict_accumulated_time_videos, dict_average_time_videos

    '''
    This method calculates for student and every video the data of all events but without redundant data.
    dict_video_list_events_students: returns a dictionary with for every student and video, thant dictionary contains a list
    with the different video events for this video and student.
    '''
    def calculate_list_video_events_without_redundant_data(self, json_file):
        dict_video_list = {}
        dict_video_list_students = {}
        dict_video_time_viwed_student = {}
        dict_video_list_events_students = {}

        for video in self.ids_video:
            dict_video_list[str(video)] = 0

        for student in self.usernames:
            dict_video_list_students[str(student)] = dict_video_list.copy()
            dict_video_time_viwed_student[str(student)] = dict_video_list.copy()
            dict_video_list_events_students[str(student)] = dict_video_list.copy()

        for student in self.usernames:
            for video in self.ids_video:
                dict_video_list_students[str(student)][str(video)] = []
                dict_video_time_viwed_student[str(student)][str(video)] = 0
                dict_video_list_events_students[str(student)][str(video)] = []

        for line in json_file:
            if "name" in line:
                if line['name'] == "stop_video":
                    student = str(line["username"])
                    event = line['event']
                    elements_events = json.loads(event)
                    code_video = str(elements_events['code'])
                    time = str(elements_events['currentTime'])
                    if time != "None":
                        li_stop = ["stop", time]
                        dict_video_list_students[student][code_video].append(li_stop)

                if line['name'] == "play_video":
                    student = str(line["username"])
                    event = line['event']
                    elements_events = json.loads(event)
                    code_video = str(elements_events['code'])
                    time = str(elements_events['currentTime'])
                    if time != "None":
                        li_play = ["play", time]
                        dict_video_list_students[student][code_video].append(li_play)

                if line['name'] == "pause_video":
                    student = str(line["username"])
                    event = line['event']
                    elements_events = json.loads(event)
                    code_video = str(elements_events['code'])
                    time = str(elements_events['currentTime'])
                    if time != "None":
                        li_pause = ["pause", time]
                        dict_video_list_students[student][code_video].append(li_pause)

                if line['name'] == "seek_video":
                    student = str(line["username"])
                    event = line['event']
                    elements_events = json.loads(event)
                    code_video = str(elements_events['code'])
                    old_time = str(elements_events['old_time'])
                    new_time = str(elements_events['new_time'])
                    if old_time != "None" and new_time != "None":
                        li_seek = ["seek", old_time, new_time]
                        dict_video_list_students[student][code_video].append(li_seek)

                if line["name"] == "speed_change_video":
                    student = str(line["username"])
                    event = line['event']
                    elements_events = json.loads(event)
                    code_video = str(elements_events['code'])
                    old_speed = str(elements_events['old_speed'])
                    new_speed = str(elements_events['new_speed'])
                    li_speed = ["speed", old_speed, new_speed]
                    dict_video_list_students[student][code_video].append(li_speed)

        for student in self.usernames:
            for video in self.ids_video:
                i = 0
                if dict_video_list_students[student][video] > 0:
                    for line in dict_video_list_students[student][video]:
                        if i < len(dict_video_list_students[student][video])-1:
                            if cmp(dict_video_list_students[student][video][i], dict_video_list_students[student][video][i+1]) == 0:
                                i = i+1
                            else:
                                dict_video_list_events_students[student][video].append(dict_video_list_students[student][video][i])
                                i = i+1
                        else:
                            dict_video_list_events_students[student][video].append(dict_video_list_students[student][video][i])
                            i = i+1

        return dict_video_list_events_students

    '''
    This method calculates the number times thaht happens every video event without redundant data
    dict_nr_stops_videos: returns a dictionary of videos with the number of stops for every video
    dict_nr_plays_videos: returns a dictionary of videos with the number of plays for every video
    dict_nr_pauses_videos: returns a dictionary of videos with the number of pauses for every video
    dict_nr_seek_for_videos: returns a dictionary of videos with the number of seek forward for every video
    dict_nr_seek_back_vidoes: returns a dictionary of videos with the number of seek backward for every video
    dict_nr_speed_up_videos: returns a dictionary of videos with the number of speed ups for every video
    dict_nr_speed_down_videos: returns a dictionary of videos with the number of speed downs for every video
    '''
    def calculate_times_every_video_events_without_redundant_data(self, dict_video_list_events_students):
        dict_nr_stops_videos = {}
        dict_nr_plays_videos = {}
        dict_nr_pauses_videos = {}
        dict_nr_seek_for_videos = {}
        dict_nr_seek_back_vidoes = {}
        dict_nr_speed_up_videos = {}
        dict_nr_speed_down_videos = {}

        for video in self.ids_video:
            dict_nr_stops_videos[str(video)] = 0
            dict_nr_plays_videos[str(video)] = 0
            dict_nr_pauses_videos[str(video)] = 0
            dict_nr_seek_for_videos[str(video)] = 0
            dict_nr_seek_back_vidoes[str(video)] = 0
            dict_nr_speed_up_videos[str(video)] = 0
            dict_nr_speed_down_videos[str(video)] = 0

        for student in self.usernames:
            for video in self.ids_video:
                for line in dict_video_list_events_students[student][video]:
                    if line[0] == "pause":
                        dict_nr_pauses_videos[video] += 1

                    if line[0] == "stop":
                        dict_nr_stops_videos[video] += 1

                    if line[0] == "play":
                        dict_nr_plays_videos[video] += 1

                    if line[0] == "seek":
                        if float(line[1]) > float(line[2]):
                            dict_nr_seek_back_vidoes[str(video)] += 1

                        if float(line[1]) < float(line[2]):
                            dict_nr_seek_for_videos[str(video)] += 1

                    if line[0] == "speed":
                        if float(line[1]) > float(line[2]):
                            dict_nr_speed_up_videos[str(video)] += 1

                        if float(line[1]) < float(line[2]):
                            dict_nr_speed_down_videos[str(video)] += 1

        return dict_nr_pauses_videos, dict_nr_stops_videos, dict_nr_plays_videos, dict_nr_seek_back_vidoes, dict_nr_seek_for_videos, dict_nr_speed_up_videos, dict_nr_speed_down_videos
