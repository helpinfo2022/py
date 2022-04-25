

def test_calculateNumOfCars():
    my_array = [['2', '2020-01-01T00:00:00.000Z', 'ENTRANCE'], ['2', '2020-01-01T05:00:00.000Z', 'EXIT'],['1', '2020-01-01T01:00:00.000Z', 'ENTRANCE'], ['1', '2020-01-01T05:00:00.000Z', 'EXIT']]

    result=0
    for my_exit in my_array:
        if my_exit[2]=="EXIT":

            check_time_exit = list(map(int, my_exit[1][11:-5].split(":")))
            sum_seconds_exit = (check_time_exit[0] * 3600) + (check_time_exit[1] * 60) + check_time_exit[2]

            id_car_exit = my_exit[0]

            for my_entrance in my_array:
                if my_entrance[0] == id_car_exit:

                    check_time_entrance = list(map(int, my_entrance[1][11:-5].split(":")))
                    sum_seconds_entrance = (check_time_entrance[0] * 3600) + (check_time_entrance[1] * 60) + check_time_entrance[2]

                    count_hours = sum_seconds_exit - sum_seconds_entrance
                    if count_hours > 7200:
                        result+=1

                    break
    return result

# test_calculateNumOfCars()





