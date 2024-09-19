import numpy as np
import matplotlib.pyplot as plt

city_x = np.array([100, 120, 85, 90, 110, 95])
city_y = np.array([80, 75, 60, 95, 85, 90])
city_z = np.array([150, 140, 40, 160, 155, 170])

def calculate_total(city_x, city_y, city_z):
    sum_x = 0
    sum_y = 0
    sum_z = 0
    for x in city_x:
        sum_x += x
    for y in city_y:
        sum_y +=y
    for z in city_z:
        sum_z += z
    print(f"total rainfall in all 3 cities are over the six months:\ncity_x : {sum_x}\ncity_y : {sum_y}\ncity_z : {sum_z}\n")
    return sum_x, sum_y, sum_z

def calculate_mean(city_x, city_y, city_z):
    print(f"average rainfall in all 3 cities are:\ncity_x: {np.mean(city_x)}\ncity_y : {np.mean(city_y)}\ncity_z : {np.mean(city_z)}\n")
    return np.mean(city_x), np.mean(city_y), np.mean(city_z)

def average_monthly_rainfall(city_x, city_y, city_z):
    avg_monthly = np.array([0, 0, 0, 0, 0, 0])
    for i in range(0, len(city_z)):
         avg_monthly[i] = (city_x[i] + city_y[i] + city_z[i])/3
    print(f"Average monthly rainfall for each month: ")
    for i in range(0, len(avg_monthly)):
        print(f"Month {i}: " + str(avg_monthly[i]))
    
def calculate_range(city_x, city_y, city_z):
    city_x_range = np.max(city_x) - np.min(city_x)
    city_y_range = np.max(city_y) - np.min(city_y)
    city_z_range = np.max(city_z) - np.min(city_z)
    return city_x_range, city_y_range, city_z_range
    
def main():
    print()
    calculate_total(city_x, city_y, city_z)
    calculate_mean(city_x, city_y, city_z)
    average_monthly_rainfall(city_x, city_y, city_z)
    x = np.arange(0,6)
    plt.title("Rainfall plot of all 3 cities")
    plt.xlabel("Months")
    plt.ylabel("Cities")
    plt.plot(x, city_x, color="r", label="City x")
    plt.plot(x, city_y, color="b", label="City y")
    plt.plot(x, city_z, color="g", label="City z")
    plt.legend()
    plt.show()
    plt.title("Bar chart of range of all 3 cities")
    plt.xlabel("Cities")
    plt.ylabel("Range")
    cities = np.array(['x', 'y', 'z'])
    city_x_range, city_y_range, city_z_range = calculate_range(city_x, city_y, city_z)
    range_array = np.array([city_x_range, city_y_range, city_z_range])
    plt.bar(cities, range_array, width=0.5)
    plt.show()
    
if __name__ == "__main__":
    main()