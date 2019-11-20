from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import os
from sqlalchemy.ext.declarative import declarative_base
from fill_db import add_to_db,delete_from_db


file_path = os.path.abspath(os.getcwd())+"\database.db"
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'
db = SQLAlchemy(app)


taking = db.Table('takers',
	db.Column('person_id',db.Integer,db.ForeignKey('person.person_id')),
	db.Column('subject_id',db.Integer,db.ForeignKey('subject.subject_id'))
	)
mystudents = db.Table('mystudents',
	db.Column('professor_id',db.Integer,db.ForeignKey('professor.professor_id')),
	db.Column('students_id',db.Integer,db.ForeignKey('student.student_id'))
	)
mygroups = db.Table('mygroups',
	db.Column('person_id',db.Integer,db.ForeignKey('person.person_id')),
	db.Column('group_id',db.Integer,db.ForeignKey('group.group_id'))
	)
myanswers = db.Table('myanswers',
	db.Column('person_id',db.Integer,db.ForeignKey('person.person_id')),
	db.Column('answer_id',db.Integer,db.ForeignKey('answer.answer_id'))
	)


class Person(db.Model):
	name = db.Column(db.String(100))
	mail = db.Column(db.String(100))
	person_id = db.Column(db.Integer,primary_key = True)
	subjects = db.relationship('Subject',secondary=taking,backref = db.backref('takers'),lazy = 'dynamic')
	groups = db.relationship('Group',secondary=mygroups,backref = db.backref('mygroups'),lazy = 'dynamic')
	answers = db.relationship('Answer',secondary=myanswers,backref = db.backref('myanswers'),lazy = 'dynamic')
	__mapper_args__ = {"polymorphic_on": person_id}

	def add_person(self):
		db.session.add(self)
		db.session.commit()

	def remove_person(self):
		db.session.delete(self)
		db.session.commit()
	

class Subject(db.Model):
	 subject_id= db.Column(db.Integer,primary_key = True)
	 subject_name = db.Column(db.String(100))


class Professor(Person,db.Model):
	professor_id = db.Column(db.Integer,db.ForeignKey('person.person_id'),primary_key = True)
	students = db.relationship('Student',secondary = mystudents,backref= db.backref('mystudents'),lazy = 'dynamic')
	


class Student (Person,db.Model):
	student_id =	db.Column(db.Integer,db.ForeignKey('person.person_id'),primary_key = True)
	
	

class Faculty(Person,db.Model):
	faculty_id = db.Column(db.Integer,db.ForeignKey('person.person_id'),primary_key = True)
	

class Answer(db.Model):
	answer_id = db.Column(db.Integer,primary_key = True)
	answer_content = db.Column(db.String(200))

class Group(db.Model):
	group_id = db.Column(db.Integer,primary_key = True)
	group_name = db.Column(db.String(100))	


