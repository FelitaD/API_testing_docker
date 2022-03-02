from test_template import APITest


authentification_test = APITest('permissions', 'Authentification')
authentification_test.test_endpoint('alice', 'wonderland')
authentification_test.test_endpoint('bob', 'builder')
authentification_test.test_endpoint('clementine', 'mandarine')
