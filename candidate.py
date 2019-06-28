import psycopg2





class Candidate:


    def __init__(self, electiontype, voter_id, status, date_application, id):
        self.electiontype = electiontype
        self.voter_id = voter_id
        self.status = status
        self.date_application = date_application
        self.id = id


    def __repr__(self):
        return "<candidate {}>".format(self.electiontype)



    #
    # def save_to_db(self):
    #     with psycopg2.connect(database="election", user="farouk", password="0000", host="localhost") as connection:
    #         with connection.cursor() as cursor:
    #             cursor.execute('INSERT INTO voter (first_name, third_name, family_name, date_birth, place_birth, governorate, province, district, city, '
    #             'quarter, status, type, national_id_no, family_book_no) VALUES (%s, %s, %s,%s, %s, %s, %s, %s, %s,%s, %s, %s,%s, %s)',
    #                            (self.centername, self.centernumber, self.validvotes))