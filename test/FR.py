# import cv2
# import numpy as np
# import sqlite3
# import threading

# # Charger le classificateur Haar pour la détection de visages
# faceDetect = cv2.CascadeClassifier('C:/Users/pc/Desktop/F-R/projet-R-F/haarcascade_frontalface_default.xml')

# # Initialiser la caméra
# cam = cv2.VideoCapture(0)  # 0 pour la webcam intégrée

# def insertorupdate(id, name):
#     # Fonction pour insérer ou mettre à jour les enregistrements dans la base de données
#     conn = sqlite3.connect("sqlite.db")  # Connexion à la base de données
#     cursor = conn.cursor()  # Créer un curseur pour exécuter des commandes SQL
#     cursor.execute("SELECT * FROM PERSONS WHERE ID=?", (id,))
#     isRecordExist = cursor.fetchone() is not None  # Vérifier si l'enregistrement existe
#     if isRecordExist:  # Si l'enregistrement existe, mettre à jour le nom
#         cursor.execute("UPDATE PERSONS SET Name=? WHERE ID=?", (name, id))
#         print(f"Updated record for ID: {id}")
#     else:  # Si l'enregistrement n'existe pas, insérer un nouveau
#         cursor.execute("INSERT INTO PERSONS (ID, Name) VALUES (?, ?)", (id, name))
#         print(f"Inserted new record for ID: {id}")
#     conn.commit()  # Valider les modifications
#     conn.close()  # Fermer la connexion à la base de données

# def capture_faces(id):
#     sampleNum = 0  # Compteur pour les échantillons d'images

#     while True:
#         ret, img = cam.read()  # Lire une image de la caméra
#         if not ret:
#             print("Failed to capture image")
#             break
        
#         gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convertir l'image en niveaux de gris
#         faces = faceDetect.detectMultiScale(gray, 1.3, 5)  # Détecter les visages
#         for (x, y, w, h) in faces:
#             sampleNum += 1  # Incrémenter le compteur d'échantillons
#             cv2.imwrite(f"dataset/user.{id}.{sampleNum}.jpg", gray[y:y+h, x:x+w])  # Enregistrer l'image
#             cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)  # Dessiner un rectangle autour du visage
#             print(f"Captured image {sampleNum} for user ID: {id}")
#             cv2.waitKey(100)  # Attendre 100ms

#         cv2.imshow("face", img)  # Afficher l'image avec le rectangle
#         if cv2.waitKey(1) & 0xFF == ord('q'):  # Appuyer sur 'q' pour quitter
#             print("Quitting capture...")
#             break
#         if sampleNum >= 20:  # Capturer 20 échantillons
#             print("Captured 20 images, stopping...")
#             break

#     cam.release()  # Libérer la caméra
#     cv2.destroyAllWindows()  # Fermer toutes les fenêtres
#     print("Capture complete and camera released.")

# def get_user_input():
#     id = input("Entrer user ID: ")
#     name = input("Entrer user name: ")
#     insertorupdate(id, name)
#     return id

# # Utiliser threading pour demander les entrées utilisateur
# user_id = threading.Thread(target=get_user_input)
# user_id.start()
# user_id.join()

# # Commencer la capture des visages après avoir reçu les entrées utilisateur
# capture_faces(user_id)



