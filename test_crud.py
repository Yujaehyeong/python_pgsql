import psycopg2
import config
from test_connect import cursor


def test_insert():
    try:
        conn = psycopg2.connect(**config.db) # 설정파일 만들어두고 불러와서 사용

        cursor = conn.cursor()
        cursor.execute("insert into pet values('성탄이', '길동이', 'dog','m', '2019-12-31' ,null )")


    except Exception as e:
        print('error: %s' % e )
    finally:
        cursor and cursor.close()
        conn and (conn.commit() or conn.close())

def test_select():
    try:
        conn = psycopg2.connect(**config.db) # 설정파일 만들어두고 불러와서 사용

        cursor = conn.cursor()
        cursor.execute("select * from pet")
        records = cursor.fetchall()

        for record in records:
            print(record, type(record))

    except Exception as e:
        print('error: %s' % e )
    finally:
        cursor and cursor.close()
        conn and (conn.commit() or conn.close())


def test_delete():

    try:
        conn = psycopg2.connect(**config.db) # 설정파일 만들어두고 불러와서 사용

        cursor = conn.cursor()
        cursor.execute("delete from pet where name = '성탄이'")

    except Exception as e:
        print('error: %s' % e )
    finally:
        cursor and cursor.close()
        conn and (conn.commit() or conn.close())



def main():
    test_insert()
    test_select()
    print('=================')
    test_delete()
    test_select()
    print('=================')
    # test_update()
    # test_select()
    print('=================')

__name__ == '__main__' and main()