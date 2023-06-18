import pandas as pd
import ssl
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import tkinter
from tkinter import *
from tkinter import ttk
import random

def train_window():
    new_window = tkinter.Toplevel(root)
    new_window.title("Wytenowano")
    knn.fit(X_train, y_train)
    label = ttk.Label(new_window, text="Wytrenowano model")
    label.pack()
    test_button.config(state='normal')
    predict_button.config(state='normal')
    rebuild_button.config(state='normal')

def test_window():
    new_window = tkinter.Toplevel(root)
    new_window.title("Przetestowano")
    predict = knn.predict(X_test)
    acc = accuracy_score(y_test, predict)
    label = ttk.Label(new_window, text="Dokladnosc modelu przy wykorzystaniu danych testowych wynosi: " + str(acc))
    label.pack()

def predict_window():
    new_window = tkinter.Toplevel(root)
    new_window.title("Podaj dane wina do predykcji")

    Alcohol_label = ttk.Label(new_window, text="Alcohol")
    Alcohol_label.pack()
    Alcohol_entry = ttk.Entry(new_window)
    Alcohol_entry.pack()

    Malicacid_label = ttk.Label(new_window, text="Malicacid")
    Malicacid_label.pack()
    Malicacid_entry = ttk.Entry(new_window)
    Malicacid_entry.pack()

    Ash_label = ttk.Label(new_window, text="Ash")
    Ash_label.pack()
    Ash_entry = ttk.Entry(new_window)
    Ash_entry.pack()

    Alcalinity_of_ash_label = ttk.Label(new_window, text="Alcalinity_of_ash")
    Alcalinity_of_ash_label.pack()
    Alcalinity_of_ash_entry = ttk.Entry(new_window)
    Alcalinity_of_ash_entry.pack()

    Magnesium_label = ttk.Label(new_window, text="Magnesium")
    Magnesium_label.pack()
    Magnesium_entry = ttk.Entry(new_window)
    Magnesium_entry.pack()

    Total_phenols_label = ttk.Label(new_window, text="Total_phenols")
    Total_phenols_label.pack()
    Total_phenols_entry = ttk.Entry(new_window)
    Total_phenols_entry.pack()

    Flavanoids_label = ttk.Label(new_window, text="Flavanoids")
    Flavanoids_label.pack()
    Flavanoids_entry = ttk.Entry(new_window)
    Flavanoids_entry.pack()

    Nonflavanoid_phenols_label = ttk.Label(new_window, text="Nonflavanoid_phenols")
    Nonflavanoid_phenols_label.pack()
    Nonflavanoid_phenols_entry = ttk.Entry(new_window)
    Nonflavanoid_phenols_entry.pack()

    Proanthocyanins_label = ttk.Label(new_window, text="Proanthocyanins")
    Proanthocyanins_label.pack()
    Proanthocyanins_entry = ttk.Entry(new_window)
    Proanthocyanins_entry.pack()

    Color_intensity_label = ttk.Label(new_window, text="Color_intensity")
    Color_intensity_label.pack()
    Color_intensity_entry = ttk.Entry(new_window)
    Color_intensity_entry.pack()

    Hue_label = ttk.Label(new_window, text="Hue")
    Hue_label.pack()
    Hue_entry = ttk.Entry(new_window)
    Hue_entry.pack()

    x_of_diluted_wines_label = ttk.Label(new_window, text="0D280_0D315_of_diluted_wines")
    x_of_diluted_wines_label.pack()
    x_of_diluted_wines_entry = ttk.Entry(new_window)
    x_of_diluted_wines_entry.pack()

    Proline_label = ttk.Label(new_window, text="Proline")
    Proline_label.pack()
    Proline_entry = ttk.Entry(new_window)
    Proline_entry.pack()

    def predict():
        list = [[]]
        Alcohol = Alcohol_entry.get()
        list[0].append(Alcohol)
        Malicacid = Malicacid_entry.get()
        list[0].append(Malicacid)
        Ash = Ash_entry.get()
        list[0].append(Ash)
        Alcalinity_of_ash = Alcalinity_of_ash_entry.get()
        list[0].append(Alcalinity_of_ash)
        Magnesium = Magnesium_entry.get()
        list[0].append(Magnesium)
        Total_phenols = Total_phenols_entry.get()
        list[0].append(Total_phenols)
        Flavanoids = Flavanoids_entry.get()
        list[0].append(Flavanoids)
        Nonflavanoid_phenols = Nonflavanoid_phenols_entry.get()
        list[0].append(Nonflavanoid_phenols)
        Proanthocyanins = Proanthocyanins_entry.get()
        list[0].append(Proanthocyanins)
        Color_intensity = Color_intensity_entry.get()
        list[0].append(Color_intensity)
        Hue = Hue_entry.get()
        list[0].append(Hue)
        x_of_diluted_wines = x_of_diluted_wines_entry.get()
        list[0].append(x_of_diluted_wines)
        Proline = Proline_entry.get()
        list[0].append(Proline)
        tmpdf = pd.DataFrame(list, columns=["Alcohol", "Malicacid", "Ash", "Alcalinity_of_ash", "Magnesium", "Total_phenols",
                   "Flavanoids", "Nonflavanoid_phenols", "Proanthocyanins", "Color_intensity", "Hue",
                   "0D280_0D315_of_diluted_wines", "Proline"])
        print(tmpdf)
        prediction = knn.predict(tmpdf)
        print(prediction)
        tmpdf.insert(0,"class",prediction,True)
        x = tmpdf.values[0].tolist()

        print(x)
        my_tree.insert('', "end", values=x)
        new_window.destroy()
    predict_but = ttk.Button(new_window, text="Predict", command=predict)
    predict_but.pack()
def rebuild_window():
    new_window = tkinter.Toplevel(root)
    new_window.title("Odbudowano")
    new_r = random.randint(1, 9999)
    new_X_train, new_X_test, new_y_train, new_y_test = train_test_split(X, y, test_size=0.25, random_state=new_r, shuffle=True)
    knn.fit(new_X_train, new_y_train)
    for i in my_tree.get_children():
        my_tree.delete(i)
    label = ttk.Label(new_window, text="Wybudowano model ponownie")
    label.pack()



ssl._create_default_https_context = ssl._create_unverified_context
file_name = 'wine.data'
headers = ["class", "Alcohol", "Malicacid", "Ash", "Alcalinity_of_ash", "Magnesium", "Total_phenols", "Flavanoids", "Nonflavanoid_phenols", "Proanthocyanins", "Color_intensity", "Hue", "0D280_0D315_of_diluted_wines", "Proline"]

df = pd.read_csv(file_name, names=headers)
X = df.iloc[:, 1:]
y = df.iloc[:, 0]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=2023, shuffle=True)

knn = KNeighborsClassifier()


root = Tk()
root.title('Wine')
root.geometry("1500x500")

tree_frame = Frame(root)
tree_frame.pack(pady=10)

tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")

tree_scroll.config(command=my_tree.yview)

my_tree["columns"] = ("class", "Alcohol", "Malicacid", "Ash","Alcalinity_of_ash", "Magnesium", "Total_phenols", "Flavanoids", "Nonflavanoid_phenols", "Proanthocyanins", "Color_intensity", "Hue", "0D280_0D315_of_diluted_wines", "Proline")
my_tree.column("#0", width=0)
my_tree.column("class", width=20)
my_tree.column("Alcohol", width=60)
my_tree.column("Malicacid", width=60)
my_tree.column("Ash", width=40)
my_tree.column("Alcalinity_of_ash", width=40)
my_tree.column("Magnesium", width=40)
my_tree.column("Total_phenols", width=40)
my_tree.column("Flavanoids", width=40)
my_tree.column("Nonflavanoid_phenols", width=40)
my_tree.column("Proanthocyanins", width=40)
my_tree.column("Color_intensity", width=40)
my_tree.column("Hue", width=40)
my_tree.column("0D280_0D315_of_diluted_wines", width=40)
my_tree.column("Proline", width=40)

my_tree.heading("class", text="class", anchor=CENTER)
my_tree.heading("Alcohol", text="Alcohol", anchor=CENTER)
my_tree.heading("Malicacid", text="Malicacid", anchor=CENTER)
my_tree.heading("Ash", text="Ash", anchor=CENTER)
my_tree.heading("Alcalinity_of_ash", text="Alcalinity_of_ash", anchor=CENTER)
my_tree.heading("Magnesium", text="Magnesium", anchor=CENTER)
my_tree.heading("Total_phenols", text="Total_phenols", anchor=CENTER)
my_tree.heading("Flavanoids", text="Flavanoids", anchor=CENTER)
my_tree.heading("Nonflavanoid_phenols", text="Nonflavanoid_phenols", anchor=CENTER)
my_tree.heading("Proanthocyanins", text="Proanthocyanins", anchor=CENTER)
my_tree.heading("Color_intensity", text="Color_intensity", anchor=CENTER)
my_tree.heading("Hue", text="Hue", anchor=CENTER)
my_tree.heading("0D280_0D315_of_diluted_wines", text="0D280_0D315_of_diluted_wines", anchor=CENTER)
my_tree.heading("Proline", text="Proline", anchor=CENTER)
my_tree.pack()

train_button = tkinter.Button(root, text="Wytrenuj model", command=train_window)
train_button.pack()
test_button =tkinter.Button(root, text="Przetestuj model", command=test_window, state=DISABLED)
test_button.pack()
predict_button =tkinter.Button(root, text="Predykcja", command=predict_window, state=DISABLED)
predict_button.pack()
rebuild_button = tkinter.Button(root, text="Zbuduj model ponownie", command=rebuild_window, state=DISABLED)
rebuild_button.pack()


root.mainloop()