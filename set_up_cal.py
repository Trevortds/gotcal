# coding: utf-8
from quickstart import *
credentials = get_credentials()
http = credentials.authorize(httplib2.Http())
service = discovery.build('calendar', 'v3', http=http)
episodes = {
1:range(1,11),
2:range(1,11),
3:range(1,11),
4:range(1,11),
5:range(1,11),
6:range(1,11),
7:range(1,8)
}
for season in episodes:
    for episode in episodes[season]:
        batch = {
            "creator": {
                "displayName":"gotbot",
                "email":"trevortds@gmail.com",
            },
        }
        
service.events().insert(calendarId="gotcal", body=batch).execute()
service.calendarList().execute
service.calendarList().execute()
service.calendarList()
service.calendarList().get()
service.calendarList().list()
service.calendarList().list().execute()
service.events().insert(calendarId="tn4081lbv9si0gvke47einvlc4@group.calendar.google.com", body=batch).execute()
gotcalid = "tn4081lbv9si0gvke47einvlc4@group.calendar.google.com"
for season in episodes:
    for episode in episodes[season]:
        batch = {
            "creator": {
                "displayName":"gotbot",
                "email":"trevortds@gmail.com",
            },
            "summary": "Game of Thrones {}.{}".format(season, episode),
            "start" {
                "date": epdate.strftime('%Y-%m-%d')
            },
            "description": "Game of Thrones season {} episode {}".format(season, episode),
            "end": {
                "date": epdate.strftime('%Y-%m-%d')
            }
            "reminders" : { "useDefault":True}
        }

        
for season in episodes:
    for episode in episodes[season]:
        batch = {
            "creator": {
                "displayName":"gotbot",
                "email":"trevortds@gmail.com",
            },
            "summary": "Game of Thrones {}.{}".format(season, episode),
            "start": {
                "date": epdate.strftime('%Y-%m-%d')
            },
            "description": "Game of Thrones season {} episode {}".format(season, episode),
            "end": {
                "date": epdate.strftime('%Y-%m-%d')
            }
            "reminders" : { "useDefault":True}
        }

        
for season in episodes:
    for episode in episodes[season]:
        batch = {
            "creator": {
                "displayName":"gotbot",
                "email":"trevortds@gmail.com",
            },
            "summary": "Game of Thrones {}.{}".format(season, episode),
            "start": {
                "date": epdate.strftime('%Y-%m-%d')
            },
            "description": "Game of Thrones season {} episode {}".format(season, episode),
            "end": {
                "date": epdate.strftime('%Y-%m-%d')
            },
            "reminders" : { "useDefault":True}
        }

        
for season in episodes:
    for episode in episodes[season]:
        batch = {
            "creator": {
                "displayName":"gotbot",
                "email":"trevortds@gmail.com",
            },
            "summary": "Game of Thrones {}.{}".format(season, episode),
            "start": {
                "date": epdate.strftime('%Y-%m-%d')
            },
            "description": "Game of Thrones season {} episode {}".format(season, episode),
            "end": {
                "date": epdate.strftime('%Y-%m-%d')
            },
            "reminders" : { "useDefault":True}
        }

       
epdate = datetime.date(year=2018, month="April", day=22)
epdate = datetime.date(year=2018, month=4, day=22)
epdate
for season in episodes:
    for episode in episodes[season]:
        batch = {
            "creator": {
                "displayName":"gotbot",
                "email":"trevortds@gmail.com",
            },
            "summary": "Game of Thrones {}.{}".format(season, episode),
            "start": {
                "date": epdate.strftime('%Y-%m-%d')
            },
            "description": "Game of Thrones season {} episode {}".format(season, episode),
            "end": {
                "date": epdate.strftime('%Y-%m-%d')
            },
            "reminders" : { "useDefault":True}
        }

       
service.events().insert(calendarId="tn4081lbv9si0gvke47einvlc4@group.calendar.google.com", body=batch).execute()
for season in episodes:
    for episode in episodes[season]:
        batch = {
            "creator": {
                "displayName":"gotbot",
                "email":"trevortds@gmail.com",
            },
            "summary": "Game of Thrones {}.{}".format(season, episode),
            "start": {
                "date": epdate.strftime('%Y-%m-%d')
            },
            "description": "Game of Thrones season {} episode {}".format(season, episode),
            "end": {
                "date": epdate.strftime('%Y-%m-%d')
            },
            "reminders" : { "useDefault":True}
        }
        service.events().insert(calendarid=gotcalid, body=batch).execute()
        epdate = epdate + datetime.timedelta(weeks=1)
        
       
for season in episodes:
    for episode in episodes[season]:
        batch = {
            "creator": {
                "displayName":"gotbot",
                "email":"trevortds@gmail.com",
            },
            "summary": "Game of Thrones {}.{}".format(season, episode),
            "start": {
                "date": epdate.strftime('%Y-%m-%d')
            },
            "description": "Game of Thrones season {} episode {}".format(season, episode),
            "end": {
                "date": epdate.strftime('%Y-%m-%d')
            },
            "reminders" : { "useDefault":True}
        }
        service.events().insert(calendarId=gotcalid, body=batch).execute()
        epdate = epdate + datetime.timedelta(weeks=1)
        
       
get_ipython().magic('save set_up_cal.py')
get_ipython().magic('save set_up_cal.py ~0/')
