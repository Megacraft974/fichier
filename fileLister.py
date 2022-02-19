import re

def parseName(f):
    f = re.split(r'\.(mkv|mp4|torrent)$', f)[0]#.mp4 / .mkv / .torrent
    f = f.replace(r'[\.,-]', ' ')#. / ,
    f = re.sub(r'/.*', '', f)#/.....
    f = re.sub(r'\[.*?\]+', ' ', f)#[.....]
    f = re.sub(r'\(.*?\)+', ' ', f)#(.....)
    f = re.split(r'[^0-9]-( |)[0-9]+', f)[0]#... - 12
    f = re.split(r'[^0-9]-( |)OVA+', f)[0]#... - OVA
    f = re.split(r'(S|Season|Seasons)( |)[0-9]+', f)[0]#S1 / S01
    f = re.split(r'[0-9](|st|nd|rd|th)( |)(S|Season|Seasons)', f)[0]#1st / 2nd / ... Season
    f = re.split(r'[0-9]+(-|~)[0-9]+', f)[0]#1 - 12
    f = re.split(r'([\-\~\&]( |))$', f)[0]#"- " / "-" / "&"
    f = re.sub(r'  +?', '', f)#"  "
    f = re.sub(r'(^ | $)', '', f)#" ..." / "... "
    return f

if __name__ == "__main__":
    # Was used to keep track of the downloaded torrents, see the animeManager project for updated version
    from os import listdir
    #from os.path import isfile, join
    from animeManager import Manager
    # m = Manager(remote=True)
    # m.regroupFiles()

    path = "E:/Animes/"
    files = []
    ignoreList = ["+++.txt","AutoNameList.txt","Torrents"]
    for f in listdir(path):
        if f not in ignoreList:
            files.append(parseName(f))

    files.sort()
    # print(files)

    dbName = "AutoNameList.txt"
    with open(path+dbName,"r") as f:
        data = f.readlines()
        
    db = [n.split("\n")[0] for n in data]
    db += files
    db = list(dict.fromkeys(db))
    db.sort()

    # print(db)

    with open(path+dbName,'w') as file:
        for f in db:
            file.write(f+'\n')

