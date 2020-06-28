import subprocess

revision = subprocess.check_output(["git", "describe", "--tags", "--dirty"]).strip().decode()

info = revision.split('-')
if len(info) == 1:
    version = info[0]
else:
    version = info[0] + "+" + "-".join(info[1:])
print('-DVERSION=\'"%s"\'' % version)
