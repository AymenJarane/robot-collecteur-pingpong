# In[ ]
import joblib
import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt
import cv2
import warnings
import glob
import numpy as np
from sklearn.model_selection import train_test_split

warnings.filterwarnings('ignore')

# Initialisation des listes pour les images et labels
X = []
y = []
image_dim = 194  # Taille des images

# Chargement des images pour chaque employé
def load_images_from_folder(folder_path, label):
    images = glob.glob(folder_path + '/*.jpg')  # Chargement des fichiers d'images
    for image_file in images:
        img = cv2.imread(image_file)
        img = cv2.resize(img, (image_dim, image_dim))
        X.append(img)
        y.append(label)

# Chargement des images des employés
load_images_from_folder(r"C:\Users\Aymen\Documents\birse\PJT_PINGPONG_ROBOT\BDD_BALLE", 0)

# Conversion des listes en tableaux NumPy
X = np.array(X, dtype=np.float32)
y = np.array(y)
print (X)
print(y)
# In[]
# Division des données en ensemble d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalisation des images (valeurs entre 0 et 1)
X_train /= 255.0
X_test /= 255.0

# Création du modèle CNN
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(194, 194, 3)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(3, activation='softmax')  
])

# Affichage de l'architecture du modèle
model.summary()

# Compilation du modèle
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])


# Entraînement du modèle
history = model.fit(X_train, y_train, epochs=15, validation_data=(X_test, y_test))
joblib.dump(history, "reconnaissance_faciale.pkl")# 
# Affichage de l'évolution de l'accuracy
plt.plot(history.history['accuracy'], label='accuracy')
plt.plot(history.history['val_accuracy'], label='val_accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend(loc='lower right')
plt.show()
# Évaluation finale du modèle
test_loss, test_acc = model.evaluate(X_test, y_test, verbose=2)
print(f"\nTest Accuracy: {test_acc:.4f}")
# In[ ]
from tensorflow.keras.models import save_model
save_model(model,r"C:\Users\Aymen\Documents\birse\PJT_PINGPONG_ROBOT\Programmes\model.h5")
