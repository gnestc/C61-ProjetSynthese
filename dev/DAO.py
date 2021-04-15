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

    def getImagesByColor(self, color):
        conn = psycopg2.connect(
            host="localhost",
            database="c61projetsynthesedb",
            user="postgres",
            password="123")
        cur = conn.cursor()
        cur.execute("SELECT * FROM training_images "+
                    "WHERE color LIKE %s",
                    (color,))
        images=cur.fetchall()
        cur.close()
        conn.close()
        return images

    def insertDataset(self, centers, dateString):
        conn = psycopg2.connect(
            host="localhost",
            database="c61projetsynthesedb",
            user="postgres",
            password="123")
        cur = conn.cursor()
        cur.execute("INSERT INTO datasets_by_date(date) " +
                    "VALUES(%s)",
                    (dateString,))
        conn.commit()

        for center in centers:
            cur.execute("INSERT INTO datasets_content(color, rgb, dataset) " +
                        "VALUES(%s, %s, (SELECT dataset FROM datasets_by_date WHERE date = %s))",
                        (center[0], center[1], dateString))
            conn.commit()
        cur.close()
        conn.close()

    def getDatasetsByDate(self):
        conn = psycopg2.connect(
            host="localhost",
            database="c61projetsynthesedb",
            user="postgres",
            password="123")
        cur = conn.cursor()
        cur.execute("SELECT * FROM datasets_by_date ")
        data=cur.fetchall()
        cur.close()
        conn.close()
        return data

    def getDatasetsContent(self, datasetNum):
        conn = psycopg2.connect(
            host="localhost",
            database="c61projetsynthesedb",
            user="postgres",
            password="123")
        cur = conn.cursor()
        cur.execute("SELECT color, rgb FROM datasets_content "+
                    "WHERE dataset = %s",
                    (datasetNum,))
        data=cur.fetchall()
        cur.close()
        conn.close()
        return data

    def deleteDataset(self, datasetNum):
        conn = psycopg2.connect(
            host="localhost",
            database="c61projetsynthesedb",
            user="postgres",
            password="123")
        cur = conn.cursor()
        cur.execute("DELETE FROM datasets_content "+
                    "WHERE dataset = %s",
                    (datasetNum,))
        conn.commit()
        cur.execute("DELETE FROM datasets_by_date "+
                    "WHERE dataset = %s",
                    (datasetNum,))
        conn.commit()
        cur.close()
        conn.close()

    def getMask(self, color):
        conn = psycopg2.connect(
            host="localhost",
            database="c61projetsynthesedb",
            user="postgres",
            password="123")
        cur = conn.cursor()
        cur.execute("SELECT * FROM masks "+
                    "WHERE color LIKE %s",
                    (color,))
        data=cur.fetchall()
        cur.close()
        conn.close()
        return data

    def getAllMasks(self):
        conn = psycopg2.connect(
            host="localhost",
            database="c61projetsynthesedb",
            user="postgres",
            password="123")
        cur = conn.cursor()
        cur.execute("SELECT * FROM masks ")
        data=cur.fetchall()
        cur.close()
        conn.close()
        return data

    def updateMask(self, savedValues):
        conn = psycopg2.connect(
            host="localhost",
            database="c61projetsynthesedb",
            user="postgres",
            password="123")
        cur = conn.cursor()
        cur.execute("UPDATE masks SET hsv_min = %s, hsv_max= %s "+
                    "WHERE color LIKE %s",
                    (savedValues[1], savedValues[2], savedValues[0]))
        conn.commit()
        cur.close()
        conn.close()