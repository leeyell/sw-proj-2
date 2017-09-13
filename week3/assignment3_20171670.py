import pickle

dbfilename = 'test3_4.dat'

def readScoreDB():
    try:
        fH = open(dbfilename, 'rb')
    except FileNotFoundError as e:
        print("New DB: ", dbfilename)
        return []

    scdb = []
    try:
        scdb = pickle.load(fH)
    except:
        print("Empty DB: ", dbfilename)
    else:
        print("Open DB: ", dbfilename)
    fH.close()
    return scdb


# write the data into person db
def writeScoreDB(scdb):
    fH = open(dbfilename, 'wb')
    pickle.dump(scdb, fH)
    fH.close()

#원래 있던 데이터의 나이, 점수를 integer로 변경하는 함수.
def toInt(scdb):
    for dic in scdb:
        dic['Age'] = int(dic['Age'])
        dic['Score'] = int(dic['Age'])

def doScoreDB(scdb):
    while (True):
        inputstr = (input("Score DB > "))
        if inputstr == "": continue
        parse = inputstr.split(" ")
        if parse[0] == 'add':
            try:
                record = {'Age': int(parse[2]), 'Name': parse[1], 'Score': int(parse[3])}   #원래 있던 데이터와 순서룰 맞추기 위해 나이 이름 점수 순으로 바꿈.
                scdb += [record]
            except:
                print("add 이름 나이 점수 순으로 입력해주세요.")
        elif parse[0] == 'del':
            try:
                for p in scdb:                   #왜 지워도 꼭 하나가 안 지워지고 남지?????? 코드 리뷰를 위해 남겨놓도록 하자..
                    if p['Name'] == parse[1]:
                        scdb.remove(p)
            except:
                print("del 이름 순으로 입력해주세요.")
        elif parse[0] == 'show':
            sortKey = 'Name' if len(parse) == 1 else parse[1]
            showScoreDB(scdb, sortKey)
        elif parse[0] == 'quit':
            break

        elif parse[0] == 'find':           #find Name
            for q in scdb:
                if q['Name'] == parse[1]:
                    print(q)
        elif parse[0] == 'inc':            #inc Name amount
            try:
                for k in scdb:
                    if k['Name'] == parse[1]:
                        k['Score'] += int(parse[2])
            except:
                print("inc 이름 추가점수 순으로 입력해주세요.")

        else:
            print("Invalid command: " + parse[0])


def showScoreDB(scdb, keyname):
    for p in sorted(scdb, key=lambda person: person[keyname]):
        print(p, end=' ')
        print()


scoredb = readScoreDB()
toInt(scoredb)
doScoreDB(scoredb)
writeScoreDB(scoredb)
