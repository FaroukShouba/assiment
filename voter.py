import psycopg2


class Voter:
    def __init__(self, first_name, third_name, family_name, id):
        self.first_name = first_name
        self.third_name = third_name
        self.family_name = family_name
        self.id = id

    def __repr__(self):
        return "<voter {}>".format(self.first_name)

    def save_to_db(self):
        with psycopg2.connect(database="election", user="farouk", password="0000", host="localhost") as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    'INSERT INTO voter (first_name, third_name, family_name) VALUES (%s, %s, %s)',
                    (self.first_name, self.third_name, self.family_name))


    # def __init__(self, first_name, third_name, family_name, date_birth, place_birth, governorate, province, district, city,
    #              quarter, status, type, national_id_no, family_book_no , id):
    #     self.first_name = first_name
    #     self.third_name = third_name
    #     self.family_name = family_name
    #     self.date_birth = date_birth
    #     self.place_birth = place_birth
    #     self.governorate = governorate
    #     self.province = province
    #     self.district = district
    #     self.city = city
    #     self.quarter = quarter
    #     self.status = status
    #     self.type = type
    #     self.national_id_no = national_id_no
    #     self.family_book_no = family_book_no
    #     self.id = id
    #
    # def __repr__(self):
    #     return "<voter {}>".format(self.first_name)
    #
    #
    #
    # def save_to_db(self):
    #     with psycopg2.connect(database="election", user="farouk", password="0000", host="localhost") as connection:
    #         with connection.cursor() as cursor:
    #             cursor.execute('INSERT INTO voter (first_name, third_name, family_name, date_birth, place_birth, governorate, province, district, city, '
    #             'quarter, status, type, national_id_no, family_book_no) VALUES (%s, %s, %s,%s, %s, %s, %s, %s, %s,%s, %s, %s,%s, %s)',
    #                            (self.first_name, self.third_name, self.family_name, self.date_birth, self.place_birth, self.governorate,
    #                             self.province, self.district, self.city, self.quarter, self.status, self.type, self.national_id_no, self.family_book_no))