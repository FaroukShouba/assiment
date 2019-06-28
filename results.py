import psycopg2


class Results:

    def __init__(self, centername, centernumber, validvotes, id):
        self.centername = centername
        self.centernumber = centernumber
        self.validvotes = validvotes
        self.id = id

    def __repr__(self):
        return "<Results {}>".format(self.centernumber)




    def save_to_db(self):
        with psycopg2.connect(database="election", user="farouk", password="0000", host="localhost") as connection:
            with connection.cursor() as cursor:
                cursor.execute('INSERT INTO results (centername, centernumber, validvotes) VALUES (%s, %s, %s)',
                               (self.centername, self.centernumber, self.validvotes))











