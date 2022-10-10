import unittest
import employee
import student
import pandas as pd

class TestEmployee(unittest.TestCase):
  
  @classmethod
  def setUpClass(cls):
    print("TestEmployee started")
    
  @classmethod
  def tearDownClass(cls):
    print("TestEmployee ended")
    
  def setUp(self):
    self.df = pd.read_csv("sample_employees.csv")
  
  def test_fullname(self):
    print("Testing fullname")
    self.assertTrue(employee.get_fullname("Bob", "Marley").islower())
  
  def test_average(self):
    # employee_df = pd.read_csv("sample_employees.csv")
    print("Testing average")
    avg_salary = self.df['salary'].mean()
    self.assertEqual(employee.get_average(self.df['salary']), avg_salary)
    
class TestStudent(unittest.TestCase):
  @classmethod
  def setUpClass(self):
    print("TestStudent started")
    
  @classmethod
  def tearDownClass(self):
    print("TestStudent ended")
    
  def setUp(self):
    self.df = pd.read_csv("sample_students.csv")
  
  def test_max_grade(self):
    # student_df = pd.read_csv('sample_students.csv')
    print("Testing max grade")
    max_grade = self.df['grade'].max()
    self.assertEqual(student.get_max_grade(self.df['grade']), max_grade)
    
  def test_min_grade(self):
    print("Testing min grade")
    # student_df = pd.read_csv('sample_students.csv')
    min_grade = self.df['grade'].min()
    self.assertEqual(student.get_min_grade(self.df['grade']), min_grade)
    
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)