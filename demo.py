from pyMaze import maze,COLOR,agent,textLabel
m=maze()
m.CreateMaze(loopPercent=100)
a=agent(m,footprints=True,filled=True)
b=agent(m,5,5,footprints=True,filled=True,color='red')
# c=agent(m,4,1,footprints=True,filled=True,color='green',shape='arrow')
m.enableArrowKey(a)
#path2=[(5,5),(5,3),(4,3),(3,3),(4,4),(3,4)]
#path3='WWNNES'
l1=textLabel(m,'Total Cells',m.rows*m.cols)
# trace path
#m.tracePath({a:m.path},delay=100) 
#m.tracePath({b:path2},delay=100,showMarked=True)
#m.tracePath({c:path3},delay=100,showMarked=True)
m.run()