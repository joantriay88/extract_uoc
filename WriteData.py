# -*- coding: utf-8 -*-
from settings import TEXT_FILES_PATH


class WriteData:
    def __init__(self, li_usernames, li_ids_videos):
        self.usernames = li_usernames
        self.ids_video = li_ids_videos

    '''
    This method writhes in a file a video dictionary data calculated
    '''
    def writeInFileDictSampleData(self, dict_data, name_file):
        fileToWrite = open(TEXT_FILES_PATH+name_file, 'a')
        for video in self.ids_video:
            line = str(video)+","+str(dict_data[video])+"\n"
            fileToWrite.write(line)
        fileToWrite.close()
        return

    '''
    This method writes in a file a video student dictionary data calculated
    '''
    def writeInFileDictComplexData(self, dict_data, name_file):
        fileToWrite = open(TEXT_FILES_PATH+name_file, 'a')
        for stud in self.usernames:
            line = stud+","
            counter_last_element = 1
            for video in self.ids_video:
                if counter_last_element == len(self.ids_video):
                    line = line+str(dict_data[stud][video])
                else:
                    line = line+str(dict_data[stud][video])+","
                    counter_last_element = counter_last_element+1
            fileToWrite.write(line+"\n")
        fileToWrite.close()
        return

    '''
    This method writes in a file a list based on strings.
    '''
    def writeInFileStringList(self, strList, file_name):
        fileToWrite = open(TEXT_FILES_PATH+file_name, 'a')
        for line in strList:
            fileToWrite.write(str(line))
        fileToWrite.close()
        return

    '''
    This method writes in a file the names of students
    '''
    def writeName(self, name_file):
        fileToWrite = open(TEXT_FILES_PATH+name_file, 'a')
        for name in self.usernames:
            fileToWrite.write(str(name)+"\n")
        fileToWrite.close()
        return

    '''This method split the first data line'''
    def split_first_data(self, line):
        div = line.split(",")
        data = div[1].split("\n")
        return str(div[0]), str(data[0])

    '''This method split other data lines, not the first'''
    def split_data(slef, line):
        div = line.split(",")
        div = div[1].split("\n")
        return str(div[0])

    def join_video_data(self):
        f = open(TEXT_FILES_PATH+"title_v.txt", "r")
        title = f.readlines()
        f.close()

        f = open(TEXT_FILES_PATH+"duration_v.txt", "r")
        duration = f.readlines()
        f.close()

        f = open(TEXT_FILES_PATH+"n_plays_v.txt", "r")
        plays = f.readlines()
        f.close()

        f = open(TEXT_FILES_PATH+"n_stops_v.txt", "r")
        stops = f.readlines()
        f.close()

        f = open(TEXT_FILES_PATH+"n_pauses_v.txt", "r")
        pauses = f.readlines()
        f.close()

        f = open(TEXT_FILES_PATH+"n_seekBack_v.txt", "r")
        seekBacks = f.readlines()
        f.close()

        f = open(TEXT_FILES_PATH+"n_seekFor_v.txt", "r")
        seekFors = f.readlines()
        f.close()

        f = open(TEXT_FILES_PATH+"n_speedUp_v.txt", "r")
        speedUps = f.readlines()
        f.close()

        f = open(TEXT_FILES_PATH+"n_speedDown_v.txt", "r")
        speedDowns = f.readlines()
        f.close()

        f = open(TEXT_FILES_PATH+"av_speedUp_v.txt", "r")
        av_speedUp = f.readlines()
        f.close()

        f = open(TEXT_FILES_PATH+"av_speedDown_v.txt", "r")
        av_speedDown = f.readlines()
        f.close()

        f = open(TEXT_FILES_PATH+"acc_t_seekBack_v.txt", "r")
        acc_t_seekBack = f.readlines()
        f.close()

        f = open(TEXT_FILES_PATH+"acc_t_seekFor_v.txt", "r")
        acc_t_seekFor = f.readlines()
        f.close()

        f = open(TEXT_FILES_PATH+"av_t_seekBack_v.txt", "r")
        av_t_seekBack = f.readlines()
        f.close()

        f = open(TEXT_FILES_PATH+"av_t_seekFor_v.txt", "r")
        av_t_seekFor = f.readlines()
        f.close()

        f = open(TEXT_FILES_PATH+"acc_t_viewed_v.txt", "r")
        acc_t_viewed = f.readlines()
        f.close()

        f = open(TEXT_FILES_PATH+"av_t_viewed_v.txt", "r")
        av_t_viewed = f.readlines()
        f.close()

        fileData = open(TEXT_FILES_PATH+"AllVariablesVideo.txt", "a")

        fileData.write("VideoId,VideoName,Duration,Plays,Stops,Pauses,SeekBacks,SeekFors,SpeedUps,SpeedDowns,AvSpeedUp,AvSpeedDown,AccTimeReplayed,AccTimeSkipped,AvTimeReplayed,AvTimeSkipped,AccTimeViwed,AvTimeViewed\n")

        for i in range(len(title)):
            video_id, title_data = self.split_first_data(title[i])
            duration_data = self.split_data(duration[i])
            play_data = self.split_data(plays[i])
            stop_data = self.split_data(stops[i])
            pause_data = self.split_data(pauses[i])
            seek_back_data = self.split_data(seekBacks[i])
            seek_for_data = self.split_data(seekFors[i])
            speed_up_data = self.split_data(speedUps[i])
            speed_down_data = self.split_data(speedDowns[i])
            av_speedUp_data = self.split_data(av_speedUp[i])
            av_speedDown_data = self.split_data(av_speedDown[i])
            acc_t_seekBack_data = self.split_data(acc_t_seekBack[i])
            acc_t_seekFor_data = self.split_data(acc_t_seekFor[i])
            av_t_seekBack_data = self.split_data(av_t_seekBack[i])
            av_t_seekFor_data = self.split_data(av_t_seekFor[i])
            acc_t_viewed_data = self.split_data(acc_t_viewed[i])
            av_t_viewed_data = self.split_data(av_t_viewed[i])

            line = video_id+","+title_data+","+duration_data+","+play_data+","+stop_data+","+pause_data+","+seek_back_data+","+seek_for_data+","+speed_up_data+","+speed_down_data+","+av_speedUp_data+","+av_speedDown_data+","+acc_t_seekBack_data+","+acc_t_seekFor_data+","+av_t_seekBack_data+","+av_t_seekFor_data+","+acc_t_viewed_data+","+av_t_viewed_data+"\n"
            fileData.write(line)

        fileData.close()
        return

    def join_video_data_no_redundant(self):
        f = open(TEXT_FILES_PATH+"title_v.txt", "r")
        title = f.readlines()
        f.close()

        f = open(TEXT_FILES_PATH+"duration_v.txt", "r")
        duration = f.readlines()
        f.close()

        f = open(TEXT_FILES_PATH+"nw_plays_v.txt", "r")
        plays = f.readlines()
        f.close()

        f = open(TEXT_FILES_PATH+"nw_stops_v.txt", "r")
        stops = f.readlines()
        f.close()

        f = open(TEXT_FILES_PATH+"nw_pauses_v.txt", "r")
        pauses = f.readlines()
        f.close()

        f = open(TEXT_FILES_PATH+"nw_seekBack_v.txt", "r")
        seekBacks = f.readlines()
        f.close()

        f = open(TEXT_FILES_PATH+"nw_seekFor_v.txt", "r")
        seekFors = f.readlines()
        f.close()

        f = open(TEXT_FILES_PATH+"nw_speedUp_v.txt", "r")
        speedUps = f.readlines()
        f.close()

        f = open(TEXT_FILES_PATH+"nw_speedDown_v.txt", "r")
        speedDowns = f.readlines()
        f.close()

        f = open(TEXT_FILES_PATH+"av_speedUp_v.txt", "r")
        av_speedUp = f.readlines()
        f.close()

        f = open(TEXT_FILES_PATH+"av_speedDown_v.txt", "r")
        av_speedDown = f.readlines()
        f.close()

        f = open(TEXT_FILES_PATH+"acc_t_seekBack_v.txt", "r")
        acc_t_seekBack = f.readlines()
        f.close()

        f = open(TEXT_FILES_PATH+"acc_t_seekFor_v.txt", "r")
        acc_t_seekFor = f.readlines()
        f.close()

        f = open(TEXT_FILES_PATH+"av_t_seekBack_v.txt", "r")
        av_t_seekBack = f.readlines()
        f.close()

        f = open(TEXT_FILES_PATH+"av_t_seekFor_v.txt", "r")
        av_t_seekFor = f.readlines()
        f.close()

        f = open(TEXT_FILES_PATH+"acc_t_viewed_v.txt", "r")
        acc_t_viewed = f.readlines()
        f.close()

        f = open(TEXT_FILES_PATH+"av_t_viewed_v.txt", "r")
        av_t_viewed = f.readlines()
        f.close()

        fileData = open(TEXT_FILES_PATH+"NoRedAllVariablesVideo.txt", "a")

        fileData.write("VideoId,VideoName,Duration,Plays,Stops,Pauses,SeekBacks,SeekFors,SpeedUps,SpeedDowns,AvSpeedUp,AvSpeedDown,AccTimeReplayed,AccTimeSkipped,AvTimeReplayed,AvTimeSkipped,AccTimeViwed,AvTimeViewed\n")

        for i in range(len(title)):
            video_id, title_data = self.split_first_data(title[i])
            duration_data = self.split_data(duration[i])
            play_data = self.split_data(plays[i])
            stop_data = self.split_data(stops[i])
            pause_data = self.split_data(pauses[i])
            seek_back_data = self.split_data(seekBacks[i])
            seek_for_data = self.split_data(seekFors[i])
            speed_up_data = self.split_data(speedUps[i])
            speed_down_data = self.split_data(speedDowns[i])
            av_speedUp_data = self.split_data(av_speedUp[i])
            av_speedDown_data = self.split_data(av_speedDown[i])
            acc_t_seekBack_data = self.split_data(acc_t_seekBack[i])
            acc_t_seekFor_data = self.split_data(acc_t_seekFor[i])
            av_t_seekBack_data = self.split_data(av_t_seekBack[i])
            av_t_seekFor_data = self.split_data(av_t_seekFor[i])
            acc_t_viewed_data = self.split_data(acc_t_viewed[i])
            av_t_viewed_data = self.split_data(av_t_viewed[i])

            line = video_id+","+title_data+","+duration_data+","+play_data+","+stop_data+","+pause_data+","+seek_back_data+","+seek_for_data+","+speed_up_data+","+speed_down_data+","+av_speedUp_data+","+av_speedDown_data+","+acc_t_seekBack_data+","+acc_t_seekFor_data+","+av_t_seekBack_data+","+av_t_seekFor_data+","+acc_t_viewed_data+","+av_t_viewed_data+"\n"
            fileData.write(line)

        fileData.close()
        return

    def join_all_stud_data(self):

        f = open(TEXT_FILES_PATH+"n_plays_vs.txt", "r")
        playsData = f.readlines()
        f.close

        f = open(TEXT_FILES_PATH+"n_stops_vs.txt", "r")
        stopsData = f.readlines()
        f.close

        f = open(TEXT_FILES_PATH+"n_pauses_vs.txt", "r")
        pausesData = f.readlines()
        f.close

        f = open(TEXT_FILES_PATH+"n_seekBack_vs.txt", "r")
        seekBackData = f.readlines()
        f.close

        f = open(TEXT_FILES_PATH+"n_seekFor_vs.txt", "r")
        seekFordwardsData = f.readlines()
        f.close

        f = open(TEXT_FILES_PATH+"t_viewed_vs.txt", "r")
        timeData = f.readlines()
        f.close

        f = open(TEXT_FILES_PATH+"quota_viewed_vs.txt", "r")
        quotasData = f.readlines()
        f.close

        f = open(TEXT_FILES_PATH+"AllVariablesStudent.txt", "a")

        for i in range(len(stopsData)):
            line = ""
            data_stops = stopsData[i].split("\n")
            data_plays = playsData[i].split("\n")
            data_pauses = pausesData[i].split("\n")
            data_seekBackward = seekBackData[i].split("\n")
            data_seekFordward = seekFordwardsData[i].split("\n")
            data_time_viewed = timeData[i].split("\n")
            data_time_quotas = quotasData[i].split("\n")

            line = self.usernames[i]+","+data_plays[0]+","+data_stops[0]+","+data_pauses[0]+","+data_seekBackward[0]+","+data_seekFordward[0]+","+data_time_viewed[0]+","+data_time_quotas[0]+"\n"
            f.write(line)
        f.close()
        return
