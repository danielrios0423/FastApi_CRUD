from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://uewrw9ijtyytkhcm:RqYGAuXmBIJEiCpyTAXW@bjxy452gwaqu3jrugi5p-mysql.services.clever-cloud.com/bjxy452gwaqu3jrugi5p")
meta = MetaData()
conn = engine.connect()
