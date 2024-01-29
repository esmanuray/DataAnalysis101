import pandas as pd
import matplotlib.pyplot as plt

pd.set_option("display.width", 500)
pd.set_option("display.max_columns", None)
df = pd.read_csv(file_path)

df["Date"] = pd.to_datetime(df["Date"])

recovered = [r for r in df["Total Recovered"]]
drecovered = []
for index, value in enumerate(recovered):
    if recovered[index] == recovered[index - 1]:
        drecovered.append(0)
    else:
        drecovered.append(value - recovered[index - 1])
drecovered[0] = 0
df["Daily Recovered"] = drecovered

died = [int(r) for r in df["Total Deaths"]]
death = []
for index, value in enumerate(died):
    if died[index] == died[index - 1]:
        death.append(0)
    else:
        death.append(died[index] - died[index - 1])
death[0] = 0
df["Daily Death"] = death

intubated = [r for r in df["Intubated Cases"]]
dintubated = []
for index, value in enumerate(intubated):
    if intubated[index] == intubated[index - 1]:
        dintubated.append(0)
    else:
        if value - intubated[index - 1] < 0:
            dintubated.append(0)
        else:
            dintubated.append(value - intubated[index - 1])
for index, value in enumerate(dintubated):
    if str(value) == 'nan':
        dintubated[index] = 0.0
df["Daily Intubated"] = dintubated

print(df.info())


def infoDataframe(DataFrame):
    print("date of last update of information : ", DataFrame["Date"].max())
    print("total case : ", DataFrame["Total Cases"].max())
    print("total death : ", DataFrame["Total Deaths"].max())
    print("total recovered : ", DataFrame["Total Recovered"].max())
    print("average case increase :  ", DataFrame["Daily(Cases/Test) %"].max())
    print("average death increase :  ", (DataFrame["Total Deaths"] / DataFrame["Total Cases"]).max())
    print("average intubated patient :  ", (DataFrame["Daily Intubated"] / DataFrame["Daily Cases"]).max())
    print("average recovered patient :  ", (DataFrame["Daily Recovered"] / DataFrame["Daily Cases"]).max())


def DataframeGraphics(dataframe):
    plt.subplot(1, 3, 1)
    plt.title("Daily Information")
    plt.plot(dataframe["Date"], dataframe["Daily Cases"], lw=2, label="Daily Cases")
    plt.plot(dataframe["Date"], dataframe["Daily Death"], lw=2, label="Daily Death")
    plt.plot(dataframe["Date"], dataframe["Daily Recovered"], lw=2, label="Daily Recovered")
    plt.plot(dataframe["Date"], dataframe["Daily Intubated"], lw=2, label="Daily Intubated")
    plt.legend()
    plt.xlabel("Date")
    plt.subplot(1, 3, 2)
    plt.title("Important Ratios")
    plt.plot(dataframe["Date"], dataframe["Total Deaths"], lw=2, label="Total deaths")
    plt.plot(dataframe["Date"], dataframe["Total Cases"], lw=2, label="Total cases")
    plt.plot(dataframe["Date"], dataframe["Total Recovered"], lw=2, label="Total recovered")
    plt.plot(dataframe["Date"], dataframe["Active Cases"], lw=2, label="Active Cases")
    plt.xlabel("Date")
    plt.legend()
    plt.subplot(1, 3, 3)
    plt.title("Ratio")
    plt.plot(dataframe["Date"], dataframe["(Death / Active Cases) %"], lw=2, label="Death/Active Cases")
    plt.plot(dataframe["Date"], dataframe["(Recovered / Active Cases) %"], lw=2, label="Active Cases/Population")
    plt.xlabel("Date")
    plt.legend()
    plt.show()


infoDataframe(df)
DataframeGraphics(df)
