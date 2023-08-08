from sqlalchemy.orm import Session

from src.assignments.schemas import AssignmentResponse
from src.assignments.exceptions import AssignmentNotFoundException
from src.models import Assignment

def get_assignment_by_id(db: Session, assignment_id: int):
    try:
         
        assignment = db.query(Assignment).where(Assignment.id == assignment_id).one_or_none
    except Exception as e: 
        raise AssignmentNotFoundException(f"could not find assignment {e}")
    return assignment

def get_assignments_by_course_id(db: Session, course_id: int): 
    try: 
        assignment = db.query(Assignment).where(Assignment.id == course_id)
    except Exception as e: 
        raise AssignmentNotFoundException(f"could not find assignment {e}")
    
    return assignment

def get_assignment_by_title(db: Session, assignment_title: str): 
    try: 
        assignment = db.query(Assignment).where(Assignment.title == assignment_title)
    except Exception as e: 
        raise AssignmentNotFoundException(f"could not find assignment that match your query {e}")
    
    return assignment  
    
def get_assignments(db: Session, skip: int = 0, limit : int = 100): 
    try: 
        assignments = db.query(Assignment).offset(skip).limit(limit) 
    except Exception as e: 
        print(e) 
    
    return assignments 
        