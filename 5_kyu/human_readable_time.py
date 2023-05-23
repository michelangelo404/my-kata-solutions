#Human readable time

def make_readable(seconds):
    mm, ss = divmod(seconds, 60)
    hh, mm = divmod(mm, 60)
    return str(hh).zfill(2)+':'+str(mm).zfill(2)+':'+str(ss).zfill(2)