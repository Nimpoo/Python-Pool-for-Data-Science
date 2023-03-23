from load_csv import load
import matplotlib.pyplot as plt


def main():

    """
    /----------- Utility -----------/
    Display a graph that represents life
    in relation to the years to come

    /---------- Arguments ----------/
    Nothing

    /----------- Return ------------/
    Return nothing
    """

    try:
        # ? Generate the DataFrame
        data_frame = load("life_expectancy_years.csv")

        # ? Take the data only for France in type :
        # ?'pandas.core.frame.DataFrame'
        years = data_frame.loc[data_frame["country"] == "France"]

        # * Parsng
    except AttributeError:
        print("AttributeError: plz use a .csv valid file")
        return (None)
    except Exception as e:
        print(e)
        return (None)

    # ? Convert years : 'pandas.core.frame.DataFrame' to 'list
    lst_years = years.columns.to_list()
    # ? Convert years : 'numpy.ndarray' to 'list BUT it's a double list
    lst_values = years.values.tolist()

    # ? Convert double list to flat list
    flat_lst_values = []
    for elem in lst_values:
        if type(elem) is list:
            for item in elem:
                flat_lst_values.append(item)
        else:
            flat_lst_values.append()

    # * Remove the first element : 'France'
    flat_lst_values.pop(0)
    # * Remove the first element : 'country'
    lst_years.pop(0)

    lst_int_years = [eval(elem) for elem in lst_years]

    # * Set the title
    plt.title("France Life expectancy Projections")
    # * Set the x-axis
    plt.xlabel("Year")
    # * Set the y-axis
    plt.ylabel("Life expectancy")
    # ! Plot the graph with the x-axis 'Years'
    # ! (lst_int_list) and 'Life expectancy' (flat_lst_values)
    plt.plot(lst_int_years, flat_lst_values)

    # * Display the setup graph
    plt.show()


if __name__ == "__main__":
    main()
