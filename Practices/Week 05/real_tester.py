import unittest
import employee
import student
import pandas as pd


class TestEmployee(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    print("TEST EMPLOYEE STARTED")
  
  @classmethod
  def tearDownClass(cls):
    print("TEARING DOWN TEST EMPLOYEE \n")
    
  def setUp(self):
    print("Sub TestEmployee started")
    self.employee_df = pd.read_csv("sample_employees.csv")
  
  def test_fullname(self):
    print("Test fullname")
    self.assertTrue(employee.get_fullname("Bob", "Marley").islower())
    
  def test_salary(self):
    print("Test salary")
    # df = pd.read_csv("sample_employees.csv")
    self.assertEqual(employee.get_average(self.employee_df['salary']), self.employee_df['salary'].mean())
    
class TestStudent(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    print("TEST STUDENT STARTED")
  
  @classmethod
  def tearDownClass(cls):
    print("TEARING DOWN TEST STUDENT \n")
  
  def setUp(self):
    print("Sub TestSTUDENT started")
    self.students_df = pd.read_csv("sample_students.csv")
  
  def test_max_grade(self):
    print("Test max grade")
    # stu_df = pd.read_csv("sample_students.csv")
    # grade_max = stu_df['grade'].max()
    grade_max = self.students_df['grade'].max()
    self.assertEqual(student.get_max_grade(self.students_df['grade']), grade_max)
    
  def test_min_grade(self):
    print("Test min grade")
    # stu_df = pd.read_csv("sample_students.csv")
    grade_min = self.students_df['grade'].min()
    self.assertEqual(student.get_min_grade(self.students_df['grade']), grade_min)
    
    
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)