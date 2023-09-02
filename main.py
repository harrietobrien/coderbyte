import pandas as pd
import json
from subprocess import call
pd.options.display.max_colwidth = 300

json_objs = json.load(open('challenges.json'))
df = pd.read_json(open('challenges.json'))

difficulties = ['solutions', 'medium', 'hard']

def create_directories():
    for i in difficulties:
        cmd = 'mkdir {difficulty}'.format(difficulty=i)
        call([cmd, i], shell=True)

def organizeDifficulties():
    return {i.capitalize():df.loc[df['difficulty'] == i.capitalize()]
            for i in difficulties}

diffDict = organizeDifficulties()

def createPyFiles(df):
    for lvl in difficulties:
        titles = list(difficulties[lvl]['title'])
        for title in titles:
            _title = title.lower().replace(" ", "_")
            title_fn = f'{_title}.py'
            cmd2 = 'touch ./{lvl}/{fn}'.format(lvl=lvl.lower(), fn=title_fn)
            call([cmd2, title_fn, lvl.lower()], shell=True)
            curr_challenge_df = df.loc[df["title"] == title]
            description = curr_challenge_df['description']
            d = '#{descript}'.format(descript=description.to_string())
            cmd3 = 'echo {descr} | cat >> ./{lvl}/{fn}'.format(descr=d, lvl=lvl.lower(), fn=title_fn)
            call([cmd3, d, lvl.lower(), title_fn], shell=True)
        call(['cd ..'], shell=True)
