from test_template import APITest

authorization_v1_test = APITest('v1/sentiment', 'Authorization')
authorization_v1_test.test_endpoint('alice', 'wonderland', sentence='i love potatoes')
authorization_v1_test.test_endpoint('bob', 'builder', sentence='il fait beau aujourdhui')

authorization_v2_test = APITest('v2/sentiment', 'Authorization')
authorization_v2_test.test_endpoint('alice', 'wonderland', sentence='it is raining today')
authorization_v2_test.test_endpoint('bob', 'builder', sentence='where is my umbrella')