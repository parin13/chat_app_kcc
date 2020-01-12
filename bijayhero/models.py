from pymongo import MongoClient

def mongo_conn():
    try:
        print ("mongo")
        conn = MongoClient(host='127.0.0.1', port=27017)
        print("MongoDB Connected", conn)
        return conn.chat_application
    except Exception as e:
        print ("Error in mongo connection: ", e)


db = mongo_conn()

def register_model(name, password, phone, email):
	print ('inside mode')
	db.user_master.insert({'name':name,'email':email,'password':password,'phone':phone})


def login_model(name, pwd):
	data = db.user_master.find_one({'name':name, 'password':pwd})
	if data:
		return data['phone']



def is_active(uname,phone_no):
	db.user_master.update({'name':uname,'phone':phone_no},{'$set':{'active':1}})

def is_inactive(uname,phone):
	db.user_master.update({'name':uname,'phone':phone_no},{'$set':{'active':0}})


def is_online():
	data = db.user_master.find({'active':1},{'__id':-1,'name':1})
	print(data)