import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

def proses_data(nama_file):
    try:
        df = pd.read_excel(nama_file)
        print("\nData sebelum diproses:")
        print(df.head())
        
        df = df.dropna()
        print("\nData setelah diproses:")
        print(df.head())
        return df
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        return None
    
nama_file = "air_quality.xlsx"  
data = proses_data(nama_file)

def model_naive_bayes(df, kolom_target):
    try:
        X = df.drop(columns=[kolom_target])
        y = df[kolom_target]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        model = GaussianNB()
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        
        akurasi = accuracy_score(y_test, y_pred)
        print(f"Akurasinya adalah: {akurasi:.2f}")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

def model_pohon_keputusan(df, kolom_target):
    try:
        X = df.drop(columns=[kolom_target])
        y = df[kolom_target]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        model = DecisionTreeClassifier()
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        
        akurasi = accuracy_score(y_test, y_pred)
        print(f"Akurasinya adalah: {akurasi:.2f}")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

def menu_utama():
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
            nama_file = input("Masukkan nama file (contoh: air_quality.xlsx): ")
            global data
            data = proses_data(nama_file)
            if data is not None:
                print("\nData berhasil diinput dan diproses.")
        elif pilihan == '2':
            if 'data' in globals() and data is not None:
                kolom_target = input("Masukkan nama kolom target: ")
                print("\nPilih Algoritma:")
                print("1. Naive Bayes")
                print("2. Pohon Keputusan")
                algo = input("Pilih Algoritma: ")
                
                if algo == '1':
                    model_naive_bayes(data, kolom_target)
                elif algo == '2':
                    model_pohon_keputusan(data, kolom_target)
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
    menu_utama()
