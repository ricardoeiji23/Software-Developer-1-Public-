#Number examples u = 10 t = 4 a = 2


u_initial_velocity_u = float(input("Enter the initial velocity value(u): ")) #m/s
t_time_taken_t = float(input("Enter the time taken value(t): ")) # seconds
a_acceleration_a = float(input("Enter the acceleration value(a): ")) #m/2**2

s_distance_s = u_initial_velocity_u * t_time_taken_t + 0.5 * a_acceleration_a * t_time_taken_t**2


print("\nThe distance travelled by the object is(s):", str (s_distance_s))