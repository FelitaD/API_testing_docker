from test_template import APITest


class ContentTest(APITest):
    def test_condition(self, request, *args, **kwargs):
        response = request.json()
        score = response['score']
        expected_polarity = kwargs.get('polarity')

        if request.status_code == 200 and (score > 0 and expected_polarity == 'positive'):
            test_status = 'SUCCESS'
        elif request.status_code == 200 and (score < 0 and expected_polarity == 'negative'):
            test_status = 'SUCCESS'
        else:
            test_status = 'FAILURE'

        print(test_status, request.status_code, request.text)
        return test_status


content_v1_test = ContentTest('v1/sentiment', 'Content')
content_v1_test.test_endpoint('alice', 'wonderland', sentence='life is beautiful', polarity='positive')
content_v1_test.test_endpoint('alice', 'wonderland', sentence='that sucks', polarity='negative')

content_v2_test = ContentTest('v2/sentiment', 'Content')
content_v2_test.test_endpoint('alice', 'wonderland', sentence='life is beautiful', polarity='positive')
content_v2_test.test_endpoint('alice', 'wonderland', sentence='that sucks', polarity='negative')
