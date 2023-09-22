#10/24/22

from tqdm import tqdm
from time import sleep
import sys
import psutil

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'



#Change Position of bars
#Add space inbetween bars
#alive progress https://www.reddit.com/r/Python/comments/kqbo85/a_new_kind_of_progress_bar_for_python/
#FPS

with tqdm(colour="red", total=20, desc=f'{bcolors.FAIL}ram used%{bcolors.ENDC}', position=0,ascii=' |') as rambar, \
        tqdm(colour="yellow", total=20, desc=f'{bcolors.WARNING}ram avlb%{bcolors.ENDC}', position=1,ascii=' |') as rambar2, \
          tqdm(colour="green", total=100, desc=f'{bcolors.OKGREEN}cpu     %{bcolors.ENDC}', position=2, ascii=' |') as cpubar, \
          tqdm(colour="cyan", total =1000, desc=f'{bcolors.OKCYAN}MBS UP  %{bcolors.ENDC}', position=3,ascii=' |') as net1bar, \
          tqdm(colour="magenta", total=1000, desc=f'{bcolors.HEADER}MBS DOWN%{bcolors.ENDC}', position=4,ascii=' |') as net2bar, \
          tqdm(colour="blue", total=100, desc=f'{bcolors.OKBLUE}Disk Use%{bcolors.ENDC}', position=5,ascii=' |') as diskbar1:

    while True:
    
        rambar.n=round(psutil.virtual_memory().used/1000000000,2)
        rambar2.n=round(psutil.virtual_memory().available/1000000000,2)
        cpubar.n=psutil.cpu_percent()
        net1bar.n=round(((psutil.net_io_counters().bytes_sent)/10000000),2)
        net2bar.n=round(((psutil.net_io_counters().bytes_recv)/10000000),2)
        diskbar1.n=psutil.disk_usage('/').percent
        
        rambar.refresh()
        rambar2.refresh()
        cpubar.refresh()
        net1bar.refresh()
        net2bar.refresh()
        diskbar1.refresh()
        #print('memory used:', , 'GB')
        #print('memory available:', psutil.virtual_memory()[1]/1000000000, 'GB')

        sleep(0.5)
        

