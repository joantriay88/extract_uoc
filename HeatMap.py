# -*- coding: utf-8 -*-
import json
from settings import ABS_PATH, TSVS_HEATMAP_FILES, HEATMAP_FILES


class HeatMap (object):

    def __init__(self, li_usernames, li_ids_videos):
        self.usernames = li_usernames
        self.ids_video = li_ids_videos

    def calculate_matrix(self, dict_total_duration_video, json_file, resolution):
        dict_video_list_seek = {}

        for video in self.ids_video:
            dict_video_list_seek[str(video)] = []

        for line in json_file:
            if "name" in line:
                if line['event_type'] == "seek_video":
                    student = str(line["username"])
                    if student in self.usernames:
                        event = line['event']
                        elements_events = json.loads(event)
                        code_video = str(elements_events['code'])
                        old_time = str(elements_events['old_time'])
                        new_time = str(elements_events['new_time'])
                        if old_time != "None" and new_time != "None":
                            li_seek = ["seek", old_time, new_time]
                            dict_video_list_seek[code_video].append(li_seek)

        for video in self.ids_video:
            youtube_id = video
            seek_list = dict_video_list_seek[video]
            duration = dict_total_duration_video[video]
            duration = int(duration)
            intervals = (duration/resolution)+1

            li_from_to = []
            i = 0
            while i < intervals:
                li_to = []
                j = 0
                while j < intervals:
                    li_to.append(0)
                    j += 1
                li_from_to.append(li_to)
                i += 1

            for event in seek_list:
                if event[0] == "seek":
                    row_float = float(event[1])
                    col_float = float(event[2])

                    # if row_float > col_float:
                    row = int(row_float)/resolution
                    col = int(col_float)/resolution

                    if int(row_float) > duration:
                        row = duration/resolution
                    if int(col_float) > duration:
                        col = duration/resolution
                    li_from_to[row][col] = li_from_to[row][col]+1

            file_data = open(TSVS_HEATMAP_FILES+"data_heatmap_"+str(youtube_id)+".tsv", "a")
            file_data.write("row_idx\tcol_idx\trepetitions\n")

            i = 0
            while i < intervals:
                j = 0
                while j < intervals:
                    file_data.write(str(i+1)+"\t"+str(j+1)+"\t"+str(li_from_to[i][j])+"\n")
                    j += 1
                i += 1

            file_data.close()
            self.create_html(str(youtube_id), intervals, resolution)

        return

    def create_html(self, youtube_id, intervals, resolution):
        base_html = open(ABS_PATH+"/res/base.html")
        base_data_html = base_html.readlines()
        base_html.close()

        html_file = open(HEATMAP_FILES+"heatmap_"+youtube_id+".html", "a")

        html_file.write('<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//ENhttp://www.w3.org/TR/html4/strict.dtd">\n')
        html_file.write("<html>\n")
        html_file.write("<head>\n")
        html_file.write("<meta charset='utf-8'>\n")
        title = "Heatmap "+youtube_id
        html_file.write("<title>"+title+"</title>\n")
        html_file.write("<link rel='stylesheet' type='text/css' href='"+ABS_PATH+"/res/styleHeatmaps.css'>\n")
        html_file.write("</head>\n")
        html_file.write("<body>\n")
        html_file.write("<div id='tooltip' class='hidden'>\n")
        html_file.write("        <p><span id='value'></p>\n")
        html_file.write("</div>\n")
        html_file.write("<script src='http://d3js.org/d3.v3.min.js'></script>\n")
        html_file.write("<div id='chart' style='overflow:auto; width:960px; height:700px;'></div>\n")
        html_file.write("<script type='text/javascript'>\n")
        html_file.write("var margin = { top: 75, right: 10, bottom: 50, left: 100 },\n")
        html_file.write("  cellSize=12;\n")

        html_file.write("  col_number="+str(intervals)+";\n")
        html_file.write("  row_number="+str(intervals)+";\n")
        html_file.write("  width = cellSize*col_number, // - margin.left - margin.right,\n")
        html_file.write("  height = cellSize*row_number , // - margin.top - margin.bottom,\n")
        html_file.write("  gridSize = Math.floor(width / 24),\n")
        html_file.write("  legendElementWidth = cellSize*2.5,\n")
        html_file.write("  colorBuckets = 11,\n")

        i = 1
        rows_cols = "["
        while i <= intervals:
            if i != intervals:
                rows_cols = rows_cols+str(i)+","
            else:
                rows_cols = rows_cols+str(i)+"]"
            i += 1

        html_file.write("colors_bottom = ['#FFFFFF','#F1EEF6','#E6D3E1','#DBB9CD','#D19EB9','#C684A4','#BB6990','#B14F7C','#A63467','#9B1A53','#91003F'];\n")
        html_file.write("  colors_top = ['#FFFFFF','#ebebfa','#d6d6f5','#c2c2f0','#adadeb','#9999e6','#8585e0','#7070db','#5c5cd6','#4747d1','#3333cc'];\n")
        html_file.write("  colors_diagonal = ['#FFFFFF','#e6ffee','#b3ffcc','#80ffaa','#4dff88','#00ff55','#00e64d','#00cc44','#00b33c','#00802b','#006622'];\n")
        html_file.write("  hcrow = "+rows_cols+", // change to gene name or probe id\n")
        html_file.write("  hccol = "+rows_cols+", // change to gene name or probe id\n")

        i = 1
        x = 0
        y = resolution-1
        frome = ""
        toe = ""
        while i <= intervals:
            if i != intervals:
                frome = frome+"'From "+str(x)+"-"+str(y)+"', "
                toe = toe+"'To "+str(x)+"-"+str(y)+"', "
                x += resolution
                y += resolution
            else:
                frome = frome+"'From "+str(x)+"-"+str(y)+"'"
                toe = toe+"'To "+str(x)+"-"+str(y)+"'"
                x += resolution
                y += resolution
            i += 1

        html_file.write("  rowLabel = ["+frome+"], // change to gene name or probe id\n")
        html_file.write("  colLabel = ["+toe+"]; // change to contrast name\n")
        html_file.write('d3.tsv("tsvs/data_heatmap_'+youtube_id+'.tsv",\n')

        html_file.writelines(base_data_html)

        html_file.write('<div id=video>\n')
        html_file.write('<embed width="420" height="315"src="http://www.youtube.com/v/'+youtube_id+'">\n')
        html_file.write('</div>\n')
        html_file.write('</body>\n')
        html_file.write('</html>')

        html_file.close()
        return
