import os


def list_directories(s):
    def dir_list(d, par_stop):
        files = os.listdir(d)
        for f in files:
            current_dir = os.path.join(d, f)
            if os.path.isdir(current_dir):
                print("\t" * par_stop + "Directory " + f+":")
                par_stop += 1
                dir_list(current_dir, par_stop)
                par_stop -= 1
            else:
                print("\t" * par_stop + f)

    tab_stop = 0
    if os.path.exists(s):
        print("Directory listing of " + s + ":")
        dir_list(s, tab_stop)
    else:
        print(s + " does not exist.")


list_directories('./../')
