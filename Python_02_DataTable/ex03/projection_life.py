from load_csv import load
import matplotlib.pyplot as plt


def main():

    """
    /----------- Utility -----------/
    Displays the projection of life expectancy
    in relation to the gross national product of
    the year 1900 for each country.

    /---------- Arguments ----------/
    Nothing

    /----------- Return ------------/
    Return nothing
    """

    try:
        data_frame_life = load("life_expectancy_years.csv")
        data_frame_gross =\
            load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")

        life = data_frame_life.loc[data_frame_life["1900"] == "1900"]
        life = data_frame_life.iloc[:, 101:102]

        gross = data_frame_gross.loc[data_frame_gross["1900"] == "1900"]
        gross = data_frame_gross.iloc[:, 101:102]

    except AttributeError:
        print("AttributeError: plz use a .csv valid file")
        return (None)
    except Exception as e:
        print(e)
        return (None)

    fig, axe = plt.subplots()

    for i in range(len(gross.columns)):
        axe.scatter(gross.iloc[:, i], life.iloc[:, i])

    axe.set_yticks([20, 25, 30, 35, 40, 45, 50, 55])
    axe.set_yticklabels([20, 25, 30, 35, 40, 45, 50, 55])
    axe.set_xticks([300, 1000, 10000])
    axe.set_xticklabels(["300", "1k", "10k"])

    plt.title("1900")
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life Expectancy")

    plt.show()


if __name__ == "__main__":
    main()
