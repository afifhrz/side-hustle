def roundtrip(time_date):
    ''' time date using years '''
    
    time_since_start = time_date * 3.154e7

    velocity = 16.9995 #km/second.
    dis_at_start = 22982855000 #km

    speed_of_light = 299792458 * 0.001 #meters / second

    distance = dis_at_start + velocity * time_since_start #km
    return 2 * distance / speed_of_light

roundtrip()