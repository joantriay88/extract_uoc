EXTRACT
===================

EXTRACT is a .JSON parser for [tracking logs](http://edx.readthedocs.org/projects/devdata/en/latest/internal_data_formats/tracking_logs.html) from [Open edX](https://open.edx.org/). That parser extract data from the logs and create a new files for every variable that extract. Normally every variable is referred to a an event from  [tracking logs](http://edx.readthedocs.org/projects/devdata/en/latest/internal_data_formats/tracking_logs.html).

----------

How it works?
-------------

First, you have to edit `settings.py` file, there you can find two constant variables called `JSON_PATH` and `API_KEY`.

> - `JSON_PATH`: You have to put the path of your .json file, that file contains all tracking logs that you want parser.
> If you don't know the path of the .json file, you can use `pwd` command to know wich is the path.

> - `API_KEY`: You have to put here your api key from [Youtube Api V3](https://developers.google.com/youtube/v3/getting-started#intro) , in the link you can find the instructions about how to get one key.

Then, when you have modified this two variables, with the command line go with `cd` to the path where you have EXTRACT and execute:
>- `python start.py`


----------

What data parse?
-------------
EXTRACT parse different events, extract different variables and store it in individual files. This files are saved in the folder `dataExtracted/files`.



 - Video files:

> This files contains different variables related with an event from 
> 
> **n_plays_v.txt** : This file contains the number of plays did in video. Is structured in two columns and different rows, the first column is referred to the youtube code, the second column is related with the number of plays and each row represents a video. This file is related with the event [play_video/edx.video.played](http://edx.readthedocs.org/projects/devdata/en/latest/internal_data_formats/tracking_logs.html#play-video-edx-video-played) from edX [tracking logs](http://edx.readthedocs.org/projects/devdata/en/latest/internal_data_formats/tracking_logs.html).
> 
> **n_pauses_v.txt** : This file contains the number of pauses did in a video. Is structured in two columns and different rows, the first column is referred to the youtube code, the second column is related with the number of pauses and each row represents a video. This file is related with the event [pause_video/edx.video.paused](http://edx.readthedocs.org/projects/devdata/en/latest/internal_data_formats/tracking_logs.html#pause-video-edx-video-paused) from edX [tracking logs](http://edx.readthedocs.org/projects/devdata/en/latest/internal_data_formats/tracking_logs.html).
> 
> **n_stops_v.txt** : This file contains number of stops did in a video. Is structured in two columns and different rows, the first column is referred to the youtube code, the second column is related with the number of stops and each row represents a video. This file is related with the event [stop_video/edx.video.stopped](http://edx.readthedocs.org/projects/devdata/en/latest/internal_data_formats/tracking_logs.html#stop-video-edx-video-stopped) from edX [tracking logs](http://edx.readthedocs.org/projects/devdata/en/latest/internal_data_formats/tracking_logs.html).
> 
> **n_seekFor_v.txt** : This file contains the number of seeks forward did in a video. Is structured in two columns and different rows, the first column is referred to the youtube code and the second column is related with the number of seeks forward and each row represents a video. This file is related with the event [seek_video/edx.video.position.changed](http://edx.readthedocs.org/projects/devdata/en/latest/internal_data_formats/tracking_logs.html#seek-video-edx-video-position-changed) from edX [tracking logs](http://edx.readthedocs.org/projects/devdata/en/latest/internal_data_formats/tracking_logs.html).
> 
> **n_seekBack_v.txt** : This file contains the number of seeks backward did in a video. Is structured in two columns and different rows, the first column is referred to the youtube code, the second column is related with the number of seeks backward and each row represents a video. This file is related with the event [seek_video/edx.video.position.changed](http://edx.readthedocs.org/projects/devdata/en/latest/internal_data_formats/tracking_logs.html#seek-video-edx-video-position-changed) from edX [tracking logs](http://edx.readthedocs.org/projects/devdata/en/latest/internal_data_formats/tracking_logs.html).
> 
> **n_speedDown_v.txt** : This file contains the number of speed downs did in a video. Is structured in two columns and different rows, the first column is referred to the youtube code, the second column is related with the number of speed downs and each row represents a video. This file is related with the event [speed_change_video](http://edx.readthedocs.org/projects/devdata/en/latest/internal_data_formats/tracking_logs.html#speed-change-video) from edX [tracking logs](http://edx.readthedocs.org/projects/devdata/en/latest/internal_data_formats/tracking_logs.html).
> 
> **n_speedUp_v.txt** : This file contains the number of speed ups did in a video. Is structured in two columns and different rows, the first column is referred to the youtube code, the second column is related with the number of speed ups and each row represents a video. This file is related with the event [speed_change_video](http://edx.readthedocs.org/projects/devdata/en/latest/internal_data_formats/tracking_logs.html#speed-change-video) from edX [tracking logs](http://edx.readthedocs.org/projects/devdata/en/latest/internal_data_formats/tracking_logs.html).
> 
> **duration_v.txt** : This file contains the different durations in seconds of each video. Is structured in two columns and different rows, the first column is referred to the youtube code, the second column is related with duration in seconds and each row represents a video.

 - Forum files:

> This files contains different variables related with the forum events. 
> 
>  **Threads_Forum.txt**: This file contains the different comment threads in forum created by the students. Every row of this file corresponds to a new thread and it have 6 different columns where we can find different information: Username, CommentID, UnicIDThread, UserRole, Title and Body. This file is related with the event [edx.forum.thread.created](http://edx.readthedocs.org/projects/devdata/en/latest/internal_data_formats/tracking_logs.html#edx-forum-thread-created) from edX [tracking logs](http://edx.readthedocs.org/projects/devdata/en/latest/internal_data_formats/tracking_logs.html).
>  
>  **Responses_Threads_Forum.txt**: This file contains the different responses of the threads. Every row of this file corresponds to a new response in a thread and it have 6 different columns where we can find different information: Username, CommentID, UnicIDThread, UnicIdResponse, UserRole and Body. This file is related with the event [edx.forum.response.created](http://edx.readthedocs.org/projects/devdata/en/latest/internal_data_formats/tracking_logs.html#edx-forum-response-created) from edX [tracking logs](http://edx.readthedocs.org/projects/devdata/en/latest/internal_data_formats/tracking_logs.html).
>  
>  **Comments_Responses_Threads_Forum.txt**: This file contains the different comments of responses of the threads. Every row of this file corresponds to a new comment in a response of thread and it have 6 different columns where we can find different information: Username, CommentID, UnicIdResponse, UnicIdComment, UserRole and Body. This file is related with the event [edx.forum.comment.created](http://edx.readthedocs.org/projects/devdata/en/latest/internal_data_formats/tracking_logs.html#edx-forum-comment-created) from edX [tracking logs](http://edx.readthedocs.org/projects/devdata/en/latest/internal_data_formats/tracking_logs.html).

 - Students files:
 
>This files contains information about the participation and about the interaction during the mooc.
>
> **n_plays_vs.txt** : This file contains a matrix where the rows represents the students and the columns the videos, except the first column that is the usernames. In te matrix, every number is the number of plays that student did in a video.  This file is related with the event [play_video/edx.video.played](http://edx.readthedocs.org/projects/devdata/en/latest/internal_data_formats/tracking_logs.html#play-video-edx-video-played) from edX [tracking logs](http://edx.readthedocs.org/projects/devdata/en/latest/internal_data_formats/tracking_logs.html).
> 
> **n_pauses_vs.txt** : This file contains a matrix where the rows represents the students and the columns the videos, except the first column that is the usernames. In te matrix, every number is the number of pauses that student did in a video. This file is related with the event [pause_video/edx.video.paused](http://edx.readthedocs.org/projects/devdata/en/latest/internal_data_formats/tracking_logs.html#pause-video-edx-video-paused) from edX [tracking logs](http://edx.readthedocs.org/projects/devdata/en/latest/internal_data_formats/tracking_logs.html).
> 
> **n_stops_vs.txt** : This file contains a matrix where the rows represents the students and the columns the videos, except the first column that is the usernames. In te matrix, every number is the number of stops that student did in a video.  This file is related with the event [stop_video/edx.video.stopped](http://edx.readthedocs.org/projects/devdata/en/latest/internal_data_formats/tracking_logs.html#stop-video-edx-video-stopped) from edX [tracking logs](http://edx.readthedocs.org/projects/devdata/en/latest/internal_data_formats/tracking_logs.html).
> 
> **n_seekFor_vs.txt** : This file contains a matrix where the rows represents the students and the columns the videos, except the first column that is the usernames. In te matrix, every number is the number of seek forwards that student did in a video.  This file is related with the event [seek_video/edx.video.position.changed](http://edx.readthedocs.org/projects/devdata/en/latest/internal_data_formats/tracking_logs.html#seek-video-edx-video-position-changed) from edX [tracking logs](http://edx.readthedocs.org/projects/devdata/en/latest/internal_data_formats/tracking_logs.html).
> 
> **n_seekBack_vs.txt** : This file contains a matrix where the rows represents the students and the columns the videos, except the first column that is the usernames. In te matrix, every number is the number of seek backwards that student did in a video. This file is related with the event [seek_video/edx.video.position.changed](http://edx.readthedocs.org/projects/devdata/en/latest/internal_data_formats/tracking_logs.html#seek-video-edx-video-position-changed) from edX [tracking logs](http://edx.readthedocs.org/projects/devdata/en/latest/internal_data_formats/tracking_logs.html).
> 
>**quota_viewed_vs.txt**: This file contains a matrix where the rows represents the students and the columns the videos, except the first column that is the usernames. In te matrix, every number is the quota of video watched, e.g if the student watched the 50% of a vídeo the number is 0.5 or if the student watched the video two times the number is 2.0.
>
> **t_viewed_vs.txt**: This file contains a matrix where the rows represents the students and the columns the videos, except the first column that is the usernames. In te matrix, every number is the time in seconds dedicated to a video.