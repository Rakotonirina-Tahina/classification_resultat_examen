import tensorflow as tf
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
"""
    Cette devoir est une classification binaire (0/1 ou Reussir/echoue) 
    pour classifier les etudiants d'apres leurs horaires d'etudes et 
    moyenne scolaire s'il va reussir un cours ou pas 
"""
data = {
    'heure_etude': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'moyenne_scolaire': [10, 13, 15, 9, 5, 13, 14, 16, 18, 20],
    'reussite_examen': [0, 0, 1, 0, 0, 1, 1, 1, 1, 1]
}
data_etudiant = pd.DataFrame(data)
x = data_etudiant[['heure_etude', 'moyenne_scolaire']].values
y = data_etudiant['reussite_examen'].values
scaler = StandardScaler()
x1 = scaler.fit_transform(x)
x_train, x_test, y_train, y_test = train_test_split(x1, y, test_size=0.2, random_state=42)
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(10, activation='relu', input_shape=(x_train.shape[1],)),
    tf.keras.layers.Dense(5, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(x_train, y_train, epochs=100, batch_size=2, verbose=0)
loss, accuracy = model.evaluate(x_test, y_test, verbose=0)
print(f"Loss: {loss:.4f}, Accuracy: {accuracy:.4f}")
etudiants = pd.DataFrame({
    'heure_etude': [2, 5, 8, 3, 6, 4],
    'moyenne_scolaire': [12, 10, 12, 9, 8, 15]
})
etudiants_array = np.column_stack((etudiants['heure_etude'], etudiants['moyenne_scolaire']))
x_etudiant = scaler.transform(etudiants_array)
predictions = model.predict(x_etudiant)
classes = (predictions > 0.5).astype(int)
print("|----------------------------------------------------------------------------------|")
print("|         Etudiant         |           Classe          |         Pourcentage       |")
print("|----------------------------------------------------------------------------------|")
for i in range (len(etudiants['moyenne_scolaire'])):
    proba = predictions[i][0]
    classe = classes[i][0]
    print(f"|           {i+1}              |          {'Réussir' if classe == 1 else 'Echoue '}          |             {proba*100:.0f}%           |")
    print("|----------------------------------------------------------------------------------|")