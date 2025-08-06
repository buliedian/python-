import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """针对AnonymousSurvey的测试"""
    def setUp(self):
        """创建调查对象和答案"""
        question="What language did you first learn to speak?"
        self.my_survey=AnonymousSurvey(question)
        self.responses=['English','Spanish','Mandarin']
        
    
    def test_store_single_response(self):
        """测试单个答案，会被妥善存储"""
        self.my_survey.store_response(self,responses[0])
        self.assertIn(self.responses[0],self.my_survey.responses)

    def test_store_three_responses(self):
        """测试三个答案，妥善存储"""
        for response in self.responses:
            self.assertIn(response,self.mu_survey.responses)

            
    
    if __name__=='__main__':
        unittest.main()


