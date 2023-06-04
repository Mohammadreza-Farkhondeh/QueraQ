
# Airplane statuses
F, T,  L, O = 1, 2, 3 , 4   # 'IN-free', 'IN-takeOff', 'IN-landing', 'OUT'
# Runways statuses
Fr, Oc = 0, 1  # 'Free', 'Occupied'


class Airplane:
    def __init__(self, ID):
        self.ID = ID
        self.status = F
        self.location = 0   # 0, 1-k, 1-k, -1

    def take_off(self):
        if self.status == F:
            for runway in runways:
                if runway.status == Fr:
                    runway.status = Oc
                    self.status = T
                    runway.airplane = self.ID
                    break
            else:
                print('NO FREE BOUND')
        elif self.status == L:
            print('YOU ARE LANDING NOW')
        elif self.status == T:
            print('YOU ARE TAKING OFF')
        else:
            print('YOU ARE NOT HERE')

    def land(self):
        if self.status == F:
            print('YOU ARE HERE')
        elif self.status == L:
            print('YOU ARE LANDING NOW')
        elif self.status == T:
            print('YOU ARE TAKING OFF')
        elif self.status == O:
            for runway in reversed(runways):
                if runway.status == Fr:
                    runway.status = Oc
                    self.status = L
                    runway.airplane = self.ID
                    break
            else:
                print('NO FREE BOUND')


    def plane_status(self):
        print(self.status)


class Airport:
    def __init__(self, n, k):
        self.Airplane_number = n
        self.runway_number = k


class Runway(Airport):
    def __init__(self, number, status):
        self.number = number
        self.status = status
        self.airplane = 0000000000

    def BAND_status(self):
        if self.airplane == 0000000000:
            print('FREE')
        else:
            print(self.airplane)
n, k = map(int, input().split())
runways = [Runway(str(i+1), Fr) for i in range(k)]
airplanes = []
for i in range(n):
    the_ID = input()
    airplanes.append(Airplane(the_ID))


q = int(input())

for i in range(q):
    command, ID = input().split(' ')
    if command == 'BAND-STATUS':
        for rw in runways:
            if rw.number == ID:
                rw.BAND_status()
                break
    else:
        for airplane in airplanes:
            if airplane.ID == ID:
                if command == 'TAKE-OFF':
                    airplane.take_off()
                elif command == 'LANDING':
                        airplane.land()
                elif command == 'PLANE-STATUS':
                        airplane.plane_status()
                break
        else:
            new_airplane = Airplane(ID)
            new_airplane.status, new_airplane.location = 4, -1
            if command == 'TAKE-OFF':
                new_airplane.take_off()
            elif command == 'LANDING':
                    new_airplane.land()
            elif command == 'PLANE-STATUS':
                    new_airplane.plane_status()
            airplanes.append(new_airplane)