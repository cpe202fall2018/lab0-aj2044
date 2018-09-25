def weight_on_planets():
    # write your code here
    normal_weight = float(input("What do you weigh on earth? "))
    mars_weight = normal_weight * 0.38
    jupiter_weight = normal_weight * 2.34
    print("\nOn Mars you would weigh {} pounds.\nOn Jupiter you would weigh {} pounds.".format(mars_weight, jupiter_weight))


if __name__ == '__main__':
    weight_on_planets()
