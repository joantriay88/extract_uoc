import os


# PATH SETTINGS:
JSON_PATH = "/Users/LearningAnalytics/Dropbox/jsons/inserlab_2015.json"
ABS_PATH = os.path.dirname(os.path.abspath(__file__))
TEXT_FILES_PATH = "dataExtracted/files/"
TSVS_HEATMAP_FILES = "dataExtracted/visual/heatmaps/tsvs/"
HEATMAP_FILES = "dataExtracted/visual/heatmaps/"

# YOUTUBE V3 API KEY
API_KEY = "AIzaSyB1I6cpK4UTwWmkqqiidXncss9Fvmb_CiQ"

# COLORS
HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

# EXCEPTIONS
PATH_JSON_ERROR = "\n"+FAIL+"ERROR: "+OKGREEN+"Path error, check in the file settings.py the variable JSON_PATH, this is the path of your json file that contains the MOOC tracking logs. Now your path is " + str(JSON_PATH) + " , is it correct?"+FAIL+" Aborted loading.\n"
VALIDATION_JSON_ERROR = FAIL+"ERROR: "+OKGREEN+"Your .json file is not validated. The .json file should be something like this:\n"+FAIL+"[\n{........},\n{........},\n{........}\n]\nAborted loading."+OKGREEN+" You can use some scripts from the folder additionalScripts to correct it."
IMPOSSIBLE_CALCULATE_USERNAMES = FAIL+"ERROR: "+OKGREEN+"Is not possible calcualte the different usernames.\n"+FAIL+"Aborted."
IMPOSSIBLE_CALCULATE_VIDEOIDs = FAIL+"ERROR: "+OKGREEN+"Is not possible calcualte the different video ids.\n"+FAIL+"Aborted."
IMPOSSIBLE_CREATE_SYSTEM_OBECTS = FAIL+"ERROR: "+OKGREEN+"Is not possible calcualte the different video ids.\n"+FAIL+"Aborted."

# SUCCESS MESSAGES
LOADING_JSON_FILE = OKBLUE+"SUCCESS:"+OKGREEN+" CORRECT PATH OF .JSON FILE TRACKING LOGS, LOADING..."
LOADED_JSON_FILE = OKBLUE+"SUCCESS:"+OKGREEN+" .JSON FILE TRACKING LOGS LOADED"
USERNAMES_CALCULATED = OKBLUE+"SUCCESS:"+OKGREEN+" USERNAMES CALCULATED"
VIDEO_IDs_CALCULATED = OKBLUE+"SUCCESS:"+OKGREEN+" VIDEO IDs CALCULATED"
SYSTEM_OBJECTS_CREATED = OKBLUE+"SUCCESS:"+OKGREEN+" SYSTEM OBJECTS CREATED"
