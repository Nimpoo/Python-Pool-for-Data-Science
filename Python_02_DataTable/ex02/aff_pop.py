from load_csv import load
import matplotlib.pyplot as plt


def main():

    """
    /----------- Utility -----------/
    Display a graph shape that represents life
    in relation to the years to come of France
    instead of another country

    /---------- Arguments ----------/
    Nothing 

    /----------- Return ------------/
    Return nothing
    """

    try:
        data_frame = load("population_total.csv")

        years_france = data_frame.loc[data_frame["country"] == "France"]
        years_morocco = data_frame.loc[data_frame["country"] == "Morocco"]

    except AttributeError:
        print("AttributeError: plz use a .csv valid file")
        return (None)
    except Exception as e:
        print(e)
        return (None)


    lst_years_france = years_france.columns.to_list()
    lst_values_france = [val for sublist in years_france.values.tolist() for val in sublist]

    lst_years_morocco = years_morocco.columns.to_list()
    lst_values_morocco = [val for sublist in years_morocco.values.tolist() for val in sublist]


    lst_years_france.pop(0)
    lst_values_france.pop(0)

    lst_years_morocco.pop(0)
    lst_values_morocco.pop(0)


    lst_int_years_france = [year for year in lst_years_france]
    lst_int_years_morocco = [year for year in lst_years_morocco]


    plt.title("Life Expectancy Projections")

    plt.xlabel("Year")
    plt.ylabel("Life Expectancy")

    plt.xticks([i for i in range(1800, 2081, 40)])

    plt.plot(lst_int_years_france, lst_values_france, label="France")
    plt.plot(lst_int_years_morocco, lst_values_morocco, label="Morocco")

    plt.legend(loc="lower right")

    plt.show()


if __name__ == "__main__":
    main()
