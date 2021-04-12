import psycopg2

class DAO:
    def insertDB(self, dateString, colorName, img):
        conn = psycopg2.connect(
            host="localhost",
            database="c61projetsynthesedb",
            user="postgres",
            password="123")
        cur = conn.cursor()
        cur.execute("INSERT INTO training_images(date, color,img) " +
                    "VALUES(%s,%s, %s)",
                    (dateString, colorName, psycopg2.Binary(img)))
        conn.commit()
        cur.close()
        conn.close()

    def getTrainingImages(self):
        conn = psycopg2.connect(
            host="localhost",
            database="c61projetsynthesedb",
            user="postgres",
            password="123")
        cur = conn.cursor()
        cur.execute("SELECT * FROM training_images")
        images = cur.fetchall()
        cur.close()
        conn.close()
        return images

    def deleteImg(self, key):
        conn = psycopg2.connect(
            host="localhost",
            database="c61projetsynthesedb",
            user="postgres",
            password="123")
        cur = conn.cursor()
        cur.execute("DELETE FROM training_images "+
                    "WHERE date LIKE %s",
                    (key,))
        conn.commit()
        cur.close()
        conn.close()