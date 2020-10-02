
class Column:
    def __init__(self, floorAmount, elevatorAmount):
        print('Column : ', floorAmount, 'Floors and ', elevatorAmount, 'Elevators')
        self.floorAmount = floorAmount
        self.elevatorAmount = elevatorAmount
        self.elevatorList = []
        self.callButtonList = []
        self.floorRequestButtonList = []
    
        
        print('ELEVATOR LIST :')
        i = 0
        while i < self.elevatorAmount:
            elevator = Elevator('Elevator {}'.format(i + 1))
            self.elevatorList.append(elevator)
            print(self.elevatorList[i].id)
            i += 1
        
        print('')
        print('FLOOR REQUEST BUTTON LIST :')
        for i in range(10):
            floorRequestButton = FloorRequestButton(i + 1, self.floorAmount)
            self.floorRequestButtonList.append(floorRequestButton)
            print('FloorRequestButton', self.floorRequestButtonList[i].id)

        print('')
        print('CALL BUTTON LIST :')
        for i in range(self.floorAmount):
            if i == 0:
                callButton = CallButton (i + 1, 'off', 'up')
                self.callButtonList.append(callButton)
                print('CallButton up {}'.format(self.callButtonList[i].id))
            
            elif i == 9:
                callButton = CallButton(i + 1, 'down', 'off')
                self.callButtonList.append(callButton)
                print('CallButton Down {}'.format(self.callButtonList[i].id))

            else:
                callButton = CallButton(i + 1, 'down', 'up')
                self.callButtonList.append(callButton)
                print('CallButton Down|Up {}'.format(self.callButtonList[i].id))


    def requestElevator(self, floor, direction):
        #print('Request Elevator Function')
        
        self.bestElevator = self.findBestElevator(floor, direction)
        print('Best Elevator is Elevator {}'.format(self.bestElevator.id))
        print('Elevator {} Requested on Floor {}'.format(self.bestElevator.id, floor))

        self.bestElevator.requestList.append(floor)
        #print(self.bestElevator.requestList)

        self.bestElevator.moveElevator(floor)
        #print(self.bestElevator.moveElevator)
        
        return self.bestElevator


    def findBestElevator(self, floor, direction):
        print('Find Best Elevator')
        #i = 0
        bestCase = None
        for i in range(len(self.elevatorList)):
            if floor == self.elevatorList[i].position and self.elevatorList[i].direction == 'idle':
                bestCase = self.elevatorList[i]
            elif direction == 'up' and (self.elevatorList[i].direction == 'up' or self.elevatorList[i].direction == 'idle') and self.elevatorList[i].position <= floor:
                bestCase = self.elevatorList[i]
            elif direction == 'down' and (self.elevatorList[i].direction == 'down' or self.elevatorList[i].direction == 'idle') and self.elevatorList[i].position <= floor:
                bestCase = self.elevatorList[i]

        minDistance = 999
        bestDistance = 11
        #i = 0
        bestIdle = None
        for i in range(len(self.elevatorList)):
            distance = abs(self.elevatorList[i].position - floor)
            if self.elevatorList[i].direction == 'idle' and bestDistance >= distance:
                minDistance = distance
                bestIdle = self.elevatorList[i]
            

        if bestCase is not None:
            return bestCase
        else: 
            return bestIdle
            
       
    def requestFloor(self, elevator, floor):
        print('Request Floor :', floor)
        elevator.requestList.append(floor)
        elevator.moveElevator(floor)
        

class Elevator:
    def __init__(self, _id):
        #print('Elevator : ')
        self.id = _id
        self.status = 'idle'
        self.position = 1
        self.direction = 'idle'
        self.floor = None
        self.doors = 'closed'
        self.requestList = []


    def moveElevator(self, position):
        #print('Move Elevator 2')
        #print(previousPosition)
        previousPosition = self.position
        elevatorStatus = self.status
        elevatorDirection = self.direction
        
        
        while len(self.requestList) != 0:
            if self.position > self.requestList[0]:
                print('Elevator', self.id, 'is moving down ... currently at Floor', self.position)
                elevatorStatus = 'moving'
                elevatorDirection = 'down'
                self.status = elevatorStatus
                self.direction = elevatorDirection
                self.position -= 1

            elif self.position < self.requestList[0]:
                print('Elevator', self.id, 'is moving up ... currently at Floor', self.position)
                elevatorStatus = 'moving'
                elevatorDirection = 'up'
                self.status = elevatorStatus
                self.direction = elevatorDirection
                self.position += 1

            elif self.position == self.requestList[0]:
                elevatorStatus = 'idle'
                elevatorDirection = 'idle'
                print('Elevator', self.id, 'arrived at Floor', self.position)
                del self.requestList[0]

                return self.status, self.direction

            if previousPosition is not self.position:
                previousPosition = self.position


class CallButton:
    def __init__(self, _id, floor, direction):
        #print('Call Button')
        self.id = _id
        self.direction = direction
        self.floor = floor

class FloorRequestButton:
    def __init__(self, _id, floorAmount):
        #print('Floor Request Button')
        self.id = _id
        self.floorAmount = floorAmount


#    !!!!!   SCENARIO RESTANT À FAIRE FONCTIONNER     !!!!!    #
######################### TEST ZONE #########################
column = Column(10, 2)
if __name__ == "__main__":
    
    def scenario1():
        
        print('\n -----------SCENARIO 1-----------')
        column.elevatorList[0].id = "A"
        column.elevatorList[0].position = 2
        column.elevatorList[0].direction = 'idle'
        column.elevatorList[0].status = 'idle'
        column.elevatorList[0].floor = 3
        column.elevatorList[1].id = "B"
        column.elevatorList[1].position = 6
        column.elevatorList[1].direction = 'idle'
        column.elevatorList[1].status = 'idle'
        column.elevatorList[1].floor = 3

        elevator = column.requestElevator(3, 'up')
        column.requestFloor(elevator, 7)


    def scenario2():
        
        print('\n -----------SCENARIO 2-----------')
        column.elevatorList[0].id = "A"
        column.elevatorList[0].position = 10
        column.elevatorList[0].direction = 'idle'
        column.elevatorList[0].status = 'idle'
        column.elevatorList[0].floor = 1
        column.elevatorList[1].id = "B"
        column.elevatorList[1].position = 3
        column.elevatorList[1].direction = 'idle'
        column.elevatorList[1].status = 'idle'
        column.elevatorList[1].floor = 1

        elevator = column.requestElevator(1, 'up')
        column.requestFloor(elevator, 6)

        elevator = column.requestElevator(3, 'up')
        column.requestFloor(elevator, 5)

        elevator = column.requestElevator(9, 'down')
        column.requestFloor(elevator, 2)


    def scenario3():   
        
        print('\n -----------SCENARIO 3-----------')
        column.elevatorList[0].id = "A";
        column.elevatorList[0].position = 10;
        column.elevatorList[0].direction = 'idle';
        column.elevatorList[0].status = 'idle';
        column.elevatorList[0].floor = 3;
        column.elevatorList[1].id = "B";
        column.elevatorList[1].position = 3;
        column.elevatorList[1].requestList = [6];
        column.elevatorList[1].direction = 'up';
        column.elevatorList[1].status = 'moving';
        column.elevatorList[1].floor = 6;
        
        elevator = column.requestElevator(3, 'down')
        column.requestFloor(elevator, 2)

        column.elevatorList[0].moveElevator(6)
        elevator = column.requestElevator(10, 'down')
        column.requestFloor(elevator, 3)


scenario1()
scenario2()
scenario3()    