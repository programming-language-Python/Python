# Переданный массив преобразуется в множество
states_needed = set( [ "mt", "wa", "or", "id", "nv", "ut", "са", "az"] ) 
# список станций
stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "са"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])
# нам понадобится структура данных для хранения итогового набора станций:
final_stations = set()
# Вы перебираете все станции и выбираете
# ту, которая обслуживает больше всего штатов,
# не входящих в текущее покрытие.
# Будем называть ее best_station:
while states_needed:
    best_station = None
    states_covered = set()
    for station, states_for_station in stations.items():
        # Новый синтаксис! Эта операция называется "пересечением множеств"
        covered = states_needed & states_for_station
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
    print (best_station)
    states_needed -= states_covered
    final_stations.add(best_station)
print (final_stations)