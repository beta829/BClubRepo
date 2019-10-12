

# some spaghetti code to get the name of the current user, so it can be imbedded int the blend file, to display the users name.

import bpy
bpy.data.objects['Text'].data.body = 'Welcome To the\nClub Repo,\n<uname>!'

def get_name():
    with open('../.git/config') as f:
        for l in f.readlines():
            if 'url' in l:
                return l.split('/')[3]
        import getpass
        return getpass.getuser()

bpy.data.objects['Text'].data.body = 'Welcome To the\nClub Repo,\n%s!'%get_name()

def set_name():
    bpy.data.objects['Text'].data.body = 'Welcome To the\nClub Repo,\n%s!'%get_name()
print(get_name())
