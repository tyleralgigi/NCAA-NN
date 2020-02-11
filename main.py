#files
import schedule
import test
import ATS
import editGameList
import getGames
import getData
#libs
import pathlib
import time

if __name__ == '__main__':
    path = pathlib.Path(__file__).parent.absolute()
    getData.getData()
    print('1/6')
    time.sleep(2)
    getGames.start(path)
    print('2/6')
    time.sleep(2)
    editGameList.editList()
    print('3/6')
    time.sleep(2)
    ATS.ATS()
    print('4/6')
    time.sleep(2)
    test.func()
    print('5/6')
    time.sleep(2)
    schedule.scheduleStart(path)
    print('Data Collection Complete')
