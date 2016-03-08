# -*- coding: utf-8 -*-
import json
import Title
import StudentData
import VideoData
import WriteData
import HeatMap
import Forum
from settings import JSON_PATH

initial = Title.Title()

'''********************************* WELCOME *******************************'''
initial.printing()

'''***************************** LOAD JSON FILE **************************'''
jsonfile = open(JSON_PATH, "r")
print "LOADING .JSON FILE..."
json_file = json.load(jsonfile)
print ".JSON FILE LOADED"

'''***************************** SYSTEM VARIABLES **************************'''
li_usernames = []
for line in json_file:
    if len(line) > 0:
        if line['username'] not in li_usernames:
            li_usernames.append(str(line['username']))

print "USERNAMES CALCULATED"

li_ids_video = []
for line in json_file:
    if not ("name" not in line):
        if line['name'] == "stop_video" or line['name'] == "play_video" or line['name'] == "pause_video" or line['name'] == "seek_video":
            event = line['event']
            elements_events = json.loads(event)
            code_video_yt = elements_events['code']
            if code_video_yt not in li_ids_video:
                li_ids_video.append(str(code_video_yt))

print "VIDEO IDS CALCULATED"

'''***************************** OBJECTS ****************************'''
students = StudentData.StudentData()
video_data = VideoData.VideoData(li_usernames, li_ids_video)
write_data = WriteData.WriteData(li_usernames, li_ids_video)
heatmap_data = HeatMap.HeatMap(li_usernames, li_ids_video)
forum_data = Forum.Forum()
print "SYSTEM OBJECTS CREATED"

'''***************************** SYSTEM ****************************'''

dict_tplays_videos_students, dict_tstops_videos_students, dict_tpauses_videos_students = video_data.calculate_times_plstpa_event(json_file)
write_data.writeInFileDictComplexData(dict_tplays_videos_students, "n_plays_vs.txt")


write_data.writeInFileDictComplexData(dict_tstops_videos_students, "n_stops_vs.txt")
write_data.writeInFileDictComplexData(dict_tpauses_videos_students, "n_pauses_vs.txt")


dict_tseek_for_videos_student, dict_tseek_back_videos_students = video_data.calculate_number_kind_seeks(json_file)
write_data.writeInFileDictComplexData(dict_tseek_for_videos_student, "n_seekFor_vs.txt")
write_data.writeInFileDictComplexData(dict_tseek_back_videos_students, "n_seekBack_vs.txt")


dict_seek_for_av_videos, dict_seek_back_av_videos, dict_seek_for_acc_time_videos, dict_seek_back_acc_time_videos, dict_tseek_back_videos, dict_tseek_for_videos = video_data.calculate_average_ac_time_kind_seeks(json_file)
write_data.writeInFileDictSampleData(dict_seek_for_av_videos, "av_t_seekFor_v.txt")
write_data.writeInFileDictSampleData(dict_seek_back_av_videos, "av_t_seekBack_v.txt")
write_data.writeInFileDictSampleData(dict_seek_for_acc_time_videos, "acc_t_seekFor_v.txt")
write_data.writeInFileDictSampleData(dict_seek_back_acc_time_videos, "acc_t_seekBack_v.txt")
write_data.writeInFileDictSampleData(dict_tseek_back_videos, "n_seekBack_v.txt")
write_data.writeInFileDictSampleData(dict_tseek_for_videos, "n_seekFor_v.txt")


dict_change_speed_up_average_videos, dict_change_speed_up_times_videos, dict_change_speed_down_average_videos, dict_change_speed_down_times_videos = video_data.calculate_change_speed(json_file)
write_data.writeInFileDictSampleData(dict_change_speed_up_average_videos, "av_speedUp_v.txt")
write_data.writeInFileDictSampleData(dict_change_speed_up_times_videos, "n_speedUp_v.txt")
write_data.writeInFileDictSampleData(dict_change_speed_down_average_videos, "av_speedDown_v.txt")
write_data.writeInFileDictSampleData(dict_change_speed_down_times_videos, "n_speedDown_v.txt")


dict_tplays_videos, dict_tstops_videos, dict_tpauses_videos = video_data.calculate_number_plstpa_events(json_file)
write_data.writeInFileDictSampleData(dict_tplays_videos, "n_plays_v.txt")
write_data.writeInFileDictSampleData(dict_tstops_videos, "n_stops_v.txt")
write_data.writeInFileDictSampleData(dict_tpauses_videos, "n_pauses_v.txt")


dict_durations_yt_videos, dict_titles_yt_videos = video_data.calculate_duration_videos()
write_data.writeInFileDictSampleData(dict_durations_yt_videos, "duration_v.txt")
write_data.writeInFileDictSampleData(dict_titles_yt_videos, "title_v.txt")


dict_video_time_viwed_students = video_data.calculate_time_video_watched_student(json_file)
write_data.writeInFileDictComplexData(dict_video_time_viwed_students, "t_viewed_vs.txt")


dict_quotas_video_students = video_data.calculate_quota_video_viwed(dict_durations_yt_videos, dict_video_time_viwed_students)
write_data.writeInFileDictComplexData(dict_quotas_video_students, "quota_viewed_vs.txt")


dict_accumulated_time_videos, dict_average_time_videos = video_data.calculate_accumulated_and_average_time_viewed_video(dict_video_time_viwed_students)
write_data.writeInFileDictSampleData(dict_accumulated_time_videos, "acc_t_viewed_v.txt")
write_data.writeInFileDictSampleData(dict_average_time_videos, "av_t_viewed_v.txt")


dict_video_list_events_students = video_data.calculate_list_video_events_without_redundant_data(json_file)


dict_nr_tpauses_videos, dict_nr_tstops_videos, dict_nr_tplays_videos, dict_nr_tseek_back_vidoes, dict_nr_tseek_for_videos, dict_nr_tspeed_up_videos, dict_nr_tspeed_down_videos = video_data.calculate_times_every_video_events_without_redundant_data(dict_video_list_events_students)
write_data.writeInFileDictSampleData(dict_nr_tplays_videos, "nw_plays_v.txt")
write_data.writeInFileDictSampleData(dict_nr_tstops_videos, "nw_stops_v.txt")
write_data.writeInFileDictSampleData(dict_nr_tpauses_videos, "nw_pauses_v.txt")
write_data.writeInFileDictSampleData(dict_nr_tseek_back_vidoes, "nw_seekBack_v.txt")
write_data.writeInFileDictSampleData(dict_nr_tseek_for_videos, "nw_seekFor_v.txt")
write_data.writeInFileDictSampleData(dict_nr_tspeed_up_videos, "nw_speedUp_v.txt")
write_data.writeInFileDictSampleData(dict_nr_tspeed_down_videos, "nw_speedDown_v.txt")


write_data.join_video_data()
write_data.join_video_data_no_redundant()
write_data.join_all_stud_data()


heatmap_data.calculate_matrix(dict_durations_yt_videos, json_file, 15)


lines_thread_created = forum_data.calculate_threads_created(json_file)
write_data.writeInFileStringList(lines_thread_created, "Threads_Forum.txt")

lines_response_created = forum_data.calculate_responses_created(json_file)
write_data.writeInFileStringList(lines_response_created, "Responses_Threads_Forum.txt")

lines_comment_created = forum_data.calculate_comments_created(json_file)
write_data.writeInFileStringList(lines_comment_created, "Comments_Responses_Threads_Forum.txt")
