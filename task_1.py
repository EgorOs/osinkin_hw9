#!/usr/bin/env python3

import os
import pwd
import subprocess

pids = [pid for pid in os.listdir('/proc') if pid.isdigit()]
user_id = os.getuid()
# for pid in pids:print(pid)
# print(user_id)
# print(pwd.getpwnam('egor').pw_uid)
# for pid in pids:
#     f = open('/proc/'+str(pid)+'/status', 'r')
#     ctr = 0
#     for line in f:
#         if 'VmSize' in line:
#             size = int(line.split('\t')[1].strip(' ').replace(' kB', ''))
#             print(size, ctr)
#             print('')
#             break
#         ctr += 1

#     f.close()

def process_count(username: str) -> int:
    # validate username
    try:
        pwd.getpwnam(username)
    except KeyError as e:
        raise KeyError("{} user doesn't exist.".format(username)).with_traceback(e.__traceback__)

    ps = subprocess.Popen('ps -u ' + str(username), shell=True, stdout=subprocess.PIPE)
    n_proc = 0
    # pass 1st line, because it is header
    for i in ps.stdout.readlines()[1::]:
        n_proc += 1
        print(i)
    ps.terminate()
    return n_proc


def total_memory_usage(root_pid: int) -> int:
    # ps -ejH
    def get_chld_pids(parent: int, chld_pids=set()) -> list:
        # print('opened' , parent)
        ps = subprocess.Popen('pgrep -P ' + str(parent), shell=True, stdout=subprocess.PIPE)
        current_chld_pids = {int(pid) for pid in ps.stdout.readlines()}
        chld_pids.update(current_chld_pids)
        ps.terminate()
        if len(current_chld_pids) == 0:# or parent in chld_pids:
            # print(parent,' ---')
            # chld_pids += ['t']
            return []
        else:
            for pid in current_chld_pids:
                # chld_pids += ['add'+str(pid)]
                new = get_chld_pids(pid)
                if new:
                    chld_pids.update(new)
        # print(current_chld_pids)
        return chld_pids

    pids_in_tree = [root_pid] + sorted(list(get_chld_pids(root_pid)))
    print(pids_in_tree)
    mem_usg = 0
    for pid in pids_in_tree:
        try:
            f = open('/proc/'+str(pid)+'/status', 'r')
            for line in f:
                if 'VmSize' in line:
                    mem_usg += int(line.split('\t')[1].strip(' ').replace(' kB', ''))
        except FileNotFoundError:
            # if subprocess was closed and removed from /proc
            pass

    return  mem_usg

print(total_memory_usage(5248))

