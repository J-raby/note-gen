import os
import sys
import shutil
import argparse

TEMPLATE_PATH = './templates'
NOTES_PATH = './notes'
templates_map = {}

parser = argparse.ArgumentParser(
    prog='NoteTakingCLIApp',
    description='App for generating notes from template for quick and easy access from the terminal',
    epilog='Made by jrpp198'
)

parser.add_argument('-n', dest='fileName', metavar='str', type=str, nargs='?', required=True,help="Name for the new note")
parser.add_argument('-t', dest='noteType', metavar='str', type=str, nargs='?', default='diaria',help="Type of note")
args = parser.parse_args()


if not os.path.exists(NOTES_PATH):
    os.mkdir(NOTES_PATH)

for files in os.listdir(TEMPLATE_PATH):
    full_file_path = os.path.join(TEMPLATE_PATH,files)
    if os.path.isfile(full_file_path):
        file_name = files.split(".")[0]
        templates_map[file_name] = full_file_path

def create_note(name: str, template_type:str):
    if(templates_map[template_type]):
        shutil.copyfile(f"{templates_map[template_type]}", f"{NOTES_PATH}/{name}.md")


create_note(args.fileName, args.noteType)