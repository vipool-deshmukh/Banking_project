'''
 self.empId  = eid
        self.empName = enm
        self.empAge = eag
        self.empSalary = esal
        self.empEmail = email
        self.empRole = erol

# DB - QUERIES ARE NOT CASE SENSITIVE
'''


CREATE_TABLE  = '''
    CREATE TABLE EMP_INFO(
      EMP_ID INT AUTO_INCREMENT NOT NULL,
      EMP_NAME VARCHAR(40),
      EMP_AGE INT,
      EMP_SALARY FLOAT,
      EMP_EMAIL VARCHAR(40) UNIQUE,
      EMP_ROLE VARCHAR(40),
      PRIMARY KEY(EMP_ID)
      )
'''
INSERT_QUERY = "INSERT INTO EMP_INFO VALUES ({},'{}',{},{},'{}','{}')"
UPDATE_QUERY = ''' UPDATE EMP_INFO SET EMP_NAME = '{}', EMP_AGE={},EMP_SALARY = {},EMP_EMAIL = '{}',
        EMP_ROLE = '{}' WHERE EMP_ID = {}
        '''
DELETE_QUERY = '''DELETE FROM EMP_INFO WHERE EMP_ID = {} '''
SEARCH_EMPLOYEE_BY_ID = 'SELECT * FROM EMP_INFO WHERE EMP_ID = {}'
SEARCH_EMPLOYEE_BY_EMAIL = '''SELECT * FROM EMP_INFO WHERE EMP_EMAIL = '{}' '''
GET_ALL_EMPLOYEES = '''SELECT * FROM EMP_INFO'''
