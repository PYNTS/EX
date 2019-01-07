#PYNTS

people = 30
cars = 40
trucks = 15

if cars > people:                                 #Jezeli cars wieksze od people
    print("Powinnismy jechac samochodami")
elif cars < people:                               #Jezeli cars mniejsze od people
    print("Nie powinnismy jechac samochodami.")
else:                                             #W przeciwnym razie
    print("Nie mozemy sie zdecydowac")

if trucks > cars:                                 #Jezeli trucks wieksze od cars
    print("Jest zbyt duzo ciezarowke.")
elif trucks < cars:                               #Jezeli Trucks mniejsze od cars
    print("Moze powinnismy wziac ciezarowki.")
else:                                             #W przeciwnym razie
    print("Nadal nie mozemy sie zdecydowac")

if people > trucks:                               #Jezeli people wieksze od trucks
    print("W porzadku, po prostu wezmy ciezarowki.")
else:                                             #W przeciwnym razie
    print("Dobra, w takim razie zostajemy w domu.")

#End of Script
