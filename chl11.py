import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

def preprocess_data(filename):
    try:
        df = pd.read_excel(filename)
        print("\nData sebelum preprocessing:")
        print(df.head())
        
        df = df.dropna()
        print("\nData setelah preprocessing:")
        print(df.head())
        return df
    except Exception as e:
        print(f"Error: {e}")
        return None
    
filename = "air_quality.xlsx"  
data = preprocess_data(filename)

def naive_bayes_model(df, target_column):
    try:
        X = df.drop(columns=[target_column])
        y = df[target_column]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        model = GaussianNB()
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        
        accuracy = accuracy_score(y_test, y_pred)
        print(f"Akurasinya adalah: {accuracy:.2f}")
    except Exception as e:
        print(f"Error: {e}")

def decision_tree_model(df, target_column):
    try:
        X = df.drop(columns=[target_column])
        y = df[target_column]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        model = DecisionTreeClassifier()
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        
        accuracy = accuracy_score(y_test, y_pred)
        print(f"Akurasinya adalah: {accuracy:.2f}")
    except Exception as e:
        print(f"Error: {e}")

def main_menu():
    while True:
        print("\n===================================")
        print("              Naive Bayes           ")
        print("===================================")
        print("1. Input Data")
        print("2. Hasil")
        print("3. Kembali ke Menu Utama")
        print("0. Keluar")
        pilihan = input("Pilih Menu: ")

        if pilihan == '1':
            filename = input("Masukkan nama file (contoh: air_quality.xlsx): ")
            global data
            data = preprocess_data(filename)
            if data is not None:
                print("\nData berhasil diinput dan diproses.")
        elif pilihan == '2':
            if 'data' in globals() and data is not None:
                target_column = input("Masukkan nama kolom target: ")
                print("\nPilih Algoritma:")
                print("1. Naive Bayes")
                print("2. Decision Tree")
                algo = input("Pilih Algoritma: ")
                
                if algo == '1':
                    naive_bayes_model(data, target_column)
                elif algo == '2':
                    decision_tree_model(data, target_column)
                else:
                    print("Pilihan algoritma tidak valid.")
            else:
                print("Harap input data terlebih dahulu (Menu 1).")
        elif pilihan == '3':
            print("Kembali ke Menu Utama...")
        elif pilihan == '0':
            print("Program selesai. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main_menu()
