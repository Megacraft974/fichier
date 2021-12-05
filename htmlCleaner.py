from tkinter import Tk
import re,subprocess

def getClip():
    fen = Tk()
    clip = fen.clipboard_get()
    fen.destroy()
    return clip
    
def copy2clip(txt):
    cmd='echo '+txt.strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

text = input("-> ")
if text == "":
    text = getClip()
text = cleanhtml(text)
copy2clip(text)

print("Done!")
