import psycopg2

class DAO():
    def __init__(self):
        self.conn = psycopg2.connect(
            host="localhost",
            database="c61projetsynthesedb",
            user="postgres",
            password="123")

    def insertDB(self, dateString, colorName, img):

        cur = self.conn.cursor()
        cur.execute("INSERT INTO training_images(date, color,img) " +
                    "VALUES(%s,%s, %s)",
                    (dateString, colorName, psycopg2.Binary(img)))
        self.conn.commit()
        cur.close()
        self.conn.close()

    def getTrainingImages(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM training_images")
        images = cur.fetchall()
        cur.close()
        self.conn.close()
        return images

    def deleteImg(self, key):
        cur = self.conn.cursor()
        cur.execute("DELETE FROM training_images "+
                    "WHERE date LIKE %s",
                    (key,))
        self.conn.commit()
        cur.close()
        self.conn.close()

    def getImagesByColor(self, color):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM training_images "+
                    "WHERE color LIKE %s",
                    (color,))
        images=cur.fetchall()
        cur.close()
        self.conn.close()
        return images

    def insertDataset(self, centers, dateString):
        cur = self.conn.cursor()
        cur.execute("INSERT INTO datasets_by_date(date) " +
                    "VALUES(%s)",
                    (dateString,))
        self.conn.commit()

        for center in centers:
            cur.execute("INSERT INTO datasets_content(color, rgb, dataset) " +
                        "VALUES(%s, %s, (SELECT dataset FROM datasets_by_date WHERE date = %s))",
                        (center[0], center[1], dateString))
            self.conn.commit()
        cur.close()
        self.conn.close()

    def getDatasetsByDate(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM datasets_by_date ")
        data=cur.fetchall()
        cur.close()
        self.conn.close()
        return data

    def getDatasetsContent(self, datasetNum):
        cur = self.conn.cursor()
        cur.execute("SELECT color, rgb FROM datasets_content "+
                    "WHERE dataset = %s",
                    (datasetNum,))
        data=cur.fetchall()
        cur.close()
        self.conn.close()
        return data

    def deleteDataset(self, datasetNum):
        cur = self.conn.cursor()
        cur.execute("DELETE FROM datasets_content "+
                    "WHERE dataset = %s",
                    (datasetNum,))
        self.conn.commit()
        cur.execute("DELETE FROM datasets_by_date "+
                    "WHERE dataset = %s",
                    (datasetNum,))
        self.conn.commit()
        cur.close()
        self.conn.close()

    def getMask(self, color):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM masks "+
                    "WHERE color LIKE %s",
                    (color,))
        data=cur.fetchall()
        cur.close()
        self.conn.close()
        return data

    def getAllMasks(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM masks ")
        data=cur.fetchall()
        cur.close()
        self.conn.close()
        return data

    def updateMask(self, savedValues):
        cur = self.conn.cursor()
        cur.execute("UPDATE masks SET hsv_min = %s, hsv_max= %s "+
                    "WHERE color LIKE %s",
                    (savedValues[1], savedValues[2], savedValues[0]))
        self.conn.commit()
        cur.close()
        self.conn.close()