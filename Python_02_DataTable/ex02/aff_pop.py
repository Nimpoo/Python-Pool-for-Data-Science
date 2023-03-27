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

        pop_fr = data_frame.loc[data_frame["country"] == "France"]
        pop_fr = pop_fr.iloc[:, 1:]
        pop_fr = pop_fr.applymap(lambda x: float(x.strip("M")))

        pop_bg = data_frame.loc[data_frame["country"] == "Belgium"]
        pop_bg = pop_bg.iloc[:, 1:]
        pop_bg = pop_bg.applymap(lambda x: float(x.strip("M")))

    except AttributeError:
        print("AttributeError: plz use a .csv valid file")
        return (None)
    except Exception as e:
        print(e)
        return (None)

    plt.title("Life Expectancy Projections")

    plt.xlabel("Year")
    plt.ylabel("Life Expectancy")
    fig, axe = plt.subplots()
    axe.set_yticks([3, 14, 28, 40, 70])
    axe.set_yticklabels(["3M", "14M", "28M", "40M", "70M"])
    plt.xticks(range(1800, 2081, 40))
    years = pop_fr.columns.values.astype(int)
    plt.plot(years, pop_fr.values[0], label="France")
    plt.plot(years, pop_bg.values[0], label="Belgium")

    plt.legend(loc="lower right")

    plt.show()


if __name__ == "__main__":
    main()
