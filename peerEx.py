from distances import *
#nodes have coordinate position and velocity (m/sec)
#for peer 1: 
xPos = 0
yPos = 0
xVel = 2
yVel = 0

#list other peers for now -> will get this info from network
peer2 = {
	"name": "peer2",
	"xPos": 5,
	"yPos": 0,
	"xVel": 0,
	"yVel": 0
}

peer3 = {
	"name": "peer3",
	"xPos": 3,
	"yPos": 3,
	"xVel": 1,
	"yVel": -1
}

#each peer knows about other peers for now (y'all can change that)
peers = [
	{"name": "peer2", "dist": -1, "timeInContact": 0, "daysSinceLastContact": -1.0},
	{"name": "peer3", "dist": -1, "timeInContact": 0, "daysSinceLastContact": -1.0}
]

# print(calcDist(xPos, yPos, B["xPos"], B["yPos"]))
# xPos, yPos = updatePos(xPos, yPos, xVel, yVel, 1)
# print(f"{xPos} {yPos}")

time = 1 #in sec
increment = time/86400 #used to increment days since last contact -> 86400 = #seconds in a day

#while true:
for t in range(10): #runtime, for debugging I'm capping it at 10 sec
	for p in peers:
		#----get info from peer----# 
		#will be done using network
		if p["name"] == "peer2":
			n = peer2
		else: n = peer3

		#calc distance from peer
		dist = calcDist(xPos, yPos, n["xPos"], n["yPos"])
		
		#check if <=2m & update records:
		if dist <= 2:
			p["timeInContact"] += time
			p["daysSinceLastContact"] = 0.0

			print(f"You were {dist} away from {p} at time t{t}")
			print(f"xPos = {xPos}, yPos = {yPos}")

		else:
			#if there's already been contact, keep track oh how long its been, if not, no need
			if p["daysSinceLastContact"] != -1:
				p["daysSinceLastContact"] += increment
			print(p)

		#would expect peers to update by themselves, but for now:
		n["xPos"], n["yPos"] = updatePos(n["xPos"], n["yPos"], n["xVel"], n["yVel"], time)
	#update peer1
	xPos, yPos = updatePos(xPos, yPos, xVel, yVel, time)
	

	
